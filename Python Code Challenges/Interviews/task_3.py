import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # print(arr)
    res = []
    for line1 in range(4):
        for line2 in range(4):
            s = sum(arr[line1][line2:line2 + 3]) + arr[line1 + 1][line2 + 1] + sum(arr[line1 + 2][line2:line2 + 3])
            res.append(s)

    print(max(res))
