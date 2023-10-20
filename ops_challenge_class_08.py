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


#Date created: 18/10/2023
#Last Revision: 20/10/2023
#Purpose: Multiple exercices with lists

#Lists created
listn1 = ["potato","carrot","cabbage","brocolli","califlower","eggplant","beans","beans","pees","corn","rice"]
listn2 = ["meat","eggs","fish"]

print("\n")

#Shows the fourth element of the list
print("Fourth element of the list:",listn1[3])

print("\n")

#Shows from the sixth to the tenth element of the list
print("From sixth to tenth element of the list:",listn1[5:10])

print("\n")

#Changes the sixth element "eggplant" to "onion"
listn1[5] = "onion"
print("onion added to the list:",listn1)

print("\n")

#Adds garlic to the list
listn1.append("garlic")
print("garlic added to the list:",listn1)

print("\n")

#Removes the element "carrot" from the list
listn1.remove("carrot")
print("carrot removed from the list:",listn1)

print("\n")

#Counts how many of the same element exist in a list
x = listn1.count("beans")
print("There are",x,"beans in the list")

print("\n")

#Gives the element index number
y = listn1.index("corn")
print("corn index number is:",y)

print("\n")

#Sorts the list alphabeticly
listn1.sort()
print("List sorted alphabeticly:",listn1)

print("\n")

#Copies the list
z = listn1.copy()
print(z)

print("\n")

listn1.insert(3,"flower")
print("flower added to the list on the index number 3:",listn1)

print("\n")

a = listn1.pop(3)
print("Removed element:",a)
print("Current list:",listn1) 

print("\n")  

#Combines the 2 lists into one
listn1.extend(listn2)
print("listn1 and listn2 combined:",listn1)

print("\n")

#clears the list
listn1.clear()
print("List cleared!",listn1)





