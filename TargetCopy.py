import os

# VERSION 1.00
# VARIABLES
listOfIllegalTargetNames = [
    "CON", "PRN", "AUX", "NUL",
    "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9",
    "CONIN$", "CONOUT$", "KBD$", "CLOCK$", "CONFIG$"
]

# FUNCTIONS LEVEL=3
def separateTargetPath(targetPath:str) -> str:
    output = targetPath.rsplit("\\", 1)
    if len(output) == 2:
        return output
    else:
        return [output[0], ""]

def separateTargetName(targetName:str) -> str:
    output = targetName.rsplit(".", 1)
    if len(output) == 2:
        return output
    else:
        return [output[0], ""]

def embedBetweenTargetNameTrueAndExtension(targetName:str, stringToEmbed:str) -> str:
    [targetNameTrue, targetNameExtension] = separateTargetName(targetName)
    return ( targetNameTrue + stringToEmbed + "." + targetNameExtension )

def removeLeadingCharacters(stringToModify:str, characterToRemove:str) -> str:
    while stringToModify[0] == characterToRemove:
        stringToModify = stringToModify[1:]
    return stringToModify

def removeTrailingCharacters(stringToModify:str, characterToRemove:str) -> str:
    while stringToModify[-1] == characterToRemove:
        stringToModify = stringToModify[:-1]
    return stringToModify

def convertIllegalTargetNameCharacters(stringToModify:str) -> str:
    ###
    listOfIllegalInputCharacters = [   '?' , '<' , '>' , '\\' , '|' , '/' , ':' , '*' , '"'   ]
    listOfLegalOutputCharacters  = [   '？' , '＜' , '＞' , '＼' , '｜' , '／' , '：' , '＊' , '“'   ]
    ###
    stringToModify = list(stringToModify)
    for i in range(len(stringToModify)):
        if stringToModify[i] in listOfIllegalInputCharacters:
            stringToModify[i] = listOfLegalOutputCharacters[listOfIllegalInputCharacters.index(stringToModify[i])]
    return ( "".join(stringToModify) )

def reduceStringLength(stringToReduce:str, newLength:int) -> str:
    if len(stringToReduce) > newLength:
        return stringToReduce[0:newLength]
    return stringToReduce

def getTargetType(targetPath:str) -> int:
    """
    Output: 1 if file; 2 if folder; 0 is None.
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

def convertIntoUniqueTargetName_returnElements(targetName:str, targetSemiPath:str, preUniqueID:str=" (", postUniqueID:str=")", startUniqueIdAt:int=1) -> str:
    [targetNameTrue, targetNameExtension] = separateTargetName(targetName)
    dotQ = "." if targetNameExtension else ""
    targetNameList = [targetNameTrue, preUniqueID, str(startUniqueIdAt), postUniqueID, dotQ, targetNameExtension]
    while os.path.exists(os.path.join(targetSemiPath, ( "".join(targetNameList) ) )):
        targetNameList = [targetNameTrue, preUniqueID, str(startUniqueIdAt), postUniqueID, dotQ, targetNameExtension]
        startUniqueIdAt += 1
    return targetNameList

# FUNCTIONS LEVEL=2
def convertToValidTargetName(
    targetSemiPath:str, targetName:str, forLongTargetName_trueIfShortenOnly_falseIfShortenWithComment:bool,
    leadingStringToEmbedIfIllegalTargetName:str="_",
    preUniqueID:str=" (", postUniqueID:str=")", startUniqueIdAt:int=1
    ) -> list[str, str, bool]:
    """
    - Returns: [targetSemiPath:str, targetName:str, successOrFailure:bool].
    - Process:
        - #step1 Returns FALSE if the parent folder cannot exist.
        - #step2 Returns FALSE if the unchangeable elements of the targetPath (ie {targetSemiPath+1 + targetNameExtension+(1 if targetNameExtension else 0)}) are 260 characters or more.
        - #step3 Removes leading and trailing spaces, and trailing dots.
        - #step4 Adds leading {leadingStringToEmbedIfIllegalTargetName} to illegalTargetNames.
        - #step5 Replaces illegal characters in targetNames with legal characters.
    """
    #step1
    targetSemiPath = removeTrailingCharacters(targetSemiPath, "\\")
    if not os.path.isdir(targetSemiPath):
        try:
            os.makedirs(targetSemiPath)
        except:
            return targetSemiPath, targetName, False
    #step2
    [targetNameTrue, targetNameExtension] = separateTargetName(targetName)
    doesTargetHaveExtensionQ = 1 if targetNameExtension else 0
    targetNameExtensionLength = len(targetNameExtension) + doesTargetHaveExtensionQ
    targetSemiPathAndNameExtensionLength = len(targetSemiPath) + 1 + targetNameExtensionLength
    if targetSemiPathAndNameExtensionLength >= 260:
        return targetSemiPath, targetName, False
    #step3
    targetName = removeLeadingCharacters(targetName, " ")
    targetName = removeTrailingCharacters(targetName, " ")
    targetName = removeTrailingCharacters(targetName, ".")
    if targetName in listOfIllegalTargetNames:
        #step4
        targetName = leadingStringToEmbedIfIllegalTargetName + targetName
    else:
        #step5
        targetName = convertIllegalTargetNameCharacters(targetName)
    #step6
    maximumLengthPossibleForTargetNameTrue = min( (255-targetNameExtensionLength) , (260-targetSemiPathAndNameExtensionLength) )
    
    targetNameTrue = reduceStringLength(targetNameTrue, maximumLengthPossibleForTargetNameTrue)
    targetName = convertIntoUniqueTargetName(targetName, targetSemiPath, preUniqueID=" (", postUniqueID=")", startUniqueIdAt=1)
