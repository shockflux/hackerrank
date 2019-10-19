#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highest=scores[0]
    small=scores[0]
    highcount=0
    lowcount=0
    for i in range(len(scores)):
        if(scores[i]>highest):
            highest=scores[i]
            highcount+=1
        if(scores[i]<small):
            small=scores[i]
            lowcount+=1
    return[highcount,lowcount]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
