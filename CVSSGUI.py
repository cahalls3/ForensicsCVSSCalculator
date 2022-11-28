import PySimpleGUI as sg



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

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif values["AttackVec"] == True:
        print("Hello World")
    elif event == "Calculate":
        sg.Popup("The CVSS Score is: 69420")
    
window.close()