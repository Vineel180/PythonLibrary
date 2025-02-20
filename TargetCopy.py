import os

# VERSION 1.00
# VARIABLES
listOfIllegalTargetNames = ["CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9", "CONIN$", "CONOUT$", "KBD$", "CLOCK$", "CONFIG$"]
listOfIllegalTargetNameCharacters = [   '?' , '<' , '>' , '\\' , '|' , '/' , ':' , '*' , '"'   ]
listOfLegalTargetNameCharacters_alternative  = [   '？' , '＜' , '＞' , '＼' , '｜' , '／' , '：' , '＊' , '“'   ]

# FUNCTIONS LEVEL=3X
def embedBetweenTargetNameTrueAndExtension(targetName:str, stringToEmbed:str) -> str:
    [targetNameTrue, targetNameExtension] = separateTargetName(targetName)
    dotQ = "." if targetNameExtension else ""
    return ( targetNameTrue + stringToEmbed + dotQ + targetNameExtension )
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
def reduceStringLength(stringToReduce:str, newLength:int) -> str:
    if len(stringToReduce) > newLength:
        return stringToReduce[0:newLength]
    return stringToReduce
def convertIntoUniqueTargetName(targetName:str, targetSemiPath:str, preUniqueID:str=" (", postUniqueID:str=")", startUniqueIdAt:int=1) -> str:
    uniqueID = startUniqueIdAt
    newTargetName = targetName
    while os.path.exists(   os.path.join(targetSemiPath, newTargetName)   ):
        stringToEmbed = preUniqueID + str(uniqueID) + postUniqueID
        newTargetName = embedBetweenTargetNameTrueAndExtension(targetName, stringToEmbed)
        uniqueID+=1
    return newTargetName
def convertIntoUniqueTargetName_returnElements(
        targetName:str, targetSemiPath:str, preUniqueID:str=" (", postUniqueID:str=")", startUniqueIdAt:int=1
        ) -> list[str, str, str, str, str, str]:
    """
    Output: [ targetNameTrue:str, preUniqueID:str, str(startUniqueIdAt):str, postUniqueID:str, dotQ:str, targetNameExtension:str ]
    """
    #
    [targetNameTrue, targetNameExtension] = separateTargetName(targetName)
    dotQ = "." if targetNameExtension else ""
    targetNameList = [targetNameTrue, preUniqueID, str(startUniqueIdAt), postUniqueID, dotQ, targetNameExtension]
    while os.path.exists(os.path.join(targetSemiPath, ( "".join(targetNameList) ) )):
        targetNameList = [targetNameTrue, preUniqueID, str(startUniqueIdAt), postUniqueID, dotQ, targetNameExtension]
        startUniqueIdAt += 1
    #
    return targetNameList

# FUNCTIONS LEVEL=3
#group1 forStep1&3
def rsplitStringOnce(stringToRsplit:str, rsplitCharacter:str) -> list[str, str]:
    output = stringToRsplit.rsplit(rsplitCharacter, 1)
    if len(output) == 2:
        return output
    else:
        return [output[0], ""]
def separateTargetPath(targetPath:str) -> list[str, str]:
    return rsplitStringOnce(targetPath, "\\")
def separateTargetName(targetName:str) -> list[str, str]:
    return rsplitStringOnce(targetName, ".")

#group2 forStep2
def removeLeadingCharacters(stringToModify:str, characterToRemove:str) -> str:
    while stringToModify[0] == characterToRemove:
        stringToModify = stringToModify[1:]
    return stringToModify
def removeTrailingCharacters(stringToModify:str, characterToRemove:str) -> str:
    while stringToModify[-1] == characterToRemove:
        stringToModify = stringToModify[:-1]
    return stringToModify

#group3 forStep5
def convertIllegalTargetNameCharacters(stringToModify:str) -> str:
    global listOfIllegalTargetNameCharacters
    global listOfLegalTargetNameCharacters_alternative
    stringToModify = list(stringToModify)
    for i in range(len(stringToModify)):
        if stringToModify[i] in listOfIllegalTargetNameCharacters:
            stringToModify[i] = listOfLegalTargetNameCharacters_alternative[listOfIllegalTargetNameCharacters.index(stringToModify[i])]
    return ( "".join(stringToModify) )

# FUNCTIONS LEVEL=2
def convertToValidTargetName(
    targetSemiPath:str, targetName:str, 

    trueIfShortenTargetName_falseIfNot:bool, forLongTargetName_trueIfShortenOnly_falseIfShortenWithComment:bool,

    leadingStringToEmbedIfIllegalTargetName:str="_",
    preUniqueID_forShortTargetName:str=" (", postUniqueID_forShortTargetName:str=")", startUniqueIdAt_forShortTargetName:int=1,
    preUniqueID_forLongTargetName:str="-", postUniqueID_forLongTargetName:str="", startUniqueIdAt_forLongTargetName:int=0
    ) -> list[str, str, str, bool]:
    """
    - Returns: [targetSemiPath:str, newTargetName:str, textForComment:str, successOrFailure:bool].
    - Process:
        - #step1 Returns FALSE if the parent folder cannot exist.
        - #step2 Returns FALSE if the unchangeable elements of the targetPath (ie {targetSemiPath+r"\" + targetNameExtension+("." if targetNameExtension else "")}) are 260 characters long or more.
        - #step3 Removes leading and trailing spaces, and trailing dots.
        - #step4 Adds leading {leadingStringToEmbedIfIllegalTargetName} to illegalTargetNames.
        - #step5 Replaces illegal characters in targetNames with legal characters.
    """
    textForComment = targetName
    #step1
    targetSemiPath = removeTrailingCharacters(targetSemiPath, "\\")
    if not os.path.isdir(targetSemiPath):
        try:
            os.makedirs(targetSemiPath)
        except:
            return targetSemiPath, targetName, "", False
    #step2
    [targetNameTrue, targetNameExtension] = separateTargetName(targetName)
    doesTargetHaveExtensionQ = 1 if targetNameExtension else 0
    targetNameExtensionLength = len(targetNameExtension) + doesTargetHaveExtensionQ
    targetSemiPathAndNameExtensionLength = len(targetSemiPath) + 1 + targetNameExtensionLength
    if targetSemiPathAndNameExtensionLength >= 260:
        return targetSemiPath, targetName, "", False
    #step3
    targetName = removeLeadingCharacters(targetName, " ")
    targetName = removeTrailingCharacters(targetName, " ")
    targetName = removeTrailingCharacters(targetName, ".")
    #setup for step4&5
    if targetName in listOfIllegalTargetNames:
        #step4
        targetName = leadingStringToEmbedIfIllegalTargetName + targetName
    else:
        #step5
        targetName = convertIllegalTargetNameCharacters(targetName)
    #step6



    while True:
        = convertIntoUniqueTargetName()
        = reduceLengthOfTargetNameTrue()
        if not os.path.exists():
            break
        if len() == 0:
            return , False




    if trueIfShortenTargetName_falseIfNot:
        if forLongTargetName_trueIfShortenOnly_falseIfShortenWithComment:
            #mode1
            maximumLengthPossibleForTargetNameTrue = min( (255-targetNameExtensionLength) , (260-targetSemiPathAndNameExtensionLength) )
            targetNameTrue = reduceStringLength(targetNameTrue, maximumLengthPossibleForTargetNameTrue)

            targetNameList = convertIntoUniqueTargetName_returnElements(targetName, targetSemiPath, 
                preUniqueID_forShortTargetName, postUniqueID_forShortTargetName, startUniqueIdAt_forShortTargetName)
            targetName = "".join(targetNameList)

        else:
            #mode2
    else:
        #mode0