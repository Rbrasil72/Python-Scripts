#!/usr/bin/env python3

#     _________
#    / ======= \
#   / __________\
#  | ___________ |
#  | | -       | |
#  | |         | |
#  | |_________| |_____________________________________
#  \=____________/   Rodrigo <Sud0Pirat3> Brasil       )
#  / """"""""""" \                                    /
# / ::::::::::::: \                               =D-'
#(_________________)


#Date created: 20/10/2023
#Last Revision: 20/10/2023
#Purpose: Multiple if-elif-else exercices

# Variables
a = 2
b = 3

print("\n") ##########################################

# if statement using the "equals" conditional
if a == b:
    print("a is equal to b")
# elif statement using the "does not equal" conditional
elif a != b:
    print("a is not equal to b")
# elif statement using the "greater than" conditional
elif a > b:
    print("a is greater than b")
# elif statement using the "greater than" conditional
elif a >= b:
    print("a is greater than and equal to b")
# elif statement using the "less than" conditional
elif a < b:
    print("a is lesser than b")
# elif statement using the "less than" conditional
elif a <= b:
    print("a is lesser than or equal to b")
# else statement to execute when none of the above conditions are met
else:
    print("a is not equal to b, and it's not greater or lesser than b")

print("\n") ##########################################

# Variables
c = 5
d = 10

if c > 0 and d < 15:
    print("Both conditions are met: c is greater than 0 and d is lesser than 15.")

print("\n") ##########################################

# Variables
x = 8
y = 20

if x < 5 or y > 15:
    print("At least one condition is met: x is lesser than 5 or y is greater than 15.")

print("\n") ##########################################

# Variables
temperature = 30
humidity = 70

if temperature > 25:
    if humidity > 60:
        print("It's hot and humid.")
    else:
        print("It's hot but not very humid.")
else:
    print("It's not hot.")

print("\n") ##########################################

# Variables
x = 10
y = 5

if x > y:
    pass  # Do nothing if x is greater than y
else:
    print("x is not greater than y.")
