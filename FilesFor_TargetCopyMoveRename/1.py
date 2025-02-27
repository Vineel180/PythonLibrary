import os
import shutil
import unicodedata
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
    long targetName or targetPath: len>255 or 260
NOTE:
    In my personal experience, naming a folder something like "con.txt" hasn't caused an error, 
    but since I couldn't find any resource to back this up (1/2), 
    and to avoid potential issues with poorly written code/apps that parse folders into targetNameTrue and targetExtension (ie do not check target type) (2/2), 
    I have decided to let this file's code restrict (ie auto-update) such folder names.
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

#

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
#group2
def getLengthOf_TargetExtension_And_TargetSemiPathAndExtension(targetSemiPath:str, targetName:str) -> Tuple[int, int]:
    targetNameTrue, targetExtension = separateTargetName(targetName)
    doesTargetHaveExtensionQ = 1 if targetExtension else 0
    targetExtensionLength = len(targetExtension) + doesTargetHaveExtensionQ
    targetSemiPathAndExtensionLength = len(targetSemiPath) + 1 + targetExtensionLength
    return targetExtensionLength, targetSemiPathAndExtensionLength

#

# FUNCTION LAYER 1
#group1
def normalizeString(stringToNormalize:str) -> str:
    return unicodedata.normalize('NFC', stringToNormalize)
#group0
def baseForCopyMoveRename(initialTargetSemiPath:str, initialTargetName:str, finalTargetSemiPath:str, finalTargetName:str, functionToRun:Callable[[str, str, str, str], Tuple[int, str]]) -> Tuple[int, str]:
    """
    Process:
        #step1 Trims initialTargetSemiPath & finalTargetSemiPath of trailing "\\"; initialTargetName & finalTargetName of leading & trailing " ", and trailing ".".
        #step2 Checks if the function should return any of the following: [1, ''], [2, ''], [3, ''], [4, ''].
        #step3 Updates finalTargetName using convertToValidTargetName_andGenerateCommentFile(). Returns the error, if any.
        #step4 Runs functionToRun(). Returns [5, e], if error {e}.
    Output: Returns:
        [1, '']: initialTarget doesn't exist.
        [2, '']: finalTargetName is empty.
        [3, '']: finalTargetSemiPath can't exist.
        [4, '']: {len(targetSemiPathAndExtension)>=260}.
        [5, e] : Exception {e} was raised while running functionToRun().
        ANYTHING ELSE: returns the error from convertToValidTargetName_andGenerateCommentFile(), if any.
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
    #step2 #a
    if not os.path.exists(os.path.join(initialTargetSemiPath, initialTargetName)):
        return [1, '']
    #b
    if not finalTargetName:
        return [2, '']
    #c
    if not os.path.exists(finalTargetSemiPath):
        try:
            os.makedirs(finalTargetSemiPath)
        except:
            return [3, '']
    #d
    if getLengthOf_TargetExtension_And_TargetSemiPathAndExtension(finalTargetSemiPath, finalTargetName)[1] >=260:
        return [4, '']
    #step3
    finalTargetName = convertToValidTargetName_andGenerateCommentFile(finalTargetSemiPath, finalTargetName)
    if finalTargetName[0] == 0:
        finalTargetName = finalTargetName[1]
    else:
        return finalTargetName
    #step4
    try:
        return functionToRun(os.path.join(initialTargetSemiPath, initialTargetName), os.path.join(finalTargetSemiPath, finalTargetName))
    except Exception as e:
        return [5, e]

#

# FUNCTION LAYER 0

#group0
def baseFor_copyWithRename(initialTargetSemiPath:str, initialTargetName:str, finalTargetSemiPath:str, finalTargetName:str) -> Tuple[int, str]:
    """
    Output: returns baseForCopyMoveRename().
    """
    #
    initialTargetSemiPath = normalizeString(initialTargetSemiPath)
    initialTargetName = normalizeString(initialTargetName)
    finalTargetSemiPath = normalizeString(finalTargetSemiPath)
    finalTargetName = normalizeString(finalTargetName)
    #
    if os.path.isdir(os.path.join(initialTargetSemiPath, initialTargetName)):
        shutilCopytree = partial(shutil.copytree(copy_function=baseFor_copyWithRename, dirs_exist_ok=True))
        return baseForCopyMoveRename(initialTargetSemiPath, initialTargetName, finalTargetSemiPath, finalTargetName, shutilCopytree)
    else:
        return baseForCopyMoveRename(initialTargetSemiPath, initialTargetName, finalTargetSemiPath, finalTargetName, shutil.copy2)
def baseFor_moveWithRename(initialTargetSemiPath:str, initialTargetName:str, finalTargetSemiPath:str, finalTargetName:str) -> Tuple[int, str]:
    """
    Output: returns baseForCopyMoveRename().
    """
    #
    initialTargetSemiPath = normalizeString(initialTargetSemiPath)
    initialTargetName = normalizeString(initialTargetName)
    finalTargetSemiPath = normalizeString(finalTargetSemiPath)
    finalTargetName = normalizeString(finalTargetName)
    #
    shutilMove = partial(shutil.move(copy_function=baseFor_copyWithRename))
    return baseForCopyMoveRename(initialTargetSemiPath, initialTargetName, finalTargetSemiPath, finalTargetName, shutilMove)
def baseFor_rename(targetSemiPath:str, initialTargetName:str, finalTargetName:str) -> Tuple[int, str]:
    """
    Output: returns baseForCopyMoveRename().
    """
    #
    targetSemiPath = normalizeString(targetSemiPath)
    initialTargetName = normalizeString(initialTargetName)
    finalTargetName = normalizeString(finalTargetName)
    #
    return baseForCopyMoveRename(targetSemiPath, initialTargetName, targetSemiPath, finalTargetName, os.rename)

# FUNCTION LAYER -1
#group0
def copy_withRename_nyan(initialTargetSemiPath:str, initialTargetName:str, finalTargetSemiPath:str, finalTargetName:str) -> Tuple[int, str]:
    output = baseFor_copyWithRename(initialTargetSemiPath, initialTargetName, finalTargetSemiPath, finalTargetName)
    if output[0] == 0:
        return output[1]
    else:
        if output[0] == 1:
            print("initialTargetFile doesn't exist. Retry.")
        elif output[0] == 2:
            print("finalTargetName is empty. Retry.")
        elif output[0] == 3:
            print("finalTargetSemiPath can't exist. Retry.")
        elif output[0] == 4:
            print("{len(targetSemiPathAndExtension)>=260}. Retry.")
        elif output[0] == 5:
            print(f"Exception '{output[1]}' was raised while running baseFor_copyWithRename(). Retry.")
        #
        initialTargetSemiPath = input("Input initialTargetSemiPath: ")
        initialTargetName = input("Input initialTargetName: ")
        finalTargetSemiPath = input("Input finalTargetSemiPath: ")
        finalTargetName = input("Input finalTargetName: ")
        return baseFor_copyWithRename(initialTargetSemiPath, initialTargetName, finalTargetSemiPath, finalTargetName)
def move_withRename_nyan(initialTargetSemiPath:str, initialTargetName:str, finalTargetSemiPath:str, finalTargetName:str) -> Tuple[int, str]:
def rename_nyan(targetSemiPath:str, initialTargetName:str, finalTargetName:str) -> Tuple[int, str]:
