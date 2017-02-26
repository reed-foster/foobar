import math
from fractions import gcd

def infloop(a, b):
    if a == b:
        return False
    sumratio = (a + b) / gcd(a, b)
    if ((sumratio) & (sumratio - 1)) == 0 and sumratio > 1:
        return False
    return True


def answer(banana_list):
    if len(banana_list) == 1:
        return 1
    if len(banana_list) == 2:
        if infloop(banana_list[0], banana_list[1]):
            return 0
        else:
            return 2
    else:
        min_guards = 0
        
        if len(banana_list) % 2 == 1:
            banana_list = remove_worst(banana_list)
            min_guards += 1
        
        opt_table = []
        for i in range(0, len(banana_list)):
            row = []
            for j in range(0, len(banana_list)):
                if i == j:
                    row.append(0)
                else:
                    row.append(1 if infloop(banana_list[i], banana_list[j]) else 0)
            opt_table.append(row)                   
        min_guards += getpairs(opt_table)
        return min_guards


def getpairs(opt_table):
    print opt_table
    dim = len(opt_table)
    if dim == 0:
        return 0
    else:
        for i in range(0, dim):
            for j in range(0, dim):
                if (opt_table[i][j] == 1):
                    if i > j:
                        return getpairs(remove(remove(opt_table, i), j))
                    else:
                        return getpairs(remove(remove(opt_table, j), i))
        return dim

def remove(table, x):
    #removes the xth column and row of the 2d array table
    for i in range(len(table)):
        del table[i][x]
    del table[x]
    return table

def remove_worst(banana_list):
    idx_worst = 0
    numpartners_worst = len(banana_list)
    for i in range(0, len(banana_list)):
        partners = 0
        for j in range(0, len(banana_list)):
            if (j != i):
                partners += 1 if infloop(banana_list[i], banana_list[j]) else 0
        if partners < numpartners_worst:
            idx_worst = i
            numpartners_worst = partners
        if numpartners_worst == 0:
            break
    del banana_list[idx_worst]
    return banana_list

def gentests(n, infsymbol, notinfsymbol):
    data = ""
    for i in range(1, n + 1):
        data += "0" * (int(math.log(n, 10)) - int(math.log(i, 10))) + str(i) + ":"
        for j in range(1, i / 2 + 1):
            data += infsymbol if infloop(j, i - j) else notinfsymbol
        data += "\n"
    print data
    data =""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            data += infsymbol if infloop(i, j) else notinfsymbol
        data += "\n"
    print data

from Tkinter import *

root = Tk()
c = Canvas(root, width = 1000, height = 1000)

scale = 1
size = 1000
for i in range(0, size):
    for j in range(0, size):
        if not infloop(i, j):
            line = c.create_rectangle(scale*j,scale*i,scale*j+scale,scale*i+scale, fill="black")
c.pack()
root.mainloop()
