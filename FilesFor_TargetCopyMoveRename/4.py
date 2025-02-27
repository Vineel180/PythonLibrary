import os

def reduceStringFromRightByIntChars(stringToReduce:str, reduceIntChars:int) -> str:
    return stringToReduce[: len(stringToReduce)-reduceIntChars ]

def convertToUniqueTargetName(targetSemiPath:str, targetName:str, maxLengthOfTargetNameTrue:int, 
forShortTargetName_preUniqueStringId:str=" (", forShortTargetName_postUniqueStringId:str=")", forShortTargetName_startUniqueIdAt:int=1, 
forLongTargetName_preUniqueStringId:str="-", forLongTargetName_postUniqueStringId:str="", forLongTargetName_startUniqueIdAt:int=0, 
) -> str:
    """
    """
    targetNameTrue, targetExtension = separateTargetName(targetName)
    dotQ = "." if targetExtension else ""
    reduceTargetNameTrueByIntChars = max(0, len(targetNameTrue)-maxLengthOfTargetNameTrue)
    if reduceTargetNameTrueByIntChars != 0:
        targetNameTrue = reduceStringFromRightByIntChars(targetNameTrue, reduceTargetNameTrueByIntChars)
        trueIfLongTargetName_falseIfShortTargetName = True
    else:
        trueIfLongTargetName_falseIfShortTargetName = False
    #
    if trueIfLongTargetName_falseIfShortTargetName:
        preUniqueID = forShortTargetName_preUniqueStringId
        uniqueId = forShortTargetName_startUniqueIdAt
        postUniqueID = forShortTargetName_postUniqueStringId
    else:
        preUniqueID = forLongTargetName_preUniqueStringId
        uniqueId = forLongTargetName_startUniqueIdAt
        postUniqueID = forLongTargetName_postUniqueStringId
    #
    targetNameList = [targetNameTrue, preUniqueID, str(uniqueId), postUniqueID, dotQ, targetExtension]
    targetName = "".join(targetNameList)
    while os.path.exists(os.path.join(targetSemiPath, targetName)):
        uniqueId += 1
        targetNameList = [targetNameTrue, preUniqueID, str(uniqueId), postUniqueID, dotQ, targetExtension]
    targetName = "".join(targetNameList)
    return targetName
