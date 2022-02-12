import requests
import re
import time

def GetEmailBySite(SiteList):
    for i in SiteList:
        DataSite = requests.get(i)
        ReturnRegex = re.findall(f'[\w\.-]+@[\w\.-]+\.\w+', DataSite.text)
        if ReturnRegex:
            return(list(set(ReturnRegex)))
        else:
            return None
    
sites = ["https://github.com/LuciLua"]

cont_x=0

try:
    for x in sites:
        mails = (GetEmailBySite([x]))
        if (mails != "None" or mails != None):
            print(mails)
        cont_x=cont_x+1
except:
    print(x)
    pass 