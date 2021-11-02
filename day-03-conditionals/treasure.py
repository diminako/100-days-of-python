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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

game_position = 0
dead_status = False
door_color = 0
def status_check():    
    if ((game_position == 1) and dead_status == True ):
        print("You've fallen into a Hole. \nGame Over!!!")
    elif ((game_position == 2) and dead_status == True):
        print("You were attacked by a trout. \nGame Over!!!")
    elif ((game_position == 3) and (dead_status == True) and (door_color == 1)):
        print("You were burned in a fire. \nGame Over!!!")
    elif ((game_position == 3) and (dead_status == True) and (door_color == 2)):
        print("You were eaten by beasts. \nGame Over!!!")
    elif ((game_position == 3) and (dead_status == True) and door_color != 0):
        print("Game Over!!")

route = (input("Would you like to go left or right?")).lower()

if (route == "left"):
    game_position = 1
    route = (input("Would you like to swim or wait?")).lower()
elif (route == "right"):
    game_position = 1
    dead_status = True
else :
    route = (input("Would you like to go left or right?")).lower()

if (route == "wait"):
    game_position = 2
    route = input("which door would like to enter? Red, Blue, or Yellow?").lower()
elif (route == "swim"):
    game_position = 2
    dead_status = True

if (route == "yellow"):
    game_position = 3
    print("You win!!!")
elif (route == "red"):
    door_color = 1
    game_position = 3
    dead_status = True
elif (route == "blue"):
    door_color = 2
    game_position = 3
    dead_status = True

status_check()