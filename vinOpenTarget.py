from subprocess import Popen

# open a site/folder/app
from webbrowser import open as openSite
from os import startfile as openFolder
def openApp_viaSubprocessPopen(appStartupCommand:str):
    Popen(appStartupCommand, shell=True)

# open a list of sites/folders/apps
def openSites_inList(siteList: list[str]) -> None:
    for i in siteList:
        openSite(i)
def openFolders_inList(folderList: list[str]) -> None:
    for i in folderList:
        openFolder(i)
def openApps_inList__viaSubprocessPopen(appStartupCommandList:list[str]):
    for i in appStartupCommandList:
        Popen(i, shell=True)
