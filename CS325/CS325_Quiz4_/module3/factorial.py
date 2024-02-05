def calculateFactorial(n):
    if n == 0:
        return 1
    else:
        return n * calculateFactorial(n-1)