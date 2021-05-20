#! python3
import pprint
import random

the_board_dictionary = {"1A": " ",  "1B": " ", "1C": " ", "2A": " ", "2B": " ", "2C": " ", "3A": " ", "3B": " ", "3C": " "}        

def is_field_empty(field_to_check, board_dictionary):
    if field_to_check in board_dictionary:
        return board_dictionary[field_to_check] == " "
    else:
        if len(the_board_dictionary.values()) > 1:
            print("Wybierz istniejące pole!")
            return False

#def all_fields_are_nonempty(the_board_dicitionary):
#    return not any(f == " " in f for f in the_board_dicitionary)

def player_winning_con(the_board_dictionary):
    #check_field = "X"
    for check_field in the_board_dictionary:
        if the_board_dictionary["1A"] == "X" and the_board_dictionary["2A"] == "X" and the_board_dictionary["3A"] == "X":
            print("Wygrałeś!")
            return True
        elif the_board_dictionary["1A"] == "X" and the_board_dictionary["1B"] == "X" and the_board_dictionary["1C"] == "X":
            print("Wygrałeś!")
            return True
        elif the_board_dictionary["2A"] == "X" and the_board_dictionary["2B"] == "X" and the_board_dictionary["2C"] == "X":
            print("Wygrałeś!")
            return True
        elif the_board_dictionary["3A"] == "X" and the_board_dictionary["3B"] == "X" and the_board_dictionary["3C"] == "X":
            print("Wygrałeś!")
            return True
        elif the_board_dictionary["1A"] == "X" and the_board_dictionary["2B"] == "X" and the_board_dictionary["3C"] == "X":
            print("Wygrałeś!")
            return True
        elif the_board_dictionary["1B"] == "X" and the_board_dictionary["2B"] == "X" and the_board_dictionary["3B"] == "X":
            print("Wygrałeś!")
            return True
        elif the_board_dictionary["1C"] == "X" and the_board_dictionary["2C"] == "X" and the_board_dictionary["3C"] == "X":
            print("Wygrałeś!")
            return True
        else:
            return False

def bot_winning_con(the_board_dictionary):
    #check_field = "X"
    for check_field in the_board_dictionary:
        if the_board_dictionary["1A"] == "O" and the_board_dictionary["2A"] == "O" and the_board_dictionary["3A"] == "O":
            print("Bot wygrał!")
            return True
        elif the_board_dictionary["1A"] == "O" and the_board_dictionary["1B"] == "O" and the_board_dictionary["1C"] == "O":
            print("Bot wygrał!")
            return True
        elif the_board_dictionary["2A"] == "O" and the_board_dictionary["2B"] == "O" and the_board_dictionary["2C"] == "O":
            print("Bot wygrał!")
            return True
        elif the_board_dictionary["3A"] == "O" and the_board_dictionary["3B"] == "O" and the_board_dictionary["3C"] == "O":
            print("Bot wygrał!")
            return True
        elif the_board_dictionary["1A"] == "O" and the_board_dictionary["2B"] == "O" and the_board_dictionary["3C"] == "O":
            print("Bot wygrał!")
            return True
        elif the_board_dictionary["1B"] == "O" and the_board_dictionary["2B"] == "O" and the_board_dictionary["3B"] == "O":
            print("Bot wygrał!")
            return True
        elif the_board_dictionary["1C"] == "O" and the_board_dictionary["2C"] == "O" and the_board_dictionary["3C"] == "O":
            print("Bot wygrał!")
            return True
        else:
            return False

def get_player_move(gamefield):
    temporary_choice = ""
    while not is_field_empty(temporary_choice, gamefield):
        temporary_choice = input("Wybierz puste pole: ").upper()
    return temporary_choice

def get_bot_move(gamefield):
    temporary_bot_choice = ""
    while not is_field_empty(temporary_bot_choice, gamefield):
            temporary_bot_choice = random.choice(list(the_board_dictionary))
    return temporary_bot_choice

def main_game_loop():
    count_player_move = 0
    count_bot_move = 0

    while player_winning_con(the_board_dictionary) == False:
        if bot_winning_con(the_board_dictionary) == False: 
            if count_player_move < 4:
                if count_player_move == count_bot_move:
                    current_player_move = get_player_move(the_board_dictionary)
                    the_board_dictionary[current_player_move] = 'X'
                    count_player_move += 1
                elif count_player_move <= 4: 
                    current_bot_move = get_bot_move(the_board_dictionary)
                    the_board_dictionary[current_bot_move] = "O"
                    count_bot_move += 1
                elif player_winning_con == True:
                    break
                elif bot_winning_con == True:
                    break
                draw_the_board(the_board_dictionary)
            else:
                print("Remis")
                break


def draw_the_board(the_board_dictionary):
    print("   " + "A" + " B" + " C")
    print("1 |" + the_board_dictionary["1A"] + "|" + the_board_dictionary["1B"] + "|" + the_board_dictionary["1C"] + "|")
    print("  -------")
    print("2 |" + the_board_dictionary["2A"] + "|" + the_board_dictionary["2B"] + "|" + the_board_dictionary["2C"] + "|")
    print("  -------")
    print("3 |" + the_board_dictionary["3A"] + "|" + the_board_dictionary["3B"] + "|" + the_board_dictionary["3C"] + "|")

main_game_loop()
pprint.pprint(the_board_dictionary)


