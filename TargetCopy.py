import os
import shutil
from functools import partial
from typing import Callable, Tuple

# VERSION 1.00
"""
_vocabulary:
    target: File/Folder
    targetPath: target's path
    targetSemiPath: target's parent folder's path
    targetName: target's name
    targetNameTrue: target's name without extension.  "" if None.
    targetExtension: target's extension. "" if None.
    longTargetName or Path: len>255 or 260
"""

# VARIABLE LAYER 1
listOfIllegalTargetNames = [
    "CON", "PRN", "AUX", "NUL",
    "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9",
    "CONIN$", "CONOUT$",
    "COM¹", "COM²", "COM³",
    "LPT¹", "LPT²", "LPT³",
    ]
listOfIllegalTargetNameCharacters = [
    '?', '<', '>', '\\', '|', '/', ':', '*', '"', 
    '\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t'  , 
    '\n'  , '\x0b', '\x0c', '\r'  , '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', 
    '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', 
    '\x1e', '\x1f', 
    ]
listOfLegalAlternativesToIllegalTargetNameCharacters = [
    '？', '＜', '＞', '＼', '｜', '／', '：', '＊', '“', 
    "", "", "", "", "", "", "", "", "", "", 
    "", "", "", "", "", "", "", "", "", "", 
    "", "", "", "", "", "", "", "", "", "", 
    "", "", 
    ]

# FUNCTION LAYER 3
#group1
def rsplitStringOnce(stringToRsplit:str, rsplitCharacter:str) -> list[str, str]:
    output = stringToRsplit.rsplit(rsplitCharacter, 1)
    if len(output) == 2:
        return output
    elif len(output) == 1:
        return [output[0], ""]
    else:
        return ["", ""]
def separateTargetPath(targetPath:str) -> list[str, str]:
    return rsplitStringOnce(targetPath, "\\")
def separateTargetName(targetName:str) -> list[str, str]:
    return rsplitStringOnce(targetName, ".")

#group2
def convertIllegalTargetNameCharacters(stringToModify:str) -> str:
    global listOfIllegalTargetNameCharacters
    global listOfLegalAlternativesToIllegalTargetNameCharacters
    stringToModify = list(stringToModify)
    for i in range(len(stringToModify)):
        if stringToModify[i] in listOfIllegalTargetNameCharacters:
            stringToModify[i] = listOfLegalAlternativesToIllegalTargetNameCharacters[listOfIllegalTargetNameCharacters.index(stringToModify[i])]
    stringToModify = "".join(stringToModify)
    return stringToModify

#group3
def reduceStringLengthByX(stringToReduce:str, reduceLengthBy:int) -> str:
    stringLength=len(stringToReduce)
    if reduceLengthBy >= stringLength:
        return ""
    else:
        diff = stringLength-reduceLengthBy
        return stringToReduce[0:diff]

#group4
def convertToUniqueTargetName_returnElements(
targetSemiPath:str, targetName:str, maxLengthOfTargetNameTrue:int, trueIfShortTarget_falseIfLongTarget:bool, 
forShortTargetName_preUniqueStringId:str=" (", forShortTargetName_postUniqueStringId:str=")", forShortTargetName_startUniqueIdAt:int=1, 
forLongTargetName_preUniqueStringId:str="-", forLongTargetName_postUniqueStringId:str="", forLongTargetName_startUniqueIdAt:int=0, 
) -> str:
    """
    """
    if trueIfShortTarget_falseIfLongTarget:
        preUniqueID = forShortTargetName_preUniqueStringId
        uniqueId = forShortTargetName_startUniqueIdAt
        postUniqueID = forShortTargetName_postUniqueStringId
    else:
        preUniqueID = forLongTargetName_preUniqueStringId
        uniqueId = forLongTargetName_startUniqueIdAt
        postUniqueID = forLongTargetName_postUniqueStringId
    ###
    targetNameTrue, targetExtension = separateTargetName(targetName)
    dotQ = "." if targetExtension else ""
    targetNameTrueList = [targetNameTrue, preUniqueID, str(uniqueId), postUniqueID]
    targetNameTrue = "".join(targetNameTrueList)
    targetNameList = [targetNameTrue, preUniqueID, str(uniqueId), postUniqueID, dotQ, targetExtension]
    targetName = "".join(targetNameList)

    excessLengthValue = len(targetNameTrue) - maxLengthOfTargetNameTrue
    if excessLengthValue<0:
        if trueIfShortTarget_falseIfLongTarget:

        else:


    while os.path.exists(os.path.join(targetSemiPath, targetName)):
        uniqueId += 1
        targetNameList = [targetNameTrue, preUniqueID, str(uniqueId), postUniqueID, dotQ, targetExtension]

    return targetNameList

def convertToUniqueTargetName_withUniqueTargetNameForCommentTxt_returnElements() -> Tuple[str, str]:

# FUNCTION LAYER 2
#group1
def removeLeadingCharacters(stringToModify:str, characterToRemove:str) -> str:
    while stringToModify[0] == characterToRemove:
        stringToModify = stringToModify[1:]
    return stringToModify
def removeTrailingCharacters(stringToModify:str, characterToRemove:str) -> str:
    while stringToModify[-1] == characterToRemove:
        stringToModify = stringToModify[:-1]
    return stringToModify

