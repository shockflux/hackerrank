#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applec = 0
    orangec = 0
    for i in range(len(apples)):
        apples[i] = apples[i] + a
    for j in range(len(apples)):
        if (apples[j] >= s and apples[j] <= t):
            applec += 1
    print(applec)
    for i in range(len(oranges)):
        oranges[i] += b
    for j in range(len(oranges)):
        if (oranges[j] >= s and oranges[j] <= t):
            orangec += 1
    print(orangec)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
