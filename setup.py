from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
import subprocess
import sys

def install_playwright_requirements():
    try:
        # 1. Chromium Download
        print("📥 [Playwright] Downloading Chromium Browser...")
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
        
        # 2. install-deps if OS is Linux
        if sys.platform.startswith('linux'):
            print("📦 [Playwright] Detected Linux. Installing system dependencies (install-deps)...")
            # Run the command on its own as it may require sudo privilege
            subprocess.check_call([sys.executable, "-m", "playwright", "install-deps"])
            print("✅ [Playwright] System dependencies installed successfully!")
            
    except Exception as e:
        print(f"⚠️ [Playwright Warning] Automatic installation encountered an issue: {e}")
        print("💡 If needed, please run 'playwright install-deps' manually inside your virtual environment.")


# Additional installation for Playwright
class CustomInstallCommand(install):
    def run(self):
        # 1. Run the installation codes on setup
        super().run()
        install_playwright_requirements()

class CustomDevelopCommand(develop):
    def run(self):
        super().run()
        install_playwright_requirements()

setup(
    name="phishing-detector-api",
    version="1.0.0",
    author="SimmyK",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.136.1",
        "uvicorn[standard]==0.46.0",
        "playwright==1.59.0",
        "joblib==1.5.3",
        "pandas==3.0.2",
        "scikit-learn==1.8.0",
        "nest-asyncio==1.6.0"
    ],
    
    python_requires=">=3.11.15",

    # Use CustomInstallCommand after setting up the required packages.
    cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand
    },
)