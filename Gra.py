#! python3
import pprint
import random

the_board_dictionary = {"1A": " ", "1B": " ", "1C": " ", "2A": " ", "2B": " ", "2C": " ", "3A": " ", "3B": " ", "3C": " "}        

def is_field_empty(field_to_check):
    return the_board_dictionary[field_to_check] == " "

def all_fields_are_nonempty(the_board_dicitionary):
    return not any(f == " " in f for f in the_board_dicitionary)

def player_move():
    player_choice = input("Wybierz puste pole: ").upper()
    the_board_dictionary[player_choice] = 'X'
    draw_the_board(the_board_dictionary)
    main_game_loop(player_choice)

def bot_move():
    bot_choice = random.choice(list(the_board_dictionary))
    the_board_dictionary[bot_choice] = 'O'
    draw_the_board(the_board_dictionary) 
    main_game_loop(bot_choice)

def main_game_loop(player_choice, bot_choice, field_to_check):
    player_count_move = 0
    bot_count_move = 0
    #each_count_move = 0
    while player_count_move <= 5:
        if not(is_field_empty(field_to_check)):
            player_count_move += 1
            return player_move
        elif not(is_field_empty(field_to_check)): 
            bot_count_move += 1
            return bot_move
        else:
            pass

def draw_the_board(the_board_dictionary):
    print("   " + "A" + " B" + " C")
    print("1 |" + the_board_dictionary["1A"] + "|" + the_board_dictionary["1B"] + "|" + the_board_dictionary["1C"] + "|")
    print("  -------")
    print("2 |" + the_board_dictionary["2A"] + "|" + the_board_dictionary["2B"] + "|" + the_board_dictionary["2C"] + "|")
    print("  -------")
    print("3 |" + the_board_dictionary["3A"] + "|" + the_board_dictionary["3B"] + "|" + the_board_dictionary["3C"] + "|")

main_game_loop(player_move, bot_move)
pprint.pprint(the_board_dictionary)




'''

Dodać funkcje:

human_move(fields) nic nie zwraca
bot_move(fields) nic nie zwraca (pisze po planszy)
game_ended(fields) zwracać bool (true/fals)

madre sprawdzenie warunkow zwyciestwa
przerobic petle gry, bo teraz w jednej iteracji robia sie dwa ruchy

while warunki:
    ruch(plansza)

def ruch()
    if (ruch_gracza):
        human_move()
    else 
        bot_move

ale wtedy musisz sobie trzymac zmienna bool ktora sie zmienia na wartosc przeciwna 
(napisac funkcje do zmiany na wartosc przeciwna chyba, ze python juz cos takiego ma (reverse boolean google))



def main_game_loop():
    player_move = 0
    bot_move = 0
    all_moves = 0

    player_choice = input("Które pole chcesz zaznaczyć: ").upper()
    the_board_dictionary[player_choice] = 'X'
    draw_the_board(the_board_dictionary)

    bot_choice = random.choice(list(the_board_dictionary))
    the_board_dictionary[bot_choice] = 'O'
    draw_the_board(the_board_dictionary)   

    while player_move <= 3 and bot_move <= 3:
        player_choice = input("Wybierz puste pole: ").upper()

        #if (not all_fields_are_nonempty):
        #    print("dupa")

        all_moves += 1
        if (all_moves == 8):
            break
        while not(is_field_empty(player_choice)):
            player_choice = input("Wybierz puste pole: ").upper()

        the_board_dictionary[player_choice] = 'X'

        bot_choice = random.choice(list(the_board_dictionary))

        all_moves += 1
        if (all_moves == 8):
            break    
        while not(is_field_empty(bot_choice)):
            bot_choice = random.choice(list(the_board_dictionary))

        the_board_dictionary[bot_choice] = 'O'
        draw_the_board(the_board_dictionary)

        player_move += 1
        bot_move += 1

    print("Koniec gry")

'''


