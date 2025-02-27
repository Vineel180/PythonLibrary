import os
from typing import Callable, Tuple




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
def convertToUniqueTargetName_returnElements(
targetSemiPath:str, targetName:str, maxLengthOfTargetNameTrue:int,
forShortTargetName_preUniqueStringId:str=" (", forShortTargetName_postUniqueStringId:str=")", forShortTargetName_startUniqueIdAt:int=1, 
forLongTargetName_preUniqueStringId:str="-", forLongTargetName_postUniqueStringId:str="", forLongTargetName_startUniqueIdAt:int=0, 
) -> str:
    targetNameTrue, targetExtension = separateTargetName(targetName)
    if maxLengthOfTargetNameTrue - len(targetNameTrue) > 0:
        trueIfLongTarget_falseIfShortTarget = True
    else:
        False
    #
    if trueIfLongTarget_falseIfShortTarget:
        preUniqueID = forShortTargetName_preUniqueStringId
        uniqueId = forShortTargetName_startUniqueIdAt
        postUniqueID = forShortTargetName_postUniqueStringId
    else:
        preUniqueID = forLongTargetName_preUniqueStringId
        uniqueId = forLongTargetName_startUniqueIdAt
        postUniqueID = forLongTargetName_postUniqueStringId
    ###
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















#group0
def convertToValidTargetName_andGenerateCommentFile(targetSemiPath:str, targetName:str, 
forLongTargetName_trueIfShorten_falseIfReturnNonZero:bool=True, forLongTargetName_trueIfCreateComment_falseIfNot:bool=True,
leadingStringToEmbedIfIllegalTargetName="_", 
) -> Tuple[int, str]:
    """
    Process:
        #step1 If targetName is illegal, add {leadingStringToEmbedIfIllegalTargetName} before targetName.
        #step2 Convert illegal targetName characters into similar looking yet legal characters.
    """
    #setup
    global listOfIllegalTargetNames
    oldTargetNameAsComment = targetName
    #step1
    if targetNameTrue in listOfIllegalTargetNames:
        targetName = leadingStringToEmbedIfIllegalTargetName + targetName
    #step2
    else:
        targetName = convertIllegalTargetNameCharacters(targetName)

    #UNCHECKED

    #step3
    targetNameTrue, targetExtension = separateTargetName(targetName)
    targetExtensionLength, targetSemiPathAndExtensionLength = getLengthOf_TargetExtension_And_TargetSemiPathAndExtension(targetSemiPath, targetName)
    maxLengthOfTargetNameTrue = max(255-targetExtensionLength, 260-targetSemiPathAndExtensionLength)
    if len(targetNameTrue) < maxLengthOfTargetNameTrue:
        if forLongTargetName_trueIfShorten_falseIfReturnNonZero:
            targetNameTrue = targetNameTrue[:maxLengthOfTargetNameTrue]
            trueIfLongUniqueIdFormat = True
        else:
            return [-1]
    else:
        trueIfLongUniqueIdFormat = False
