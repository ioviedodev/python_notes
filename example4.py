# Currency conversion -With use of functions-


def do_conversion(money, rate):
    money_dollar=float(money*rate)
    return money_dollar

print("Current conversion to dollars - using functions")
currency=input("Select the currency: \n1)Argentine peso \n2)Colombian currency \n3)Mexican currency ")
money = input("Input the money: ")

currency=int(currency)
money=float(money)
money_dollar=float(0)

successful=True

rate_argentine_dollar=0.0076
rate_colombian_dollar=0.00023
rate_mexican_dollar=0.049

if(currency==1): #argentine currency
    money_dollar=do_conversion(money, rate_argentine_dollar)
elif(currency==2): #colombian currency
    money_dollar=do_conversion(money,rate_colombian_dollar)
elif(currency==3): #mexican currency
    money_dollar=do_conversion(money,rate_mexican_dollar)
else:
    successful=False

# money_dollar=round(money_dollar,2)

if(successful):
   print("You have $"+ str(money_dollar)+ " dollars")     
else:
    print("invalid currency type")
