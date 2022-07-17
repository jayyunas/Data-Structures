import math
import binarylog

def iterativeLogStar(n, b):

    count = 0
    while n >= 1:
        n = binarylog._log(n, b)
        count += 1

    return count

if __name__ == '__main__':
    n = 1000
    base = 5
    print("Log* (", n, ") = ", iterativeLogStar(n, base)) 