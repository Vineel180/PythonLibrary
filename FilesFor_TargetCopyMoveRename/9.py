# FUNCTIONS LEVEL=3X
def embedBetweenTargetNameTrueAndExtension(targetName:str, stringToEmbed:str) -> str:
    [targetNameTrue, targetExtension] = separateTargetName(targetName)
    dotQ = "." if targetExtension else ""
    return ( targetNameTrue + stringToEmbed + dotQ + targetExtension )
def getTargetType(targetPath:str) -> int:
    """
    Output: 1 if file; 2 if folder; 0 if None.
    """
    if os.path.isdir(targetPath):
        return 2
    elif os.path.isfile(targetPath):
        return 1
    else:
        return 0
def convertIntoUniqueTargetName(targetName:str, targetSemiPath:str, preUniqueID:str=" (", postUniqueID:str=")", startUniqueIdAt:int=1) -> str:
    uniqueID = startUniqueIdAt
    newTargetName = targetName
    while os.path.exists(   os.path.join(targetSemiPath, newTargetName)   ):
        stringToEmbed = preUniqueID + str(uniqueID) + postUniqueID
        newTargetName = embedBetweenTargetNameTrueAndExtension(targetName, stringToEmbed)
        uniqueID+=1
    return newTargetName
