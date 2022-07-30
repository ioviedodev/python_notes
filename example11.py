# Show use of break for validation of input data 



def use_break():
    print("Program that validate the input data will be a number")

    while True:
        number=input("Please input a number: ")
        if(number.isnumeric()):
            number=int(number)
            break
        else:
            print("Please input a valid number")
    print("Sucessfully input number: ",number)

def run():
    print("")

if __name__=='__main__':
    run()