#group0
def convertToValidTargetName_andGenerateCommentFile(targetSemiPath:str, targetName:str, 
forLongTargetName_trueIfShorten_falseIfReturnNonZero:bool=True, forLongTargetName_trueIfCreateComment_falseIfNot:bool=True,
leadingStringToEmbedIfIllegalTargetName="_", 
) -> list:
    """
    Process:
        #step1 If targetName is illegal, add {leadingStringToEmbedIfIllegalTargetName} before targetName.
        #step2 Convert illegal targetName characters into similar looking yet legal characters.
    Output: Returns:
        [5]: {len(finalTargetSemiPath + finalTargetExtension) >= 260}.
    """
    global listOfIllegalTargetNames
    oldTargetNameAsComment = targetName
    #
    targetNameTrue, targetExtension = separateTargetName(targetName)
    doesTargetHaveExtensionQ = 1 if targetExtension else 0
    targetExtensionLength = len(targetExtension) + doesTargetHaveExtensionQ
    targetSemiPathAndExtensionLength = len(targetSemiPath) + 1 + targetExtensionLength
    if targetSemiPathAndExtensionLength >= 260:
        return [5]
    #step1
    if targetNameTrue in listOfIllegalTargetNames:
        targetName = leadingStringToEmbedIfIllegalTargetName + targetName
    #step2
    else:
        targetName = convertIllegalTargetNameCharacters(targetName)
    #step3
    reduceStringLengthByX_var = max(targetExtensionLength-255, targetSemiPathAndExtensionLength-260, 0)
    targetNameTrue, targetExtension = separateTargetName(targetName)
    if reduceStringLengthByX_var != 0:
        targetNameTrue = reduceStringLengthByX(targetNameTrue, reduceStringLengthByX_var)
        trueIfLongUniqueIdFormat = True
        if not forLongTargetName_trueIfShorten_falseIfReturnNonZero:
            return [6]
    else:
        trueIfLongUniqueIdFormat = False
    if forLongTargetName_trueIfCreateComment_falseIfNot:
    else:

    


    #ONGOING

# FUNCTION LAYER 1
#group0
def baseForCopyMoveRename(initialTargetSemiPath:str, initialTargetName:str, finalTargetSemiPath:str, finalTargetName:str, 
functionToRun:Callable[[str, str, str, str], None]) -> list:
    """
    Process:
        #step1 Trims: initialTargetSemiPath & finalTargetSemiPath of trailing "\\"; initialTargetName & finalTargetName of leading and trailing " ", and trailing ".".
    Output: Returns:
        [1]: initialTarget doesn't exist.
        [2]: finalTargetName is empty.
        [3]: finalTargetSemiPath cannot exist.
        [4, e]: exception {e} was raised in baseForCopyMoveRename().
        ANYTHING ELSE: returns convertToValidTargetName_andGenerateCommentFile().
    """
    #step1
    initialTargetSemiPath = removeTrailingCharacters(initialTargetSemiPath, "\\")
    finalTargetSemiPath   = removeTrailingCharacters(finalTargetSemiPath, "\\")
    initialTargetName = removeLeadingCharacters(initialTargetName, " ")
    initialTargetName = removeTrailingCharacters(initialTargetName, " ")
    initialTargetName = removeTrailingCharacters(initialTargetName, ".")
    finalTargetName = removeLeadingCharacters(finalTargetName, " ")
    finalTargetName = removeTrailingCharacters(finalTargetName, " ")
    finalTargetName = removeTrailingCharacters(finalTargetName, ".")
    #step1 end
    if not os.path.exists(os.path.join(initialTargetSemiPath, initialTargetName)):
        return [1]
    #
    if not finalTargetName:
        return [2]
    #
    if not os.path.exists(finalTargetSemiPath):
        try:
            os.makedirs(finalTargetSemiPath)
        except:
            return [3]
    #
    finalTargetName = convertToValidTargetName_andGenerateCommentFile(finalTargetSemiPath, finalTargetName)
    try:
        return functionToRun(os.path.join(initialTargetSemiPath, initialTargetName), os.path.join(finalTargetSemiPath, finalTargetName))
    except Exception as e:
        return [4, e]

# FUNCTION LAYER 0
#group0
def copy_withRename(initialTargetSemiPath:str, initialTargetName:str, finalTargetSemiPath:str, finalTargetName:str) -> list:
    """
    Output: returns baseForCopyMoveRename().
    """
    shutilCopytree = partial(shutil.copytree(copy_function=copy_withRename, dirs_exist_ok=True))
    if os.path.isdir(os.path.join(initialTargetSemiPath, initialTargetName)):
        return baseForCopyMoveRename(initialTargetSemiPath, initialTargetName, finalTargetSemiPath, finalTargetName, shutilCopytree)
    else:
        return baseForCopyMoveRename(initialTargetSemiPath, initialTargetName, finalTargetSemiPath, finalTargetName, shutil.copy2)
def move_withRename(initialTargetSemiPath:str, initialTargetName:str, finalTargetSemiPath:str, finalTargetName:str) -> list:
    """
    Output: returns baseForCopyMoveRename().
    """
    shutilMove = partial(shutil.move(copy_function=copy_withRename))
    return baseForCopyMoveRename(initialTargetSemiPath, initialTargetName, finalTargetSemiPath, finalTargetName, shutilMove)
def rename(targetSemiPath:str, initialTargetName:str, finalTargetName:str) -> list:
    """
    Output: returns baseForCopyMoveRename().
    """
    return baseForCopyMoveRename(targetSemiPath, initialTargetName, targetSemiPath, finalTargetName, os.rename)
