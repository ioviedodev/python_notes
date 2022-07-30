# Show iteration of a string


def run():
    print("Show iteration of a string")
    text=input("Please input a text: ")
    if(len(text)>0):
        print(text)
        for character in text:
            print(character)
    else:
        print("Invalid text")

if __name__=='__main__':
    run()