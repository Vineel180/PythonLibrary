def readFile(filePath: str) -> str:
    """
    returns file's text
    """
    with open(filePath, "r") as file:
        return file.read()

def writeFile(filePath: str, dataToWrite: str) -> None:
    """
    writes the file
    """
    with open(filePath, "w") as file:
        file.write(dataToWrite)
