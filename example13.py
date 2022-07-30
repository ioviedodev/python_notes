# Game guess the number
import random

# Constants
NUMBER_HIDE         =   45
GUESS               =   0   
CONTINUE_TRYING     =   -1   

def run():
    print("---Game guess the number---")
    number_hide=random.randint(1,100)

    while True:    
        number=validate_number()
        print("number: ",number)
        result=check_guess_number(number,number_hide)
        if(result==GUESS):
            break

def validate_number():
    while True:
        number=input("Please input a number: ")
        if(number.isnumeric()):
            number=int(number)
            break
        else:
            print("Please input a valid number!!")
    return number  

def check_guess_number(number,number_to_guess):
    if(number_to_guess==number):
        print("Congratulation!!! You gess the number!!..")
        return GUESS
    elif(number_to_guess>number):
        print("Continue trying!!! Try with a greater number!!..")
        return CONTINUE_TRYING
    else:
        print("Continue trying!!! Try with a less number!!..")
        return CONTINUE_TRYING    

if __name__=='__main__':
    run()