from tkinter import *

def evolve(generation, rule254):
    last = len(generation) - 1
    size = len(generation[last])
    line = generation[last]
    linePlus = []
    for i in range(size):
        for k, v in rule254.items():
            if i+2 < size and ("[" + str(line[i]) + "," + str(line[i+1]) +  "," + str(line[i+2]) + "]" == k):
                linePlus.append(v)
                break
    print("LinePLus:", linePlus)
    generation.append(linePlus)
    return generation


def display(generation, w, marginTop):
    last = len(generation) - 1
    line = generation[last]
    print(line)
    marginRight = 0
    for l in line:
        if(l == 1):
            w.create_rectangle(marginRight, marginTop, 10, 10, fill="black")
        marginRight = marginRight + 10
    mainloop()

def main():
    generation = [[1,0,0,0,0,1,0,0,0,0,0,0]]
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

    master = Tk()
    w = Canvas(master, width=500, height=500)
    w.pack()
    marginTop = 0

    generation = evolve(generation, rule254)
    display(generation, w, marginTop)
    marginTop = marginTop + 10
    
    while True:
        generation, marginTop = master.after(1000, loop(generation, rule254, w, marginTop))

def loop(generation, rule254, w, marginTop):
    generation = evolve(generation, rule254)
    display(generation, w, marginTop)
    marginTop = marginTop + 10
    return generation, marginTop

main()