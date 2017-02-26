"""
Pairs of guards will bet bananas and thumb wrestle. The one with fewer bananas
will bet all of theirs, and the one with more matches the bet. The one with
more bananas always loses. Guards will enter an infinite loop if their banana
counts are never equal. Certain pairings will result in an infinite loop.

Write a function answer(banana_list) which, given a list of positive integers
representing the amount of bananas each guard starts with, returns the fewest
possible number of guards that will be left to watch the prisoners.
"""

import itertools

def infloop(a, b):
    #determines if guards with a and b bananas will enter an infinite loop

    #optimizations
    if (a == b):
        return False
    if (a + b) % 2 == 1:
        return True
    if (a + b) & (a + b - 1) == 0:
        return False

    #all other cases:
    mem = []
    while (a != b):
        if (a > b):
            a, b = b, a
        if (a, b) in mem: #guards have entered infinite loop
            return True
        else:
            mem.append((a, b))
            b -= a
            a += a
    return False

def answer(banana_list):
    total = 0
    if len(banana_list) % 2 == 1:
        banana_list = remove_worst(banana_list)
        total += 1
    combs = combo_iter(banana_list)
    total += leftover(list(min(combs, key = lambda c: leftover(list(c)))))
    return total

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

def leftover(banana_list):
    #get number of guards remaining with the specified ordering of the list
    #pairs will be consecutive numbers
    banana_list = [k for i in banana_list for k in i] #flatten input
    cnt = 0
    while len(banana_list) > 1:
        a = banana_list.pop()
        b = banana_list.pop()
        if not infloop(a, b):
            cnt += 2
    cnt += len(banana_list)
    return cnt

def combo_iter(banana_list):
    #gets all unique combinations of guards with the supplied list
    if len(banana_list) < 2:
        yield banana_list
        return
    a = banana_list[0]
    for i in range(1,len(banana_list)):
        pair = (a, banana_list[i])
        for rest in combo_iter(banana_list[1:i] + banana_list[i + 1:]):
            yield [pair] + rest
