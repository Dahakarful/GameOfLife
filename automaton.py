import sys, getopt
import random
from tkinter import *
from rules import getRule

master = Tk()
w = None
sizeSquare = None
generation = None
listGeneration = []
line = 1
y1 = 0
y2 = 0
x1 = 0
x2 = 0
listOfRules = None

# Main programm
def gameOfLife(width, height, rule, size):
    global sizeSquare
    global y2
    global generation
    global listGeneration
    global w
    global listOfRules

    sizeSquare = size
    y2 = sizeSquare
    generation = [0] * width
    generation[int(width/2)] = 1
    listGeneration.append(generation)
    listOfRules = getRule(rule)
    
    w = Canvas(master, width=width, height=height)
    # generateRandomLine(width, height)
    while True:
        if line == height:
            break
        elif line == 1:
            drawSquare()
            w.pack()
            master.update_idletasks()
            master.update()
        else:
            master.after(100, evolve())
            w.pack()
            master.update_idletasks()
            master.update()
    master.mainloop()

# Evolution of generation
def evolve():
    global generation
    size = len(generation)
    linePlus = []
    for i in range(size):
        for k, v in listOfRules.items():
            if i+2 < size and ("[" + str(generation[i]) + "," + str(generation[i+1]) +  "," + str(generation[i+2]) + "]" == k):
                linePlus.append(v)
                break
    linePlus.insert(0,0)
    linePlus.append(0)
    print("LinePLus:", linePlus)
    global listGeneration
    listGeneration.append(linePlus)
    generation = linePlus
    drawSquare()

# Generate random table
def generateRandomLine(width, height):
    x1 = random.randrange(width)
    y1 = 0
    x2 = x1 + random.randrange(width)
    y2 = 2
    w.create_rectangle(x1, y1, x2, y2, fill="blue", outline='black')

# Draw squares with the given generation
def drawSquare():
    global w
    global generation
    global line
    global y1
    global y2
    global x1
    global x2
    i = 0
    for index in range(len(generation)):
        if generation[index] == 1:
            if i == 0:
                x1 = index
                x2 = index + sizeSquare
                w.create_rectangle(x1, y1, x2, y2, fill="black")
                i = i + 1
            else:
                x1 = index + 1
                x2 = index + 1
            # elif i == 0:
            #     if sizeSquare == 1:
            #         x1 = index - sizeSquare
            #         x2 = index + sizeSquare
            #     else:
            #         x1 = x1 - sizeSquare
            #         x2 = x2 - sizeSquare
            #     i = i + 1
            #     w.create_rectangle(x1, y1, x2, y2, fill="black")
            # else:
            #     x1 = x1 + sizeSquare
            #     x2 = x2 + sizeSquare
            #     w.create_rectangle(x1, y1, x2, y2, fill="black")
            
            w.create_rectangle(x1, y1, x2, y2, fill="black")
    y1 = y1 + sizeSquare
    y2 = y2 + sizeSquare
    line = line + 1

# Launch arguments
def main(argv):
    width = ''
    height = ''
    rule = ''
    size = ''
    try:
        opts, args = getopt.getopt(argv,"Hw:h:r:",["width=","height=","rule="])
        #s:      ,"size="])
    except getopt.GetoptError:
        print('Bad parameters ! Run command with -H option for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-H':
            print('Choose the width and the height of the table with -w and -h\n')
            print('And choose the rule to generate with -r\n')
            print('The final command should be: gameOfLife.py -w <width> -h <height> -r <number rule>\n')
            sys.exit()
        elif opt in ("-w", "--width"):
            try:
                width = int(arg)
            except ValueError:
                print('-w: Option width need to be an int')
                return
        elif opt in ("-h", "--height"):
            try:
                height = int(arg)
            except ValueError:
                print('-w: Option height need to be an int')
                return
        elif opt in ("-r", "--rule"):
            try:
                rule = int(arg)
            except ValueError:
                print('-w: Option rule need to be an int')
                return
        # elif opt in ("-s", "--size"):
        #     try:
        #         size = int(arg)
        #     except ValueError:
        #         print('-s: Option size need to be an int')
        #         return
    if width != '' and height != '' and rule != '':
        #and size != '':
        gameOfLife(width, height, rule, 1)
    else:
        print('Run command with -H option for help')

if __name__ == "__main__":
    main(sys.argv[1:])