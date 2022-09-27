
import math


def convertUI2MathScore(val):
    mathScore = -1

    if val == 1:
        mathScore = 3.33
    elif val == 2:
        mathScore = 6.66
    elif val == 3:
        mathScore = 9.99
    else: 
        return 0

    return mathScore

def binaryResponse2MathScore(val):
    mathScore = -1

    if val == 1:
        mathScore = 0
    elif val == 2:
        mathScore = 10
    else:
        mathScore = 0
    
    return mathScore