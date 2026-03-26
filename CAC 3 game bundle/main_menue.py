import CAC
from CAC import the_first_game
from CAC import first_game_won
print("main_menue")
print("what installment of the series do you want to play?")
game = input("1, 2, or 3? ")
if game == "1":
    the_first_game()
if game == "2":
    print("the second game is currently in development, check back later!")
if game == "3":
    print("the third game is currently in development, check back later!")