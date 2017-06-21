def findSqrt(N, guessFactor, flag):
    squareRoot = (N/guessFactor)
    average = ((squareRoot+guessFactor)/2)

    if flag == True:
        findSqrt(N, average, False)
    else:
        print(average)

findSqrt(500, 20, True)

