import PySimpleGUI as sg
import CVSSCalculatorAll


layout = [
          [[sg.T("Attack Vector:")],
          sg.T("         "), sg.Radio('Network', "RADIO1", default=False, key="AttackVecNet"),
          sg.T("     "), sg.Radio('Adjacent Network', "RADIO1", default=False, key="AttackVecAdj"),
          sg.T("         "), sg.Radio('Local', "RADIO1", default=False, key="AttackVecLocal"),
          sg.T("         "), sg.Radio('Physical', "RADIO1", default=True, key="AttackVecPhys")],

          [[sg.T("Attack Complexity:")],
          sg.T("         "), sg.Radio('Low', "RADIO2", default=False, key="AttackComplexL"),
          sg.T("           "), sg.Radio('Medium', "RADIO2", default=False,key="AttackComplexM"),
          sg.T("    "), sg.Radio('High', "RADIO2", default=True,key="AttackComplexH")],

          [[sg.T("Privileges Required:")],
          sg.T("         "), sg.Radio('None', "RADIO3", default=False, key="PrivReqsN"),
          sg.T("         "), sg.Radio('Low', "RADIO3", default=False, key="PrivReqsL"),
          sg.T("         "), sg.Radio('High', "RADIO3", default=True, key="PrivReqsH")],

          [[sg.T("User Interaction:")],
          sg.T("         "), sg.Radio('None', "RADIO4", default=False, key="UIReqN"),
          sg.T("         "), sg.Radio('Required', "RADIO4", default=True,key="UIReq")],

          [[sg.T("Scope:")],
          sg.T("         "), sg.Radio('Changed', "RADIO5", default=False, key="ScopeChange"),
          sg.T("    "), sg.Radio('Unchanged', "RADIO5", default=True, key="ScopeNChange")],

          [[sg.T("Confidentiality Impact:")],
          sg.T("         "), sg.Radio('None', "RADIO6", default=True, key="ConImpN"),
          sg.T("         "), sg.Radio('Low', "RADIO6", default=False, key="ConImpL"),
          sg.T("         "), sg.Radio('High', "RADIO6", default=False, key="ConImpH")],

          [[sg.T("Integrity Impact:")],
          sg.T("         "), sg.Radio('None', "RADIO7", default=True, key="IntImpN"),
          sg.T("         "), sg.Radio('Low', "RADIO7", default=False, key="IntImpL"),
          sg.T("         "), sg.Radio('High', "RADIO7", default=False, key="IntImpH")],

          [[sg.T("Availability Impact:")],
          sg.T("         "), sg.Radio('None', "RADIO8", default=True, key="AvailImpN"),
          sg.T("         "), sg.Radio('Low', "RADIO8", default=False, key="AvailImpL"),
          sg.T("         "), sg.Radio('High', "RADIO8", default=False, key="AvailImpH")],

          [sg.T("")],[sg.T("        "), sg.Button('Calculate',size=(20,4))], [sg.T("")]

          ]


###Setting Window
window = sg.Window('Push my Buttons', layout, size=(700,600))

###Showing the Application, also GUI functions can be placed here.

# attackVector = 0
# attackComplexity = 0
# priviledges = 0
# userInteraction = 0
# scope = 0
# confidentiality = 0
# integrity = 0
# availability = 0

### Class Object
class RadioValues():
    # Populating values in the class
    def __init__(self, attackVector, attackComplexity, priviledges, userInteraction, scope, confidentiality, integrity, availability):
        self.attackVector = attackVector
        self.attackComplexity = attackComplexity
        self.priviledges = priviledges
        self.userInteraction = userInteraction
        self.scope = scope
        self.confidentiality = confidentiality
        self.integrity = integrity
        self.availability = availability

while True:
    event, values = window.read()
    # if event == sg.WIN_CLOSED or event=="Exit":
    #     break
    # elif event == "Calculate":
    #     radioValues = RadioValues(attackVector, attackComplexity, priviledges, userInteraction, scope, confidentiality, integrity, availability)
    #     cvssScore = CVSSCalculatorAll.Calculate(radioValues)
    #     sg.Popup("The CVSS Score is: " + cvssScore)

    if values["AttackVecNet"] == True:
        attackVector = 4
    elif values["AttackVecAdj"] == True:
        attackVector = 3
    elif values["AttackVecLocal"] == True:
        attackVector = 2
    elif values["AttackVecPhys"] == True:
        attackVector = 1

    if values["AttackComplexL"] == True:
        attackComplexity = 3
    elif values["AttackComplexM"] == True:
        attackComplexity = 2
    elif values["AttackComplexH"] == True:
        attackComplexity = 1

    if values["PrivReqsN"] == True:
        priviledges = 3
    elif values["PrivReqsL"] == True:
        priviledges = 2
    elif values["PrivReqsH"] == True:
        priviledges = 1

    if values["UIReqN"] == True:
        userInteraction = 2
    elif values["UIReq"] == True:
        userInteraction = 1

    if values["ScopeChange"] == True:
        scope = 2
    elif values["ScopeNChange"] == True:
        scope = 1

    if values["ConImpN"] == True:
        confidentiality = 1
    elif values["ConImpL"] == True:
        confidentiality = 2
    elif values["ConImpH"] == True:
        confidentiality = 3

    if values["IntImpN"] == True:
        integrity = 1
    elif values["IntImpL"] == True:
        integrity = 2
    elif values["IntImpH"] == True:
        integrity = 3

    if values["AvailImpN"] == True:
        availability = 1
    elif values["AvailImpL"] == True:
        availability = 2
    elif values["AvailImpH"] == True:
        availability = 3

    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Calculate":
        radioValues = RadioValues(attackVector, attackComplexity, priviledges, userInteraction, scope, confidentiality, integrity, availability)
        cvssScore = CVSSCalculatorAll.Calculate(radioValues)
        sg.Popup("The CVSS Score is: " + cvssScore)


window.close()