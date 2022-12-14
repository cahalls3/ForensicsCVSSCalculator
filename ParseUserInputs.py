
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


#THE COMMENTS BELOW ARE THE EQUATIONS THAT THE WEBSITE USES TO CALCULATE RISK.

# The Base Score is a function of the Impact and Exploitability sub score equations. Where the Base score is defined as,

# If (Impact sub score <= 0)     0 else,
# Scope Unchanged4                 πππ’πππ’π(ππππππ’π[(πΌπππππ‘ + πΈπ₯πππππ‘ππππππ‘π¦), 10])
# Scope Changed                      πππ’πππ’π(ππππππ’π[1.08 Γ (πΌπππππ‘ + πΈπ₯πππππ‘ππππππ‘π¦), 10])

# and the Impact sub score (ISC) is defined as,

# Scope Unchanged 6.42 Γ πΌππΆBase
# Scope Changed 7.52 Γ [πΌππΆπ΅ππ π β 0.029] β 3.25 Γ [πΌππΆπ΅ππ π β 0.02]15

# Where,

# πΌππΆπ΅ππ π = 1 β [(1 β πΌπππππ‘πΆπππ) Γ (1 β πΌπππππ‘πΌππ‘ππ) Γ (1 β πΌπππππ‘π΄π£πππ)]

# And the Exploitability sub score is,

# 8.22 Γ π΄π‘π‘πππππππ‘ππ Γ π΄π‘π‘ππππΆππππππ₯ππ‘π¦ Γ ππππ£πππππππππ’ππππ Γ ππ πππΌππ‘πππππ‘πππ

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