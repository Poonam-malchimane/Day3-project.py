
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome To Tresure Island!")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroad. Do you want to go left or right? ").lower()
if choice1 == "left":
    choice2 = input("You've come to a lake. Do you want to swim across or wait for a boat? (swim/wait) ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with three doors. Which door do you choose? (red/blue/yellow) ").lower()
        if choice3 == "yellow":
            print("Congratulations! You found the treasure! You win!")
        elif choice3 == "blue":
            print("You enter a room full of beasts. Game Over.")
        elif choice3 == "red":
            print("You were burned by fire. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by a trout. Game Over.")
