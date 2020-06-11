#taken from: https://automatetheboringstuff.com/2e/chapter3/
import random 
def bumble(buzz):
    a = input("think of the question you want to ask then press enter")
    if buzz == 1:
        return 'it will be!'
    elif buzz == 2:
        return 'the force is with you'
    elif buzz == 3:
        return 'naw'
    elif buzz == 4:
        return 'booooom goes.... the actuall answer is no' 
    elif buzz == 5:
        return 'too complex for the future to be seen'   
    elif buzz == 6:
        return 'yes' 
    elif buzz == 7:
        return 'no'
    elif buzz == 8:
        return 'that is the way' 
    elif buzz == 9:
        return 'look inward, you will know the way'
    elif buzz == 0:
        return "yesn't"   
print(bumble(random.randint(0,9)))