# Monopoly Simulator
# http://img.thesun.co.uk/aidemitlum/archive/01771/Monopoly2_1771742a.jpg

import sys
from random import randint

if len(sys.argv) != 2:
    print("\nType the number of times you want to simulate it in the command line.\n")    
    sys.exit(0)
    
num = int(sys.argv[1])

piece = 0
jail = 0
iteration = 0

brown1 = 0
brown2 = 0

light_blue1 = 0
light_blue2 = 0
light_blue3 = 0

pink1 = 0
pink2 = 0
pink3 = 0

orange1 = 0
orange2 = 0
orange3 = 0

red1 = 0
red2 = 0
red3 = 0

yellow1 = 0
yellow2 = 0
yellow3 = 0

green1 = 0
green2 = 0
green3 = 0

dark_blue1 = 0
dark_blue2 = 0

#num = input("How many rolls do you want to simulate? ")

for h in range(0, num):
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    roll = dice1 + dice2

    piece += roll
    
    if piece > 40:
        piece -= 40
        iteration += 1
        #print("Around the board %d times so far" %(iteration)) ### Optional
    
    #print(piece) ### Optional
        
    #Jail
    if piece == 30:
        piece = 10
        jail += 1
        #print("JAIL") ### Optional
    
    #Brown
    if piece == 1:
        brown1 += 1
    if piece == 3:
        brown2 += 1

    #Light Blue
    if piece == 6:
        light_blue1 += 1
    if piece == 8:
        light_blue2 += 1
    if piece == 9:
        light_blue3 += 1
        
    #Pink
    if piece == 11:
        pink1 += 1
    if piece == 13:
        pink2 += 1
    if piece == 14:
        pink3 += 1
    
    #Orange
    if piece == 16:
        orange1 += 1
    if piece == 18:
        orange2 += 1
    if piece == 19:
        orange3 += 1
    
    #Red
    if piece == 21:
        red1 += 1
    if piece == 23:
        red2 += 1
    if piece == 24:
        red3 += 1
    
    #Yellow
    if piece == 26:
        yellow1 += 1
    if piece == 27:
        yellow2 += 1
    if piece == 29:
        yellow3 += 1
    
    #Green
    if piece == 31:
        green1 += 1
    if piece == 32:
        green2 += 1
    if piece == 34:
        green3 += 1
    
    #Dark Blue
    if piece == 37:
        dark_blue1 += 1
    if piece == 39:
        dark_blue2 += 1
        
brown = brown1 + brown2
light_blue = light_blue1 + light_blue2 + light_blue3
pink = pink1 + pink2 + pink3
orange = orange1 + orange2 + orange3
red = red1 + red2 + red3
yellow = yellow1 + yellow2 + yellow3
green = green1 + green2 + green3
dark_blue = dark_blue1 + dark_blue2

#Prints all the Statistics

print("\n\n")
print("Brown = %d" %(brown))
print("Light Blue = %d" %(light_blue))
print("Pink = %d" %(pink))
print("Orange = %d" %(orange))
print("Red = %d" %(red))
print("Yellow = %d" %(yellow))
print("Green = %d" %(green))
print("Dark Blue = %d" %(dark_blue))
print("\n")

print("Brown 1 = %d" %(brown1))
print("Brown 2 = %d" %(brown2))
print("\n")
print("Light Blue 1 = %d" %(light_blue1))
print("Light Blue 2 = %d" %(light_blue2))
print("Light Blue 3 = %d" %(light_blue3))
print("\n")
print("Pink 1 = %d" %(pink1))
print("Pink 2 = %d" %(pink2))
print("Pink 3 = %d" %(pink3))
print("\n")
print("Orange 1 = %d" %(orange1))
print("Orange 2 = %d" %(orange2))
print("Orange 3 = %d" %(orange3))
print("\n")
print("Red 1 = %d" %(red1))
print("Red 2 = %d" %(red2))
print("Red 3 = %d" %(red3))
print("\n")
print("Yellow 1 = %d" %(yellow1))
print("Yellow 2 = %d" %(yellow2))
print("Yellow 3 = %d" %(yellow3))
print("\n")
print("Green 1 = %d" %(green1))
print("Green 2 = %d" %(green2))
print("Green 3 = %d" %(green3))
print("\n")
print("Dark Blue 1 = %d" %(dark_blue1))
print("Dark Blue 2 = %d" %(dark_blue2))
print("\n")
print("You've been jailed %d times" %(jail))



#The Board

#Calculating highest number of digits (for board formatting)

places = [brown1, brown2, light_blue1, light_blue2, light_blue3, pink1, pink2, pink3,
            orange1, orange2, orange3, red1, red2, red3, yellow1, yellow2, yellow3,
            green1, green2, green3, dark_blue1, dark_blue2]
         
digit = 0
temp = 0
         
for place in places:
    while place / 10 >= 1:
        place /= 10
        temp += 1
    temp += 1
    if temp > digit:
        digit = temp
    temp = 0

#Creating Blanks & Spaces

blank = "-"
space = " "

for i in range(0, digit - 1):
    blank += "-"
    space += " "

#Formatting all the places, so that they have "temp" digits

formatted = []

placelen = 0

for place in places:
    holder = place
    form = 0

    while holder / 10 >= 1:
        holder /= 10
        placelen += 1
    placelen += 1
    
    if placelen != digit:
        form = format(place, "0%d" %(digit))
    else:
        form = str(place)
    
    placelen = 0
    
    formatted.append(form)


brown1 = formatted[0]
brown2 = formatted[1]

light_blue1 = formatted[2]
light_blue2 = formatted[3]
light_blue3 = formatted[4]

pink1 = formatted[5]
pink2 = formatted[6]
pink3 = formatted[7]

