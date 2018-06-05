import sys, getopt
import random
from tkinter import *

master = Tk()
w = None
sizeSquare = 2
generation = [0] * 800
rule254 = {
        "[1,1,1]" : 1, 
        "[1,1,0]" : 1, 
        "[1,0,1]" : 1, 
        "[1,0,0]" : 1,
        "[0,1,1]" : 1,
        "[0,1,0]" : 1,
        "[0,0,1]" : 1,
        "[0,0,0]" : 0
}

def evolve():
    size = len(generation)
    linePlus = []
    for i in range(size):
        for k, v in rule254.items():
            if i+2 < size and ("[" + str(line[i]) + "," + str(line[i+1]) +  "," + str(line[i+2]) + "]" == k):
                linePlus.append(v)
                break
    print("LinePLus:", linePlus)
    generation.append(linePlus)
    return generation

def gameOfLife(width, height, rule):
    global w
    w = Canvas(master, width=width, height=height)
    w.grid()
    # generateRandomLine(width, height)
    w.pack()
    mainloop()

def generateRandomLine(width, height):
    x1 = random.randrange(width)
    y1 = 0
    x2 = x1 + random.randrange(width)
    y2 = 2
    w.create_rectangle(x1, y1, x2, y2, fill="blue", outline='black')

def main(argv):
    width = ''
    height = ''
    rule = ''
    try:
        opts, args = getopt.getopt(argv,"Hw:h:r:",["width=","height=","rule="])
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
    if width != '' and height != '' and rule != '':
        gameOfLife(width, height, rule)
    else:
        print('Run command with -H option for help')

if __name__ == "__main__":
    main(sys.argv[1:])