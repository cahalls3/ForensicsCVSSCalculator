
import math


def convertUI2MathScore(val):
    mathScore = -1

    if val == 1:
        mathScore = 3
    elif val == 2:
        mathScore = 6
    elif val == 3:
        mathScore = 9
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
        mathScore = 5
    
    return mathScore