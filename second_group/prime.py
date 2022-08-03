# Match if a number is prime 
# + Static typed

#Constants
LIMIT_FACTORS=2

def check_is_prime(number: int) -> bool:
    nbr_factor=0

    is_prime=True
    for index in range(1,number+1):
        if(nbr_factor>LIMIT_FACTORS):
            is_prime=False
            break

        if(number%index==0):
            nbr_factor+=1
    
    return is_prime

def validate_number():
    number=-1
    while True:
        number_str=input("Please input a number: ")
        if(number_str.isnumeric()):
            number=int(number_str)
            break
        else:
            print("Please input a valid number!!")
    return number  

def run():
    print("---Match if a number is prime---")

    number=validate_number()
    print("number: ",number)
    is_prime=check_is_prime(number)
    message="The number: %i " % (number)
    
    if(is_prime):
        message+= "is prime"
    else:
        message+= "is not prime"

    print(message)

if __name__=='__main__':
    run()