orange1 = formatted[8]
orange2 = formatted[9]
orange3 = formatted[10]

red1 = formatted[11]
red2 = formatted[12]
red3 = formatted[13]

yellow1 = formatted[14]
yellow2 = formatted[15]
yellow3 = formatted[16]

green1 = formatted[17]
green2 = formatted[18]
green3 = formatted[19]

dark_blue1 = formatted[20]
dark_blue2 = formatted[21]

#Making the Board

board = [
        [blank, red1, blank, red2, red3, blank, yellow1, yellow2, blank, yellow3, blank],
        [orange1, space, space, space, space, space, space, space, space, space, green1],
        [orange2, space, space, space, space, space, space, space, space, space, green2],
        [blank, space, space, space, space, space, space, space, space, space, blank],
        [orange3, space, space, space, space, space, space, space, space, space, green3],
        [blank, space, space, space, space, space, space, space, space, space, blank],
        [pink3, space, space, space, space, space, space, space, space, space, blank],
        [pink2, space, space, space, space, space, space, space, space, space, dark_blue1],
        [blank, space, space, space, space, space, space, space, space, space, blank],
        [pink1, space, space, space, space, space, space, space, space, space, dark_blue2],
        [blank, light_blue1, light_blue2, blank, light_blue3, blank, blank, brown2, blank, brown1, "GO"]
        ]

#Drawing the Board

print("\n")

print("  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  " %(board[0][0], 
                                                                                    board[0][1],
                                                                                    board[0][2],
                                                                                    board[0][3],
                                                                                    board[0][4],
                                                                                    board[0][5],
                                                                                    board[0][6],
                                                                                    board[0][7],
                                                                                    board[0][8],
                                                                                    board[0][9],
                                                                                    board[0][10]
                                                                                    ))
print("  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  " %(board[1][0], 
                                                                                    board[1][1],
                                                                                    board[1][2],
                                                                                    board[1][3],
                                                                                    board[1][4],
                                                                                    board[1][5],
                                                                                    board[1][6],
                                                                                    board[1][7],
                                                                                    board[1][8],
                                                                                    board[1][9],
                                                                                    board[1][10]
                                                                                    ))
print("  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  " %(board[2][0], 
                                                                                    board[2][1],
                                                                                    board[2][2],
                                                                                    board[2][3],
                                                                                    board[2][4],
                                                                                    board[2][5],
                                                                                    board[2][6],
                                                                                    board[2][7],
                                                                                    board[2][8],
                                                                                    board[2][9],
                                                                                    board[2][10]
                                                                                    ))
print("  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  " %(board[3][0], 
                                                                                    board[3][1],
                                                                                    board[3][2],
                                                                                    board[3][3],
                                                                                    board[3][4],
                                                                                    board[3][5],
                                                                                    board[3][6],
                                                                                    board[3][7],
                                                                                    board[3][8],
                                                                                    board[3][9],
                                                                                    board[3][10]
                                                                                    ))
print("  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  " %(board[4][0], 
                                                                                    board[4][1],
                                                                                    board[4][2],
                                                                                    board[4][3],
                                                                                    board[4][4],
                                                                                    board[4][5],
                                                                                    board[4][6],
                                                                                    board[4][7],
                                                                                    board[4][8],
                                                                                    board[4][9],
                                                                                    board[4][10]
                                                                                    ))
print("  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  " %(board[5][0], 
                                                                                    board[5][1],
                                                                                    board[5][2],
                                                                                    board[5][3],
                                                                                    board[5][4],
                                                                                    board[5][5],
                                                                                    board[5][6],
                                                                                    board[5][7],
                                                                                    board[5][8],
                                                                                    board[5][9],
                                                                                    board[5][10]
                                                                                    ))
print("  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  " %(board[6][0], 
                                                                                    board[6][1],
                                                                                    board[6][2],
                                                                                    board[6][3],
                                                                                    board[6][4],
                                                                                    board[6][5],
                                                                                    board[6][6],
                                                                                    board[6][7],
                                                                                    board[6][8],
                                                                                    board[6][9],
                                                                                    board[6][10]
                                                                                    ))
print("  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  " %(board[7][0], 
                                                                                    board[7][1],
                                                                                    board[7][2],
                                                                                    board[7][3],
                                                                                    board[7][4],
                                                                                    board[7][5],
                                                                                    board[7][6],
                                                                                    board[7][7],
                                                                                    board[7][8],
                                                                                    board[7][9],
                                                                                    board[7][10]
                                                                                    ))
print("  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  " %(board[8][0], 
                                                                                    board[8][1],
                                                                                    board[8][2],
                                                                                    board[8][3],
                                                                                    board[8][4],
                                                                                    board[8][5],
                                                                                    board[8][6],
                                                                                    board[8][7],
                                                                                    board[8][8],
                                                                                    board[8][9],
                                                                                    board[8][10]
                                                                                    ))
print("  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  " %(board[9][0], 
                                                                                    board[9][1],
                                                                                    board[9][2],
                                                                                    board[9][3],
                                                                                    board[9][4],
                                                                                    board[9][5],
                                                                                    board[9][6],
                                                                                    board[9][7],
                                                                                    board[9][8],
                                                                                    board[9][9],
                                                                                    board[9][10]
                                                                                    ))
print("  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  " %(board[10][0], 
                                                                                    board[10][1],
                                                                                    board[10][2],
                                                                                    board[10][3],
                                                                                    board[10][4],
                                                                                    board[10][5],
                                                                                    board[10][6],
                                                                                    board[10][7],
                                                                                    board[10][8],
                                                                                    board[10][9],
                                                                                    board[10][10]
                                                                                    ))