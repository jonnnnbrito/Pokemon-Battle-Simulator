"""
TITLE: Pokemon Battle Simulator
-- Python program that simulates a batte between a user-seected Pokemon chatacter and a computer-selected Pokemon character

Five (5) functions to be made:
1. Selection of Pokemon Characters
    TODO -- Create an introduction for this game
    TODO -- The program provides a list of characters for the user (see picture).
    TODO -- Each pokemon hasa predefined base power, representing their natural strength. Power should range from weak to strong.
    TODO -- The actual power used in the battle will be a combination of the base power and a random factor between 0 and 1 (see computation).
    TODO -- Once selected, the user should be prompted by the Pokemon character and its corresponding power.
    
2. Computer-Generated Counter-Power 
    TODO -- The computer will randomly select a Pokemon character to battle against the user's selection with a counter-power value to simulate the opponent's strength. You can assign power for this or you have the option to use the same formula in the end-user Pokemon list.
    TODO -- Your program should explain how pokemon characters and powers were randomly selected.
    TODO -- For every battle, new selection of characters should take effect

3. Battle Simulation
    TODO -- The program should simulate a battle between the user-selected Pokemon character and the computer-selected Pokemon character.
    TODO -- If the user's power is greater than the computer's power, the user wins. If the computer's power is greater than the user's power, the computer wins. If the powers are equal, the battle is a draw.

4. Battle Continuation
    -- The program should prompt the user if they want to continue battling or not. If the user chooses to continue, the program should repeat the battle simulation process. If the user chooses to stop, the program should display the number of battles won by the user and the computer.
    -- You can use the 'c' character to continue the battle, and 'n' for new pokemon selection.
    -- The user can end the program in two ways: one by pressing 'x' button or by entering any character other than 'c' or 'n'.
    -- To ensure fairness, the comparison should be done after applying any random variations to both powers.

5. Output
    -- After each battle, the program should ask the user if they want to continue battling or not. If the user chooses to continue, the program should repeat the battle simulation process. If the user chooses to stop, the program should display the number of battles won by the user and the computer.
    -- The program should display the number of battles won by the user and the computer.
 """