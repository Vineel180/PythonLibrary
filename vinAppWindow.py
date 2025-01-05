import pygetwindow
from time import sleep

def appWindow_restoreYaMaximizeYaActivate(appWindowName:str, restore=True, maximize=True, activate=True):
    """1
    NOTE: IN BETA at try
    """
    appWindow = pygetwindow.getWindowsWithTitle(appWindowName)
    if appWindow:
        appWindow = appWindow[0]
        if restore:
            appWindow.restore()
        if maximize:
            appWindow.maximize()
        if activate:
            #
            try:
                appWindow.activate()
            except Exception as e:
                print("Encountered error: ", end="")
                print(e)
                input("Press Enter to continue.")
            #
        return True
    else:
        return False

def appWindow_restoreYaMaximizeYaActivate_withRetry(appWindowName:str, restore=True, maximize=True, activate=True, retryXTimes=3, retryEveryXSecs=1):
    status = False
    for i in range(retryXTimes):
        if appWindow_restoreYaMaximizeYaActivate(appWindowName, restore, maximize, activate):
            status = True
            break
        else:
            sleep(retryEveryXSecs)
    return status
