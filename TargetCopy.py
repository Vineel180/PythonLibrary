import os
import shutil
from functools import partial
from typing import Callable

# FUNCTION LAYER 2
def removeLeadingCharacters(stringToModify:str, characterToRemove:str) -> str:
    while stringToModify[0] == characterToRemove:
        stringToModify = stringToModify[1:]
    return stringToModify
def removeTrailingCharacters(stringToModify:str, characterToRemove:str) -> str:
    while stringToModify[-1] == characterToRemove:
        stringToModify = stringToModify[:-1]
    return stringToModify

# FUNCTION LAYER 1
def baseForCopyMoveRename(initialTargetSemiPath:str, initialTargetName:str, finalTargetSemiPath:str, finalTargetName:str, 
functionToRun:Callable[[str, str, str, str], None]) -> list:
    """
    Output: Returns:
        [1]: initialTarget doesn't exist.
        [2]: finalTargetName is empty.
        [3]: finalTargetSemiPath cannot exist.
        [4, e]: exception {e} was raised in baseForCopyMoveRename().
        ANYTHING ELSE: returns convertToValidTargetName_andGenerateCommentFile().
    """
    initialTargetSemiPath = removeTrailingCharacters(initialTargetSemiPath, "\\")
    finalTargetSemiPath   = removeTrailingCharacters(finalTargetSemiPath, "\\")
    initialTargetName = removeLeadingCharacters(initialTargetName, " ")
    initialTargetName = removeTrailingCharacters(initialTargetName, " ")
    initialTargetName = removeTrailingCharacters(initialTargetName, ".")
    finalTargetName = removeLeadingCharacters(finalTargetName, " ")
    finalTargetName = removeTrailingCharacters(finalTargetName, " ")
    finalTargetName = removeTrailingCharacters(finalTargetName, ".")
    #
    if not os.path.exists(os.path.join(initialTargetSemiPath, initialTargetName)):
        return [1]
    if not finalTargetName:
        return [2]
    if not os.path.exists(finalTargetSemiPath):
        try:
            os.makedirs(finalTargetSemiPath)
        except:
            return [3]
    finalTargetName = convertToValidTargetName_andGenerateCommentFile(finalTargetSemiPath, finalTargetName)
    try:
        return functionToRun(os.path.join(initialTargetSemiPath, initialTargetName), os.path.join(finalTargetSemiPath, finalTargetName))
    except Exception as e:
        return [4, e]

# FUNCTION LAYER 0
def copy(initialTargetSemiPath:str, initialTargetName:str, finalTargetSemiPath:str, finalTargetName:str) -> list:
    """
    Output: returns baseForCopyMoveRename(). \n
    Process: Uses shutil.copy2() for files and shutilCopytree for folders.
    """
    shutilCopytree = partial(shutil.copytree(copy_function=copy, dirs_exist_ok=True))
    if os.path.isfile(os.path.join(initialTargetSemiPath, initialTargetName)):
        return baseForCopyMoveRename(initialTargetSemiPath, initialTargetName, finalTargetSemiPath, finalTargetName, shutil.copy2)
    else:
        return baseForCopyMoveRename(initialTargetSemiPath, initialTargetName, finalTargetSemiPath, finalTargetName, shutilCopytree)
def move(initialTargetSemiPath:str, initialTargetName:str, finalTargetSemiPath:str, finalTargetName:str) -> list:
    """
    Output: returns baseForCopyMoveRename().
    """
    shutilMove = partial(shutil.move(copy_function=copy))
    return baseForCopyMoveRename(initialTargetSemiPath, initialTargetName, finalTargetSemiPath, finalTargetName, shutilMove)
def rename(targetSemiPath:str, initialTargetName:str, finalTargetName:str) -> list:
    """
    Output: returns baseForCopyMoveRename().
    """
    return baseForCopyMoveRename(targetSemiPath, initialTargetName, targetSemiPath, finalTargetName, os.rename)
