import os
def main():

"""Creating folder structure"""

"""Documentation"""
Doc = "1.Documentation"
Cust = "a. Customer Info"
Reports = "b. Reports"

#Findings Folder
"""Findings"""
Findings = "2.Findings"
Ext_F = "a. External"
Int_F = "b. Internal"
Phishing = "c. Phishing"

#Data Folder
"""Data"""
Data ="3.Data"
Database = "a. Database"
Phishing = "b. Phishing"
Templates = "i. Templates"
Payloads = "ii. Payloads"
Network = "c. Network Mapping"
ExtM = "i. External"
Nmap_E ="1. Nmap"
Eye_E = "2. Eyewitness"
Int_M = "Internal"
Nmap_I ="1. Nmap"
Eye_I = "2. Eyewitness"
Pen_Test = "d. Penetration Test"
Vul_Scan = "e. Vulnerability Scanning"
Ext_V = "i. External"
Nessus_E = "1. Nessus"
Internal_I = "1. Nessus"
Web_App = "f. Web App"
Burp = "i. Burp"
Nikto = "ii. Nikto"

#Where the directory will be exectuted
root = "<insert directory>"
#Folder Creation
path = f"{root}/{Doc}/{Cust}/{Reports}"

"""
path = f"{root}/{Findings}/{Int_F}/{Ext_F}/{Phishing}"
path = f"{root}/{Data}/{Database}/{Phishing}/{Database}/{Phishing}"
"""
print(path)

if not os.path.exists(path):
    os.makedirs(path)
else:
    os.removedirs(path)
