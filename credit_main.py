import math
from chicken import *
from chicken_objects import *

chicken_options = {
    1: filet.name,
    2: spicy.name,
    3: nugget.name,
    4: strip.name,
    5: grilled_filet.name,
    6: grilled_nugget.name,
    7: breakfast.name
}

chicken_objects = {
    1: filet,
    2: spicy,
    3: nugget,
    4: strip,
    5: grilled_filet,
    6: grilled_nugget,
    7: breakfast
}

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

def option1():

    print_chicken()
    submission_amount = 0
    chicken_option = 1

    try:
        chicken_option = int(input("Enter chicken type(1-7): "))
    except:
        print("Must be a whole number...")

    choice = chicken_objects[chicken_option]
    
    print(f"--------{choice.name}--------")

    while 1 > submission_amount or 10 < submission_amount:
        try:
            submission_amount = int(input("Enter submission amount(1-10): "))
        except:
            print("Must be a whole number...")

    weights = []
    pieces = []

    for x in range(submission_amount):
        weight = 0
        while 1 > weight:
            try:
                weight = int(input(f"Enter weight of item {x+1}: "))
            except:
                print("Must be a whole number...")
        weights.append(weight)

        piece = int(math.ceil(choice.min_piece_per_case - (weights[x] / choice.average_weight_per_piece)))
        pieces.append(piece)

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