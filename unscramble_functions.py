"""CSC108: Fall 2021 -- Assignment 1: Unscramble

This code is provided solely for the personal and private use of students 
taking the CSC108 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Michelle Craig, Tom Fairgrieve, Sadia Sharmin, and 
Jacqueline Smith.
"""

# Move constants
SHIFT = 'S'
FLIP = 'F'
CHECK = 'C'

# Constant for hint functions
HINT_MODE_SECTION_LENGTH = 3


def get_section_start(section_num: int, section_len: int) -> int:
    """Return the starting index of the section corresponding to section_num
    if the length of a section is section_len.

    >>> get_section_start(1, 3)
    0
    >>> get_section_start(2, 3)
    3
    >>> get_section_start(3, 3)
    6
    >>> get_section_start(4, 3)
    9
    """
    return 
    

# Write the rest of your functions here

def is_valid_move (move_input: str) -> bool:
    """Return valid move move_input 
    >>> is_valid_move('S')
    True
    
    >>> is_valid_move('G')
    False
    
    >>> is_valid_move('C')
    True
    
    """
    if move == SHIFT or move == FLIP or move == CHECK:
        return true
    
#
    
def get_num_sections (answer_string: str, section_num: int) -> int:
    """Return number of sections section_num in the answer answer_string
    
    
    """
    return 
#

def is_valid_section (valid_section: int, answer_string: str, section_length: int) -> bool:
    """Return 
    
    """
    return 
#

def check_section (game_state: str, answer_string: str, valid_section: int, section_length: int) -> bool:
    """Return the 
    
    """
    return 
#

def change_section (game_sate: str, applied_move: str, section_num: int, section_length: int) -> str:
    """Return updated game state game_state after applying 
    """
    return 
#

def section_needs_flip (game_state: str, answer_string: str, valid_section_num: int) -> bool:
    """Return 
    """
    return
#

def get_move_hint (game_state: str, answer_string: str, scrambled_section_num: int) -> str:
    """Return a move that will help user come closer to the solving the section 
    with the index scrambled_section_num in the str game_state coming to the answer answer_string 
    
    >>>get_move_hint('rde')
    
    """
    return
