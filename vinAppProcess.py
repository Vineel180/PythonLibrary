from psutil import process_iter
from subprocess import Popen, run

def stopApp_viaPsutilProcessiterTerminate(processName:str):
    """
    Slower than subprocess.Popen and subprocess.run.
    """
    for i in process_iter(attrs=["name", "pid"]):
        if processName == i.info["name"]:
            try:
                i.terminate()
                return True
            except:
                return False
    return False

def stopApp_viaSubprocessRunTaskkill(processName:str):
    """1
    Waits for a response.
    """
    try:
        cmd = f"taskkill /F /IM {processName}"
        status = run(cmd, shell=True)
        return (status.returncode == 0)
    except:
        return False

def stopApp_viaSubprocessPopenTaskkill(processName:str) -> None:
    """
    Does not wait for a response.
    """
    try:
        cmd = f"taskkill /F /IM {processName}"
        Popen(cmd, shell=True)
    except:
        pass
