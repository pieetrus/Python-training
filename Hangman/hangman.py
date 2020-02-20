"""
HANGMAN
"""

from numpy.random import randint

words = ["łatwe", "ciężkie", "trudne", "zgaduj", "ziemniak", "kolor", "czerwony", "zielono", "astronauta", "python"]



def dash_word(word):
    dashed_word = []
    for i in range(0, len(word)):
        dashed_word.append("_")
    return dashed_word

def get_letter():
    print(" ")
    letter = input("Podaj literę:")
    if(len(letter) != 1):
        print("Podaj tylko jedną literę")
    else:
        if(not(letter.isalpha())):
            print("W słowie znajdują się same litery. Nie podawaj numerów.")
        else:
            return letter

def get_indexes_letter(input_str, letter):
    list_results = []
    lenght = len(input_str)
    index = 0
    while index < lenght:
        i = input_str.find(letter, index)
        if(i == -1):
            return list_results
        else:
            list_results.append(i)
            index = i + 1
    return list_results

def reveal(dashed_word, index, letter):
    x = 0
    for i in index:
        dashed_word[index[x]] = letter
        x += 1
    print_dashed(dashed_word)
    return dashed_word

def print_dashed(dashed_word):
    x=0
    for i in dashed_word:
        print(dashed_word[x] + " ", end="")
        x+=1
    print(" ")

def game(word, dashed_word, counter):
    while(counter < 6 and ("_" in dashed_word)):
        letter = get_letter()
        if(letter in word):
            print("Zgadłeś")
            index = get_indexes_letter(word, letter)
            reveal(dashed_word, index, letter)
            print("Liczba błędów: {}".format(counter))

        else:
            counter += 1
            print("Liczba błędów: {}".format(counter))
            print_dashed(dashed_word)
    if(not("_" in dashed_word)):
        print(" ")
        print("Gratulacje! Liczba popełnionych błędów w tej rozgrywce {}.".format(counter))


index = int(randint(0,len(words)))

word_to_guess = words[index]
counter = 0
dashed_word = dash_word(word_to_guess)





print(" ")
print("Witaj w wisielcu!")
print("Jeśli popełnisz 6 błędów to przegrywasz.")
print(" ")
print("Gotowy do gry? (y/n)")
decision = input("")

if(decision == 'n'):
    print("Oki. Wróć jak będziesz gotowy, czekam!")
    exit()
elif(decision == 'y'):
    print("Słowo które musisz zgadnąć zawiera {} liter.".format(len(word_to_guess)))
    print(" ")

    print_dashed(dashed_word)
    game(word_to_guess,dashed_word,counter)
else:
    print("Ehhh miało być y albo n. Wyłączam się za karę!")
    exit()