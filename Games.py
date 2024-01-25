import random
import sys

def main():
    player_name = introduction()
    clear()
    list_games(player_name)
    
def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
def introduction():
    clear()
    print("What is your name?")
    input_name = input("Your Name Here: ")
    return(input_name)

def list_games(player_name):
    while True:
        print(f"Alright {player_name}, what game would you like to play?")
        print("(type \"list\" if you would like to know which games there are)'")
        player_choice = input("Type Here: ").lower()
            
        if player_choice == "list":
            clear()
            print("Here is a list of games:\n1. Dice Rolling\n2. Hangman\n3. Exit\n")
            list_games(player_name)
        elif player_choice == "dice rolling" or player_choice == "1":
            dice_game(player_name)
        elif player_choice == "hangman" or player_choice == "2":
            hang_man(player_name)
        elif player_choice == "exit" or player_choice == "3":
            break
        else:
            print("\n\033[4mPlease smake sure you are entering the correct input\033[0m\n")

def roll_die_1():
    return random.randint(1,6)

def roll_die_2():
    return random.randint(1,6)

def dice_game(player_name):
    while True:
        clear()
        input(f"{player_name}, please press enter to roll both dice")
        clear()
        die_1 = roll_die_1()
        die_2 = roll_die_2()
        total_dice = die_1 + die_2
        print(f"Your first die landed on a {die_1}!\n")
        print(f"Your second die landed on a {die_2}!\n")
        print("------------------\n")
        print(f"You scored {total_dice} in total!\n")
        
        keep_playing = input("would you like to continue playing? (y/n)").lower()
        
        if keep_playing != "y":
            print("Leaving Dice Rolling")
            clear()
            break
        
def hang_man(player_name):
    clear()
    print("I havent made this game yet...")
    keep_playing = input("Would you like to play a different game? (y/n)").lower()
        
    if keep_playing != "y":
        sys.exit()

main()
