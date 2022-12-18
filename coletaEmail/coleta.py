import requests
import re
import time
import argparse
import os


parser = argparse.ArgumentParser()

# Arguments
parser.add_argument(
    '-s',
    '--site',
    nargs='?',
    const=True,
    help='link of site')


def GetEmailBySite(SiteList):
    for i in SiteList:
        DataSite = requests.get(i)
        ReturnRegex = re.findall(f'[\w\.-]+@[\w\.-]+\.\w+', DataSite.text)
        if ReturnRegex:
            return (list(set(ReturnRegex)))
        else:
            return None

# if not exist: create. If already, just print a messasge


def createDirectory():
    if os.path.isdir('saves'):
        print("[...] directory already exists")
    else:
        os.makedirs('saves')
        print("[...] directory created at " + 'saves')


args = parser.parse_args()


def separate():
    all = args.site
    separe = all.split(',')
    return separe


if (args.site):
    createDirectory()
    cont_x = 0
    allMails = []
    sites = separate()
    file = open('saves/emails.txt', 'w')
else:
    print('Please, use [-s site,site,site] for continue')


def collectMails(mails):
    stringMail = (str(mails))
    allMails.append(stringMail)


def writeMails(allMails):

    convertStr = str(allMails)

    def removeComma(string):
        return string.replace(',', '\r')

    def removeAspas(string):
        return string.replace("'", '')

    def removeColchetes(string):
        return string.replace('[', '')

    def removeColchetesDois(string):
        return string.replace(']', '')

    def removeAspasDois(string):
        return string.replace('"', '')

    def removeWhiteSpace(string):
        return string.replace(' ', '')

    joinStr = removeComma(convertStr)
    joinStr = removeAspas(joinStr)
    joinStr = removeColchetes(joinStr)
    joinStr = removeColchetesDois(joinStr)
    joinStr = removeAspasDois(joinStr)
    joinStr = removeWhiteSpace(joinStr)

    file.write(joinStr)


if (args.site):
    try:
        for x in sites:
            mails = (GetEmailBySite([x]))
            if (mails != "None in this site" or mails != None):
                collectMails(mails)
            cont_x = cont_x+1
        writeMails(allMails)
        print("LOG IN: {0}\\saves\\emails.txt".format(os.getcwd()))

    except:
        print(x)
        pass

    file.close()
