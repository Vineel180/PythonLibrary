def convertToValidPath_withReadme(targetPath:str, 
                       trueForReduceDriveCharacter_falseForDefaultDriveCharacter:bool=True, defaultDriveCharacter:str="D", defaultDriveCharacter_windows:str="C", 
                       printWarningIfTargetSemiPathChanges:bool=True):
    """
    - (/8) Shorten OR Shorten-and-Add-Comment long all elements of the target PATH.
    # ensure to rename the file if a duplicate is already there
                            # ensure to keep the file extension
    """
    #step1
    targetPath_broken = breakTargetPath(targetPath)
    if not (len(targetPath_broken[0]) == 2):
        targetPath_broken.insert(0, "D:")
    else:
        if not targetPath_broken[0][1] == ":":
            targetPath_broken[0][1] = ":"
    if not os.path.exists(targetPath_broken[0]):
        if trueForReduceDriveCharacter_falseForDefaultDriveCharacter:
            try:
                listOfAlphabets_small.index()
            except:

        else:
            targetPath_broken[0][0] = defaultDriveCharacter
            if not os.path.exists(targetPath_broken[0]):
                targetPath_broken[0][0] = defaultDriveCharacter_windows

    if not (   (len(targetPath_broken_element1) == 2) and (targetPath_broken_element1[1]==":")   ):
        targetPath_broken_element1 = targetPath_broken_element1 + ":"
    else:

    if (   (len(targetPath_broken_element1) == 2) and (targetPath_broken_element1[1] == ":") and (os.path.exists(targetPath_broken_element1))   ):
    else:



"""
    #step 6
    targetName_charactersRemaining = 255 - len(targetName)
    targetPath = os.path.join(targetSemiPath, targetName)
    targetPath_charactersRemaining = 260 - len(targetPath)
    charactersRemaining = min(targetPath_charactersRemaining, targetName_charactersRemaining)
    if charactersRemaining < 0:

        if forLongTargetName_trueIfShortenOnly_falseIfShortenWithComment:
        else:

[targetNameTrue, targetNameExtension] = separateTargetName(targetName)
if len(targetSemiPath) + 2 + len(targetNameExtension) > maximumTargetSemiPathLength: # 2 = "\" + "."
"""

