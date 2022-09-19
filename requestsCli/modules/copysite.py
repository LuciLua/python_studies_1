import os
from pywebcopy import save_webpage

def copySite(args, path, openBrowser):
    
    openBrowser = args.openBrowser
    nameOfFolder = 'site'
    currentDir = os.getcwd()
    
    if (args.openBrowser):
        openBrowser = True
    if (args.copy and args.copy != True):
        nameOfFolder = args.copy
        
    kwargs = {'project_name': nameOfFolder}
    save_webpage(
        url=path,
        project_folder=currentDir,
        open_in_browser=openBrowser,
        **kwargs
    )