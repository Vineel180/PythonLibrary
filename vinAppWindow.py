import pygetwindow

def appWindow_restoreYaMaximizeYaActivate(appWindowName:str, restore=True, maximize=True, activate=True):
    appWindow = pygetwindow.getWindowsWithTitle(appWindowName)
    if appWindow:
        appWindow = appWindow[0]
        if restore:
            appWindow.restore()
        if maximize:
            appWindow.maximize()
        if activate:
            appWindow.activate()
        return True
    else:
        return False
