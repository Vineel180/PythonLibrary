255
260

tester system

---


convertToUniqueFileName:
    Return errorCode= if {==""}
    Return errorCode= if {>=260}.
    Convert illegalTargetNameCharacters similar looking yet legal characters.
    Add {} before illegalTargetNames.
    Rstrip targetNameTrue if {len(targetNameTrue)>}
    Remove leading and trailing spaces, and leading spaces.
