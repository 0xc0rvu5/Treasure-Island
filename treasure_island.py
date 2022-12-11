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

SURVIVING = True

def path_1(choice):
    if choice == 'left':
        print('**You have made it to the desolate tundra known as Alezaestradone. You lose. Try again**')


def path_2(choice):
    if choice == 'swim':
        print('**You notice crodiles ahead mid-swim and turn around. You eventually make it back to the island, but the boat is already gone. You lose.**')


def path_3(choice):
    match choice:
        case 'red':
            print('**You enter a room of ravid dogs! You lose.**')
        case 'blue':
            #win
            print('                            ~/!\~ WINNER ~/!\~                            ')
            print('You choose blue. You find the treasure. You win! Nice work and keep it up!')
            print('                            ~/!\~ WINNER ~/!\~                            ')
        case 'yellow':
            print('**You open the door and nothing is there. You lose.**')

while SURVIVING:
    choice = input('You are at a crossroad. Where do you go?\nType "left" or "right"\n ~ ').lower()
    path_1(choice)
    if choice != 'right':
        break
    choice = input('You have arrived to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat. Type "swim" to swim across.\n ~ ').lower()
    path_2(choice)
    if choice != 'wait':
        break
    choice = input('You eventually arrive at the island unharmed. There is a house with 3 doors. One "red", one "yellow", and one "blue". Which color do you choose?\n ~ ').lower()
    path_3(choice)
    break