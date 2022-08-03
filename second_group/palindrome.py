# Detect if a string is or not "palindromo"
# + Static typed

def check_palindromo(user_text: str) -> bool:
    user_text=user_text.replace(" ","")
    user_text=user_text.lower()
    user_text_swap=user_text[::-1]

    print("Word input:      "+user_text)
    print("Swap word:       "+user_text_swap)

    if(user_text == user_text_swap):
        return True
    else:
        return False    


def run():
    print("Programs to detect if a string is or not a Palindromo word")
    user_text=input("Input a word: ")
    is_palindromo=False
    if(len(user_text)>0):
        if(check_palindromo(user_text)):
            print("Yes, it is a Palindromo word")
        else:
            print("No, it is a Palindromo word")    
    else:
        print("Invalid word")    

if __name__=='__main__':
    run()