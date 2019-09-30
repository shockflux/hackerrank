#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    plus_count = 0
    minus_count = 0
    zero_count = 0
    for i in range(len(arr)):
        if (arr[i] < 0):
            minus_count += 1
        if (arr[i] > 0):
            plus_count += 1
        elif (arr[i] == 0):
            zero_count += 1
    print(plus_count / len(arr))
    print(minus_count / len(arr))
    print(zero_count / len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)