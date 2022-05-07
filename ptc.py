import math
import os
import random
import re
import sys

# Complete the 'permutationEquation' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.

def permutationEquation(p):
    # Write your code here
    re = []
    for i in range(1, len(p)+1):
        for j in range(len(p)):
            if(p[p[j]-1] == i):
                re.append(str(j+1))
    return re

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    result = permutationEquation(p)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()