from tkinter import *

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
generation = [[1,0,0,0,1,0,0,0,0,0,0,0]]

def evolve():
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

master = Tk()
w = Canvas(master, width=500, height=500)
w.pack()

w.create_rectangle(250,0,258,10, fill="black")

last = len(generation) - 1
line = generation[last]
print(line)
marginTop = 0
marginRight = 0
# for l in line:
#     if(l == 1):
#         w.create_rectangle(marginRight, marginTop, 10, 10, fill="black")
#     else:
#         w.create_rectangle(marginRight, marginTop, 10, 10, fill="white")
#     marginRight = marginRight + 10
mainloop()