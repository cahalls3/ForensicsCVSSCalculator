import string
from urllib import response
import math

# Calculating the score this one has the formula
def scoreCalc():
    exploitabilityCoefficient = 8.22
    scopeCoefficient = 1.08

    # Define associative arrays mapping each metric value to the constant used in the CVSS scoring formula.
    weight = {
        "attackVector" : [ 0.2, 0.55, 0.62, 0.85 ],
        "attackComplexity" : [ 0.44, 0.52, 0.77 ],
        "privilegesRequiredUnChanged" : [ 0.27, 0.62, 0.85 ],
        "privilegesRequiredChanged" : [ 0.5, 0.68, 0.85 ],
        "userInteraction" : [ 0.62, 0.85 ],
        "scope" : [ 6.42, 7.52 ],
        "confidentialityImpact" : [ 0, 0.22, 0.56 ],
        "integrityImpact" : [ 0, 0.22, 0.56 ],
        "availabilityImpact" : [ 0, 0.22, 0.56 ]
        # C, I, A, have same weights
    }

    tempScopeType = ""
    if sScope == 1:
        tempScopeType = "privilegesRequiredUnChanged"
    elif sScope == 2:
        tempScopeType = "privilegesRequiredChanged"

    baseScore = 0
    impactScore = 0
    exploitabilityScore = (exploitabilityCoefficient * weight["attackVector"][sAttackVector - 1] * weight[tempScopeType][sPrivilegesRequired - 1] * weight["attackComplexity"][sAttackComplexity - 1] * weight["userInteraction"][sUserInteraction - 1])
    impactScoreMultiplier = (1 - ((1 - weight["confidentialityImpact"][sConfidentialityImpact - 1]) * (1 - weight["integrityImpact"][sIntegrityImpact - 1]) * (1 - weight["availabilityImpact"][sAvailabilityImpact - 1])))  
    if tempScopeType == "privilegesRequiredUnChanged":
        impactScore = (weight["scope"][sScope - 1] * impactScoreMultiplier)
    elif tempScopeType == "privilegesRequiredChanged":
        impactScore = (weight["scope"][sScope - 1] * (impactScoreMultiplier - 0.029) - 3.25 * math.pow((impactScoreMultiplier - 0.02), 15))
    
    if impactScore <= 0:
        baseScore = 0
    else:
        if sScope == 1:
            baseScore = min((exploitabilityScore + impactScore), 10)
        elif sScope == 2:
            baseScore = min(((exploitabilityScore + impactScore) * scopeCoefficient), 10)

    baseScore = (math.ceil(baseScore * 10) / 10)
    return baseScore


# Function to receive user intput
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
    elif val >= 0.1 and val <= 3.9:
        returnString = "LOW"
    elif val >= 4 and val <= 6.9:
        returnString = "MEDIUM"
    elif val >= 7 and val <= 8.9:
        returnString = "HIGH"
    elif val >= 9:
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
print("1 : High")
print("2 : Low")
print("3 : None")

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

score = scoreCalc()
print(calculateRating(score) + " " + str(score))