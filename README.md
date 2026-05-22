# 🚀 Real-Time Phishing Website Detector
- Developed the ML model that detects if a given website is benign or not, with interactive UI made with FastAPI 😁
- Source of Data: https://www.kaggle.com/datasets/shashwatwork/phishing-dataset-for-machine-learning
---
## ❗ (Very IMPORTANT!) WARNING
- Due to the nature of phishing websites, it is **not recommended** to download this repository on your local desktop and run it, as the UI window works on your local PC in this case, and may bring all those malicious codes to your device 💥
- Instead, it is **highly advisable** for you to download and run this repository on a **virtual machine** and run it, or simply use a **docker container** 😊

## Features
- Trained and tested a randomforestclassifier from scikit-learn library for phishing website detection
- Developed a data parser that extracts information from the given url for analysis
- Created an interactive html webpage to use the data parser and ML model, by simply copying and pasting the urls that need to be examined

## 🛠️ Tech Stack ![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
- **Framework:** Scikit-Learn / PlayWright / FastAPI
- **DevOps:** Docker (To be uploaded!)

---
## 📁 Project Folder Structure
```text
Phishing_Websites/
├── Model_params/              # All model parameters are stored here
├── Model_training_testing/    # Code for training and testing model is here
├── Website_detector/          # Data parser and Web UI are here
├── model_config.json          # JSON file containing the information of key model
├── setup.py                   # Script for installing key packages of the project
└── README.md                  # Explanation of the whole project
```

## 🏃‍♂️ Getting Started

### 1. Prerequisites
- Python >= 3.11.15
- Compatible OS: Windows, Linux-based OS (except Alpine), MacOS (Not recommended)

### 2. Installation

```bash
# 1. How to clone the project
git clone https://github.com/SimmyKwon/Phishing_Website_Detector.git

# 2. Change to the current directory
cd Phishing_Website_Detector

# 3. Create virtual environment 
python -m venv {"Name of your choice for the project"}

#For Windows
.\{Name of your choice for the project}\Scripts\activate
#For Mac/Linux
source {Name of your choice for the project}/bin/activate

# 4. Install dependencies
pip install -e .
```

### 3. Running files (after installation)
```bash
#1. Model training and testing
python Model_training_testing/Model_train_test.py

#2. Using the interactive UI for website detection
python Website_detector/UI_Window.py
```
