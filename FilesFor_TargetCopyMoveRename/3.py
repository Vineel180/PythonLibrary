    """
    - Returns: [newTargetName:str, oldTargetNameAsComment:str, errorCode:int].
    - Process:
        - #step1 If {len(targetName)==0}, returns *errorCode=1*.
        - #step2 If the path doesn't exist, then it is made. If the path cannot exist, then *errorCode=2* is returned.
        - #step3 Returns *errorCode=3* if {len(targetSemiPath+r"\" + targetNameExtension+('.' if targetNameExtension else '') >= 260)}.
        - #step4 Removes leading and trailing spaces, and trailing dots.
        - #step5 Adds {leadingStringToEmbedIfIllegalTargetName} before illegalTargetNames.
        - #step6 Replaces illegal characters with similar looking legal characters, in targetNames.
    """
remove duplicates