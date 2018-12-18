#!/usr/bin/python3

nb = int(input())

for a in range(0, nb):
    N, M = [int(i) for i in input().split()]
    print("Case #%d: %.9f" % (int(a + 1), ((N - M) / (N + M))))