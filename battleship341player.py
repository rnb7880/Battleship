
from random import randint
from random import sample
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
# makes a board
def print_board(board):
    for row in board:
        print (" ".join(row))


# makes a random starting point for all ships
def random_row(board):
    return randint(1, len(board)-1)
def random_col(board):
    return randint(1, len(board)-1)


#makes the row higher
def change_up(dbllist,plc):
    dbllist.append([dbllist[plc][0]-1,dbllist[plc][1]])

#makes the row lower
def change_dwn(dbllist,plc):
    dbllist.append([dbllist[plc][0]+1,dbllist[plc][1]])

# makes column move left
def change_lt(dbllist,plc):
    dbllist.append([dbllist[plc][0],dbllist[plc][1]-1])

# makes column move right
def change_rt(dbllist,plc):
    dbllist.append([dbllist[plc][0],dbllist[plc][1]+1])


# this creates another set of coordinates that will make a ship in a line
# adds a coordinate to the ship
def add_coord(ship_coord,x):
    plc = randint(0,len(ship_coord)-1)
    if x == 0:  #change row
        if ship_coord[plc][0] <= 1 : #need to move down
            change_dwn(ship_coord,plc)
        elif ship_coord[plc][0] >= (len(board)-1 - len(ship_coord)): #need to move up
            change_up(ship_coord,plc)
        else: #can go up or down
            upordwn = randint(0,1)
            if upordwn == 1:
                change_dwn(ship_coord,plc)
            else:
                change_up(ship_coord,plc)
    else:   #change col
        if ship_coord[plc][1] <= 1: #need to move right
            change_rt(ship_coord,plc)
        elif ship_coord[plc][1] >= (len(board)-1 - len(ship_coord)): #need to move left
            change_lt(ship_coord,plc)
        else: #can go right or left
            rtorlt = randint(0,1)
            if rtorlt == 1:
                change_rt(ship_coord,plc)
            else:
                change_lt(ship_coord,plc)
    spots = len(ship_coord)-1
    for i in range(spots):
        if ship_coord[-1] == ship_coord[i]:
            del ship_coord[-1]
            add_coord(ship_coord,x)
    for ship in all_ships:
        for i in range(len(ship)):
            if i == ship_coord:
                del ship_coord[-1]
                add_coord(ship_coord,x)



#makes the ship based on input and length
def make_ship(ship,lgth):
    x = randint(0,2)
    for i in range(lgth-1):
        add_coord(ship,x)


# ends the game
def end_game(x):
    print ("Game Over")
    if x == 'win':
        print ("You Won! in %s turns!" %(turn))
    else:
        print ("You Lost! Try again next time.")
    quit()

def all_same(items):
    return all(x == items[0] for x in items)
# print board and perform actions to place ships
board = []


alpha = [' ','A','B','C','D','E','F','G','H','I','J']
numbers = ['1','2','3','4','5','6','7','8','9','10']
board.append(numbers)
for x in range(0,10):
    board.append(["O"]*10)
for i in range(0,11):
    board[i].insert(0,alpha[i])


# type_of_game = input("One player or Two player? (enter 1 or 2):")
# if type_of_game == "1" :
patrol     = [[random_row(board),random_col(board)]]
destroyer  = [[random_row(board),random_col(board)]]
submarine  = [[random_row(board),random_col(board)]]
battleship = [[random_row(board),random_col(board)]]
carrier    = [[random_row(board),random_col(board)]]


all_ships = [patrol,destroyer,submarine,battleship,carrier]
ship_names= ['Patrol Boat','Destroyer','Submarine','Battleship','Aircraft Carrier']

make_ship(patrol,2)
make_ship(destroyer,3)
make_ship(submarine,3)
make_ship(battleship,4)
make_ship(carrier,5)


answer_coords = []
for ships in all_ships:
    for coord in ships:
        answer_coords.append(coord)

#print answer_coords
#display for answers
"""
print "patrol is here: %s" %(patrol)
print "destroyer is here: %s" %(destroyer)
print "submarine is here: %s" %(submarine)
print "battleship is here: %s" %(battleship)
print "aircraft carrier is here: %s" %(carrier)
print

 #DISPLAY FOR ANSWERS
for boat in all_ships:
    for coords in boat:
        row = coords[0]
        col = coords[1]
        #print row
        #print col
        board[row][col] = "X"
        print_board(board)
"""


print_board(board)

print ("Let\'s Play Some Battleship!")
print ("Guess a row and column. You have 50 turns to sink all the ships!")
print ("Good Luck!")


# Write your code below!
hits = 0
turn = 0
for i in range(1,50):
    turn = i
    print ("Turn %s out of 50" %(turn))
    guess_row = (input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    guess_row = ord(guess_row) - 96
    guess = [guess_row,guess_col]
    spaces_sunk = board.count("X")
    if guess_row not in range(11) or guess_col not in range(11):
        print ("Oops, that\'s not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
        print ("You guessed that one already.")
    elif guess in (answer_coords):
        print ("Congratulations! You hit a ship!")
        board[guess_row][guess_col]= "X"
        for ships in all_ships:
            for coord in ships:
                name_place = all_ships.index(ships)
                # both = zip(ship_names,all_ships)
                name = ship_names[name_place]
                if guess == coord:
                    print ("You hit my %s !" %name)
                    coord_place = ships.index(coord)
                    del ships[coord_place]
                    if not ships:
                        print ("You destroyed my %s !" %name)
                        hits = hits + 1
                        if hits == 5:
                            end_game('win')
                            break
        #cls()
        print_board(board)
    else:
        print ("You missed my battleship!")
        board[guess_row][guess_col]= " "
        #cls()
        print_board(board)
        if turn == 50:
            end_game('loss')
            break
