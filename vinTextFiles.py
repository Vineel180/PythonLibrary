# MADE FOR ComputerStartup

def readFile(filePath: str) -> str:
    """1"""
    with open(filePath, "r") as file:
        return file.read()

def writeFile(filePath: str, dataToWrite: str) -> None:
    """1"""
    with open(filePath, "w") as file:
        file.write(dataToWrite)
