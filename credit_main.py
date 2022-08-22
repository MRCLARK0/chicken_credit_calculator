import math
from os import system, name
from chicken import *
from chicken_objects import *

menu_options = {
    1: 'Start Program',
    2: 'Exit'
}

def print_menu():
    print('------------------------------------------')
    for key in menu_options.keys():
        print(key, '-', menu_options[key])

def print_chicken():
    print('------------------------------------------')
    for key in chicken_options.keys():
        print(key, '-', chicken_options[key])

def clear():
    system('cls' if name == 'nt' else 'clear')

def option1():
    clear()
    print_chicken()
    submission_amount = 0
    chicken_option = 1

    try:
        chicken_option = int(input("Enter chicken type(1-7): "))
    except:
        print("Must be a whole number...")
        
    clear()

    choice = chicken_objects[chicken_option]

    while 1 > submission_amount or 10 < submission_amount:
        try:
            submission_amount = int(input("Enter submission amount(1-10): "))
        except:
            print("Must be a whole number...")

    weights = []
    pieces = []

    clear()

    for x in range(submission_amount):
        weight = 0
        while 1 > weight:
            try:
                weight = int(input(f"Enter weight of {choice.name.upper()} {x+1}: "))
            except:
                print("Must be a whole number...")
        weights.append(weight)

        piece = int(math.ceil(choice.min_piece_per_case - (weights[x] / choice.average_weight_per_piece)))
        pieces.append(piece)

    clear()

    print(f"--------{choice.name}--------")

    for x in range(len(weights)):
        print(f"{x+1}: {weights[x]} grams - {pieces[x]} pieces")


if __name__ == '__main__':
    while (True):
        print_menu()
        try:
            option = int(input('Enter your choice: '))
        except:
            print("Wrong input. Please enter a number...")
        if option == 1:
            option1()
        elif option == 2:
            print("Exiting...")
            exit()
        else:
            print("Invalid option. Please enter a number.")