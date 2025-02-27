def convertToUniqueTargetName_andCreateCommentTxt(targetSemiPath:str, targetName:str, MODE:int):
    """
    MODE == :
        0: Do not shorten targetName. | *iref0
        1: Shorten targetName, but do not create commentTxt. | *iref1
        2: Shorten targetName, and create commentTxt. | *iref2
        3: Do iref0, but move to iref1 if user confirmation, else return.
        4: Do iref0, but move to iref2 if user confirmation, else return.
        5: Do iref1, but move to iref2 if user confirmation, else return.
    """
    if MODE == 0:
        targetNameTrue, targetExtension = separateTargetName(targetName)
        i, targetSemiPathAndExtensionLength = getLengthOf_targetExtension_and_targetSemiPathAndExtension(targetSemiPath, targetName)
        targetNameList = [targetNameTrue, preUniqueId, startUniqueIdAt, postUniqueId, dotQ, targetExtension]
        while True:
            lastLengthOfUniqueId = len(startUniqueIdAt)
            if os.path.exists(os.path.join(targetSemiPath, "".join(targetNameList))):
                break
            startUniqueIdAt += 1
            (redeclare) targetNameList
            if len(startUniqueIdAt) > start