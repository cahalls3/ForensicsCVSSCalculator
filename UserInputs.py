import string
from urllib import response

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