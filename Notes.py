'''
    Lesson: If and Else
    Author: Mr. Kalisz
    Date Created: October 15, 2024
    Date Last Modified: October 15, 2024
'''

# If Review

num = 25

if num < 20:
    print("run if statement")

# Else Statement

num = 5

if num == 15:
    print("num is equal to 15")
else: #has no condition -> the conditon represented by else here is num != 15
    #Unindent else statements
    print("num was not equal to 15")

if num < 20:
    print("run if statement")
else: #num >= 20
    print()

if num < 15 and num > 5:
    print()
else: # not (num < 15 and num > 5)
    #num >= 15 or num <= 5
    print()
