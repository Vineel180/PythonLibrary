def getQualityOfFolderPath(folderPath:str) -> None:
    newLineAndFourSpaces = "\n    "
    BORDER_1 = 52 # 0.2 * 260
    BORDER_2 = 208 # 0.8 * 260
    #
    folderPath = removeTrailingCharacters(folderPath, "\\") + "\\"
    length = len(folderPath)
    print(f"Folder path length: {length} chars.")
    #
    print("Recommendations: ", end="")
    if length>BORDER_1:
        if length>BORDER_2:
            if length>260:
                print("INVALID")
                print(f"{newLineAndFourSpaces}Folder path length is over 260 chars. Reduce it by at least {length-260} chars to make the path valid, or {length-BORDER_1}/{}/{} chars to make it long/moderate/short respetively.")
            else:
                print(f"STRONG")
                print(f"{newLineAndFourSpaces}Folder path length is LONG. It is STRONGLY recommended to reduce it by preferably {length-BORDER_1} chars to make it short, or at least {length-BORDER_2} chars to make it moderate.")
        else:
            print(f"Moderate")
            print(f"{newLineAndFourSpaces}Folder path length is moderate. It is recommended to reduce it by at least {length-BORDER_1} chars.")
    else:
        print(f"None")
        print(f"{newLineAndFourSpaces}Folder path length is short (good).")
