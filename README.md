# ForensicsCVSSCalculator

## November Creation for Digital Forensics

### Created by Carson Halls, Roman Vish, Jade Ashford, John Keenan, Tyler Abbott, Conor Kikel, Chandler Evans

The intent of this program is to provide an offline Python solution to a CVSS (Common Vulnerability Scoring System) calculator.

A CVSS Calculator is a way to take a variety of parameters and variables regarding a cyber attack, and rate how damaging of an attack it would be, for example, a highly complex attack with escalated privileges needed will be rated lower than a simple attack that requires no escalated privileges.

In order to run this program the user should do the following:

1. Download code
2. Run the file "CVSSGUI.py"
3. Input values as prompted

<br />
<br />

### Severity Score Ranges

| Rating | Score Range |
| ----------- | ----------- |
| None | 0 |
| Low | 0.1 - 3.9 |
| Medium | 4 - 6.9 |
| High | 7 - 8.9 |
| Critical | 9 + |

<br />
<br />

### Option Explanation

There are several different options available on the GUI:

1. Attack Vector: The Attack Vector is indicative of where the attack is coming from on the network in question. It is a metaphorical layout of the land (network).
2. Attack Complexity: The Attack Complexity can be, in a way, compared to the amount of effort being put into the attack. The amount of attack vectors as well as variety has a direct impact on complexity. However, it has most come to mean how repeatable this particular attack may be.
3. Privileges Required: This is self-explanatory. What privileges on the device does the attack require? Does it require guest, user, or administrative access?
4. User Interaction: Does the attack require consistent iteraction from end-users to correctly carry out its objective?
5. Scope: How much of your network does the attack affect? Is it limited to just one device or does it span several?
6. Confidentiality Impact: What level of confidentiality does the attack have access to? Can it access Top Secret information?
7. Integrity Impact: Does the attack affect the veracity of the information accessed? Has any data change? What is the extent to which the data has been altered?
8. Availability Impact: To what extent has the attack affected our ability to access information?

<br />
<br />

### References

We referenced a similarly themed calculator made in JavaScript and used some of the weighted categories listed there for our project.

[CVSS Calculator by FIRST.ORG](https://github.com/cvssjs/cvssjs.github.io/tree/master/3.0)

<br />
<br />

#### Libraries

- Math
- PySimpleGUI
