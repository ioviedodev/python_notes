# Show the first n exponents of a number - using for- 

def oper_exponent(base,exponent):
    return base**exponent

def run():
    print("PShow the first n exponents of a number ")
    base=input("Input the base number.")
    first_n=input("Input the number of first n numbers.")

    if(base.isnumeric() and first_n.isnumeric()) :
        base=int(base)
        first_n=int(first_n)
        if(base>0 and first_n>0):
            for exponent in range (first_n):
                result=oper_exponent(base,exponent)
                print(str(exponent)+") "+str(base)+"**"+str(exponent)+" = "+str(result)) 
        else:
            print("Only numbers greater than zero!")
    else:
         print("Error invalid numbers!")
   

if __name__=='__main__':
    run()