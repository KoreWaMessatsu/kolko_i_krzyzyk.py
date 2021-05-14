#! python3
import pprint
import random

the_board_dictionary = {"1A": " ", "1B": " ", "1C": " ", "2A": " ", "2B": " ", "2C": " ", "3A": " ", "3B": " ", "3C": " "}        

def is_field_empty(field_to_check):
    return the_board_dictionary[field_to_check] == " "




def main_game_loop():
    player_move = 0
    bot_move = 0

    player_choice = input("Które pole chcesz zaznaczyć: ").upper()
    the_board_dictionary[player_choice] = 'X'
    draw_the_board(the_board_dictionary)

    bot_choice = random.choice(list(the_board_dictionary))
    the_board_dictionary[bot_choice] = 'O'
    draw_the_board(the_board_dictionary)   


    while player_move <= 3 and bot_move <= 3:
        player_choice = input("Wybierz puste pole: ").upper()
        
        while not(is_field_empty(player_choice)):
            player_choice = input("Wybierz puste pole: ").upper()
        
        the_board_dictionary[player_choice] = 'X'

        bot_choice = random.choice(list(the_board_dictionary))

        while not(is_field_empty(bot_choice)):
            bot_choice = random.choice(list(the_board_dictionary))
            
        the_board_dictionary[bot_choice] = 'O'
        draw_the_board(the_board_dictionary)

        player_move += 1
        bot_move += 1

def draw_the_board(the_board_dictionary):
    print("   " + "A" + " B" + " C")
    print("1 |" + the_board_dictionary["1A"] + "|" + the_board_dictionary["1B"] + "|" + the_board_dictionary["1C"] + "|")
    print("  -------")
    print("2 |" + the_board_dictionary["2A"] + "|" + the_board_dictionary["2B"] + "|" + the_board_dictionary["2C"] + "|")
    print("  -------")
    print("3 |" + the_board_dictionary["3A"] + "|" + the_board_dictionary["3B"] + "|" + the_board_dictionary["3C"] + "|")

main_game_loop()
pprint.pprint(the_board_dictionary)
