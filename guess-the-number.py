
from numpy.random import randint
number = randint(0,501)
attemps = 0


def get_number():
    user_input = input("Podaj liczbę:")
    try:
        int(user_input)
        return int(user_input)
    except ValueError:
        try:
            float(user_input)
            print("Liczba ma być liczbą całkowitą.")
        except ValueError:
            print("Podaj liczbę całkowitą.")
    
            


print("Witaj w grze zgadnij numer!")
print("Zgadnij liczbę. Znajduje się ona w przedziale 0-500")
playernumber = get_number()

while(playernumber != number):
    if(playernumber > number):
        print("Liczba jest za duża")
    if(playernumber < number):
        print("Liczba jest za mała")

    attemps += 1
    print("Liczba prób {}".format(attemps))
    playernumber = get_number()
    


    

if(playernumber == number):
    print("Gratulacje podałeś prawidłowy numer!!!!!")
    print("Liczba prób {}".format(attemps))

