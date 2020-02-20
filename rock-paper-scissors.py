# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:44:34 2020

@author: pietr
"""

from numpy.random import randint

figures_list = ["kamień", "papier", "nożyce"]
score = [0,0]


def menu():

    print("")
    print("0 - Kamień")
    print("1 - Papier")
    print("2 - Nożyce")
    
def get_player_choice():
    user_input = input("Wybieram:")
    try:
        int(user_input)
        if(int(user_input) >= 0 and int(user_input) <= 3):
            return int(user_input)  
        else:
            print("Liczba powinna być z zakresu 0-2")
            menu()
            get_player_choice()
    except ValueError:
        print("Podaj liczbę całkowitą")
        menu()
        get_player_choice()
        
def get_computer_choice():
    return randint(0,3)

def check_if_player_won(player, computer):
        if(player == 0 and computer == 1):
            print("Komputer wybrał papier. Przegrywasz.")
            return False
        if(player == 0 and computer == 2):
            print("Komputer wybrał nożyce. Wygrywasz!.")
            return True
        if(player == 1 and computer == 0):
            print("Komputer wybrał kamień. Wygrywasz!.")
            return True
        if(player == 1 and computer == 2):
            print("Komputer wybrał nożyce. Przegywasz.")
            return False
        if(player == 2 and computer == 0):
            print("Komputer wybrał kamień. Przegrywasz.")
            return False
        if(player == 2 and computer == 1):
            print("Komputer wybrał papier. Wygrywasz!.")
            return True

    
print("Witaj w grze kamień papier nożyce")
print("Do każdej figury jest przypisany odpowiedni numer")
print("wybierz figurę wpisując ten numer")
print("Powodzenia!!! :)")
    
while(score[0] <3 and score[1] <3):
    menu()
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    if(player_choice == computer_choice):
        print("Remis")
    else:
        if(check_if_player_won(player_choice,computer_choice)):
            score[0] += 1
        else:
            score[1] += 1
    
    print("")        
    print("Wynik: {}:{}".format(score[0], score[1]))

if(score[0] == 3):
    print("Gratulacje wygrywasz!!!")
else:
    print("Niestety komputer tym razem okazał się lepszy :(")
    





