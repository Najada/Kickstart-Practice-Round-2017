#!/usr/bin/python3

N = int(input())

def count_char(elemnt):
    i = 0
    count = 0
    while i < len(elemnt):
        j = 0
        if (elemnt[i] != ' '):
            count += 1
        while j < len(elemnt):
            if (elemnt[j] == elemnt[i] and i != j):
                elemnt[j] = ' '
            j += 1
        i += 1
    return count

def find_the_leader(array, index):
    max = 0
    value = array[0]

    for i in range(0, len(array)):
        element = list(array[i])
        result = count_char(element)
        if (max < result):
            max = result
            value = array[i]
        elif (max == result ):
            if (value > array[i]):
                value = array[i]
    print("Case #{}: {}".format(index, value))

for i in range(0, N):
    nb= int(input())
    array = []
    for a in range(0, nb):
        s = input()
        array.append(s)
    find_the_leader(array, int(i + 1))
