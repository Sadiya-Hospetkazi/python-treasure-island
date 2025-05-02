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
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome To Treasure island")
print("Your mission is to find Treasure.")

choice1=input('You\'re at a cross road.Where do you want to go? type "Left" or "right".').lower()

if choice1=="left":
    choice2=input('you come to lake.There is an island in the middle of lake'
                  'Type "wait" to wait for boat Type "swim" to swim across the lake.').lower()
    if choice2 == "wait":
       choice3=input("You arrive at island unharmed."
                     "There is house with 3 door ."
                     "One is yellow and one is blue and one is red "
                     "which color you chose").lower()
       if choice3 == "blue":
           print("🐊 You enter a room full of beasts. Game Over.")
       elif choice3 == "red":
           print("🔥 It's a room full of fire. Game Over.")
       elif choice3=="yellow":
           print("🎉 Congratulation you found treasure")
       else:
           print("🚪 You chose a door that doesn't exist")
    else:
        print("🐟 You were attacked by a trout. Game Over.")
else:
    print("💀 You fell into a hole. Game Over.")
