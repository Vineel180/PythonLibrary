    if len(os.path.join(targetSemiPath, targetName)) > 260:
        if forLongTargetName_trueIfShorten_falseIfReturnFalse:
        else:
            return targetSemiPath, targetName, "", False
    else:




    #imp
    while True:
        = convertIntoUniqueTargetName()
        = reduceLengthOfTargetNameTrue()
        if not os.path.exists():
            break
        if len() == 0:
            return , False




    if forLongTargetName_trueIfShorten_falseIfReturnFalse:
        if forLongTargetName_trueIfShortenWithComment_falseIfShortenWithoutComment:
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