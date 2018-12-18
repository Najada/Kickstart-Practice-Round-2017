#!/usr/bin/python3

import math

nb = int(input())

def solve(N, index):
    res = ((N + 1) * N )/ 2
    print('Case #%d: %d' % (index, res))

for i in range(0, nb):
    N, M = [ int(i) for i in input().split() ]
    solve(min(N,M), int(i + 1))