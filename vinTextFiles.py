def readFile(filePath: str) -> str:
    """1
    returns file's text
    """
    with open(filePath, "r") as file:
        return file.read()

def writeFile(filePath: str, dataToWrite: str) -> None:
    """1
    writes the file
    """
    with open(filePath, "w") as file:
        file.write(dataToWrite)
