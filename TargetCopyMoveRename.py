from typing import Callable, Tuple

"""NOTE:
_vocabulary:
    def nyan_ ... : for users
    def i_    ... : for this file
"""

def i_copy_withRename():
def i_move_withRename():
def i_rename_withNone():

def i_baseFor__i_copyWithRename__i_moveWithRename__i_rename_withNone(
        functionToRun:Callable[[str, str, str, str, int, str, int, str, str], Tuple[int, str]], 
        initialTargetSemiPath:str, initialTargetName:str, finalTargetSemiPath:str, finalTargetName:str, outputMODE:int, 
        preIdString:str, startIdAt:int, postIdString:str, leadingStringForIllegalTargetName:str
        ) -> str:
    ###
    output = functionToRun(
            initialTargetSemiPath, initialTargetName, finalTargetSemiPath, finalTargetName, outputMODE, 
            preIdString, startIdAt, postIdString, leadingStringForIllegalTargetName
            )
    if output[0] == 0:
        return output[1]
    else:
    ###
        if output[0] == 1:
            print("initialTargetPath does not exist.", end=" ")
        elif output[0] == 2:
            print("finalTargetName is empty.", end=" ")
        elif output[0] == 3:
            print("finalTargetSemiPath cannot exist.", end=" ")
        elif output[0] == 4:
            print("Sum of lengths of targetSemiPath and targetExtension is equal to or more than 260.", end=" ")
        elif output[0] == 5:
            print(f"Exception '{output[1]}' occurred while running '{functionToRun.__name__}'.", end=" ")
        print("You will be re-entering the arguments. Enter = Yes; Any printing key + Enter = No.")
        fourSpaces = "    "
        ###
        showCurrentArguments = input("Show current arguments = Yes. Else no.")
        if not showCurrentArguments:
            print(f"{fourSpaces}initialTargetSemiPath: {initialTargetSemiPath}")
            print(f"{fourSpaces}initialTargetName: {initialTargetName}")
            print(f"{fourSpaces}finalTargetSemiPath: {finalTargetSemiPath}")
            print(f"{fourSpaces}finalTargetName: {finalTargetName}")
            print(f"{fourSpaces}outputMODE: {outputMODE}")
            print(f"{fourSpaces}preIdString: {preIdString}")
            print(f"{fourSpaces}startIdAt: {startIdAt}")
            print(f"{fourSpaces}postIdString: {postIdString}")
            print(f"{fourSpaces}leadingStringForIllegalTargetName: {leadingStringForIllegalTargetName}")
        #
        print
        _@onoging
        ###
        print()
        return i_baseFor__i_copyWithRename__i_moveWithRename__i_rename_withNone(
                functionToRun, 
                initialTargetSemiPath, initialTargetName, finalTargetSemiPath, finalTargetName, outputMODE, 
                preIdString, startIdAt, postIdString, leadingStringForIllegalTargetName
                )

def nyan_copy_withRename(
        initialTargetSemiPath:str, initialTargetName:str, finalTargetSemiPath:str, finalTargetName:str, outputMODE:int, 
        preIdString:str="-", startIdAt:int=0, postIdString:str="", leadingStringForIllegalTargetName:str="_"
        ) -> str:
    return i_baseFor__i_copyWithRename__i_moveWithRename__i_rename_withNone(
            i_copy_withRename, initialTargetSemiPath, initialTargetName, finalTargetSemiPath, finalTargetName, outputMODE, 
            preIdString, startIdAt, postIdString, leadingStringForIllegalTargetName
            )
def nyan_move_withRename(
        initialTargetSemiPath:str, initialTargetName:str, finalTargetSemiPath:str, finalTargetName:str, outputMODE:int, 
        preIdString:str="-", startIdAt:int=0, postIdString:str="", leadingStringForIllegalTargetName:str="_"
        ) -> str:
    return i_baseFor__i_copyWithRename__i_moveWithRename__i_rename_withNone(
            i_move_withRename, initialTargetSemiPath, initialTargetName, finalTargetSemiPath, finalTargetName, outputMODE, 
            preIdString, startIdAt, postIdString, leadingStringForIllegalTargetName
            )
def nyan_rename_withNone(
        targetSemiPath:str, initialTargetName:str, finalTargetName:str, outputMODE:int, 
        preIdString:str="-", startIdAt:int=0, postIdString:str="", leadingStringForIllegalTargetName:str="_"
        ) -> str:
    return i_baseFor__i_copyWithRename__i_moveWithRename__i_rename_withNone(
            i_rename_withNone, targetSemiPath, initialTargetName, targetSemiPath, finalTargetName, outputMODE, 
            preIdString, startIdAt, postIdString, leadingStringForIllegalTargetName
            )
