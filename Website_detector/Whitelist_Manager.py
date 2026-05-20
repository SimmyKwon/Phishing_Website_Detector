#%%Import Packages

import os
import urllib.request
import zipfile
import io
from datetime import datetime, timedelta
from urllib.parse import urlparse

#%%Change the working directory
current_dir = os.path.abspath(__file__)
os.chdir(os.path.dirname(current_dir))

#Set URL for the data
UMBRELLA_URL = "https://s3-us-west-1.amazonaws.com/umbrella-static/top-1m.csv.zip"
#Backup URL
UMBRELLA_URL_2 = "https://api.sse.cisco.com/investigate/v2/topmillion"
CACHE_FILE = "umbrella_top_1m.csv"

#%%Function to download these whitelist

def load_live_whitelist():
    whitelist = set()
    download = True

    #Check if the csv was made in last 24 hours
    if os.path.exists(CACHE_FILE):
        file_mod_time = datetime.fromtimestamp(os.path.getmtime(CACHE_FILE))
        if datetime.now() - file_mod_time < timedelta(hours=24):
            print("Passing the update of whitelist!")
            download = False

    #If there is no existing file or it passed more than a day, get a new one
    if download:
        try:
            print("▶ Downloading top 1 Million CISCO Frequent Webpage data")
            #Open the url with url lib
            response = urllib.request.urlopen(UMBRELLA_URL)
            #Fetch the zip file
            zip_file = zipfile.ZipFile(io.BytesIO(response.read()))
            #Indicate the 1st element of the zip
            csv_name = zip_file.namelist()[0]

            #Write the contents of zip file 
            with open(CACHE_FILE, 'wb') as f:
                f.write(zip_file.read(csv_name))
            print("✅ Successfully built cache for whitelist")

        except Exception as e:
            print(f"❌ Failed to build a cache, using the existent one: {e}")
    
    #Fetch the data
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        whitelist.add(parts[1].lower())
                    else:
                        whitelist.add(parts[0].lower())
            print(f"✅ Loaded the whitelist data successfully with {len(whitelist)} rows.")
        except Exception as e:
            print(f"❌ Failed to load the whitelist data: {e}")

    return whitelist

# %%Function to be imported in other scripts

print("Initiating whitelist manager.")
WHITELIST_DOMAINS = load_live_whitelist()


#Make a function to be used in UI_Window.py

def is_whitelisted(url: str) -> bool:
    try:
        parsed_url = urlparse(url)
        #Make the domain name lowercase
        domain = parsed_url.netloc.lower()

        if domain.startswith("www."):
            domain_no_www = domain[4:]
            if domain_no_www in WHITELIST_DOMAINS:
                return True
            
        return domain in WHITELIST_DOMAINS
    except:
        return False