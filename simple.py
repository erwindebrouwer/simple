# simple.py
import sys
#
# get input
number = input("Number: ")
#
# Check if input is a number
try:
    int(number)
except:
    print("ERROR: Your input is not a number!")
    sys.exit()
#
# print analysis
if number > 100:
    print("Wow! That's higher than 100!")
if number < 100:
    print("Oops... That's lower than 100.")
