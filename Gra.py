#! python3
import pprint
import random

the_board_dictionary = {"1A": " ",  "1B": " ", "1C": " ", "2A": " ", "2B": " ", "2C": " ", "3A": " ", "3B": " ", "3C": " "}        


def is_field_empty(field_to_check, board_dictionary):
    if (field_to_check in board_dictionary):
        return board_dictionary[field_to_check] == " "
    else:
        print("Wybierz istniejące pole!")
        return False

def all_fields_are_nonempty(the_board_dicitionary):
    return not any(f == " " in f for f in the_board_dicitionary)

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

    while count_player_move <= 5:
        if count_player_move == count_bot_move:
            current_player_move = get_player_move(the_board_dictionary)
            the_board_dictionary[current_player_move] = 'X'
            count_player_move += 1
        else: #count_player_move <= count_bot_move:     
            current_bot_move = get_bot_move(the_board_dictionary)
            the_board_dictionary[current_bot_move] = "O"
            count_bot_move += 1
        draw_the_board(the_board_dictionary)

def draw_the_board(the_board_dictionary):
    print("   " + "A" + " B" + " C")
    print("1 |" + the_board_dictionary["1A"] + "|" + the_board_dictionary["1B"] + "|" + the_board_dictionary["1C"] + "|")
    print("  -------")
    print("2 |" + the_board_dictionary["2A"] + "|" + the_board_dictionary["2B"] + "|" + the_board_dictionary["2C"] + "|")
    print("  -------")
    print("3 |" + the_board_dictionary["3A"] + "|" + the_board_dictionary["3B"] + "|" + the_board_dictionary["3C"] + "|")


main_game_loop()
pprint.pprint(the_board_dictionary)


