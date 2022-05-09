from chicken import *

# Chicken Types
filet = Chicken("Filet",150,93,0)
filet.average_weight_per_piece = 93

breakfast = Chicken("Breakfast", 240, 55, 0)
breakfast.average_weight_per_piece = 55

spicy = Chicken("Spicy", 137, 105, 125)
nugget = Chicken("Nugget", 1010, 10, 22)
strip = Chicken("Strip", 341, 33, 53)
grilled_filet = Chicken("Grilled Filet", 130, 100, 125)
grilled_nugget = Chicken("Grilled Nugget", 872, 12, 20)

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