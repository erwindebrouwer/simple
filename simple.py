# simple.py
import sys
#
def Check_Number(number):
    # Check if input is a number
    try:
        int(number)
    except:
        print("ERROR: Your input is not a number!")
        sys.exit()
#
def Analyze_Number(number):
    # print analysis
    if int(number) > 100:
        return "Wow! That's higher than 100!"
    if int(number) < 100:
        return "Oops... That's lower than 100."
    if int(number) == 100:
        return "No way! That's exactly 100!"
#
if __name__ == "__main__":
    # get input
    number = input("Number: ")
    Check_Number(number)
    conclusion = Analyze_Number(number)
    print(conclusion)
