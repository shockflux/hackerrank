#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here

    left = ([arr[i][i] for i in range(len(arr))])
    right = ([arr[i][len(arr) - i - 1] for i in range(len(arr))])
    print(left)
    print(right)
    sum = 0
    sum1 = 0
    diff = 0
    for i in range(len(left)):
        sum = sum + left[i]
    for i in range(len(right)):
        sum1 = sum1 + right[i]
    if (sum > sum1):
        diff = sum - sum1
        return diff
    elif (sum < sum1):
        diff = sum1 - sum
        return diff
    else:
        diff = sum - sum1
        return diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()