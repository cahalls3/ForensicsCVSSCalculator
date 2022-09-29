import string
from urllib import response
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

def scoreCalc():
    exploitabilityCoefficient = 8.22
    scopeCoefficient = 1.08

    # Define associative arrays mapping each metric value to the constant used in the CVSS scoring formula.
    weight = {
        "attackVector" : [ 0.2, 0.55, 0.62, 0.85 ],
        "attackComplexity" : [ 0.44, 0.52, 0.77 ],
        "privilegesRequiredUnChanged" : [ 0.85, 0.62, 0.27 ],
        "privilegesRequiredChanged" : [ 0.85, 0.68, 0.5 ],
        "userInteraction" : [ 0.85, 0.62 ],
        "scope" : [ 6.42, 7.52 ],
        "confidentialityImpact" : [ 0, 0.22, 0.56 ],
        "integrityImpact" : [ 0, 0.22, 0.56 ],
        "availabilityImpact" : [ 0, 0.22, 0.56 ]
        # C, I, A, have same weights
    }

def getUserInput(low,high):
    response = int(input("Enter value below: \n"))
    print("\n")
    while response < low or response > high:
        if response < low:
            print("Invalid value. Enter a number listed:")
            response = int(input("Enter value below: \n"))
            print("\n")
        elif response > high:
            print("Invalid value. Enter a number listed:")
            response = int(input("Enter value below: \n"))
            print("\n")

    return int(response)


def calculateRating(val):
    returnString = ""

    if val == 0:
        returnString = "NONE"
    elif val > 0.1 and val < 3.9:
        returnString = "LOW"
    elif val > 4 and val < 6.9:
        returnString = "MEDIUM"
    elif val > 7 and val < 8.9:
        returnString = "HIGH"
    elif val > 9:
        returnString = "CRITICAL"
    else: 
        return "SEG FAULT"

    return returnString


# Get Attack Vector user input variable
print("Enter a number for Attack Vector:") 
print("1 : Physical")
print("2 : Local")
print("3 : Adjacent Network")
print("4 : Network")

sAttackVector = getUserInput(1,4)

# Get Attack Complexity user input variable
print("Enter a number for Attack Complexity:") 
print("1 : High")
print("2 : Medium")
print("3 : Low")

sAttackComplexity = getUserInput(1,3)

# Get Privileges Required user input variable
print("Enter a number for Privileges Required:") 
print("1 : None")
print("2 : Low")
print("3 : High")

sPrivilegesRequired = getUserInput(1,3)

# Get User Interaction user input variable
print("Enter a number for User Interaction:") 
print("1 : Required")
print("2 : None")

sUserInteraction = getUserInput(1,2)

# Get Scope user input variable
print("Enter a number for Scope:") 
print("1 : Unchanged")
print("2 : Changed")

sScope = getUserInput(1,2)

# Get Confidentiality Impact user input variable
print("Enter a number for Confidentiality Impact:") 
print("1 : None")
print("2 : Low")
print("3 : High")

sConfidentialityImpact = getUserInput(1,3)

# Get Integrity Impact user input variable
print("Enter a number for Integrity Impact:") 
print("1 : None")
print("2 : Low")
print("3 : High")

sIntegrityImpact = getUserInput(1,3)

# Get Availability Impact user input variable
print("Enter a number for Availability Impact:") 
print("1 : None")
print("2 : Low")
print("3 : High")

sAvailabilityImpact = getUserInput(1,3)
