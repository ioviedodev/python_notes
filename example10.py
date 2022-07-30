# Show  use of break and continue

def use_continue(nbr_iteration, nbr_skip):
            nbr_iteration=int(nbr_iteration)
            nbr_skip=int(nbr_skip)
            if(nbr_iteration>0 and nbr_skip>0):
                for index in range(nbr_iteration):
                    if(index==nbr_skip):
                        continue
                    print(index)
            else:
                print("Invalid numbers")

def use_break(text):
    if(len(text)>0):
            print(text)
            for character in text:
                print(character)
                if(character=='a'):                    
                    break
    else:
        print("Invalid text")

def run():
    print("Show  use of break and continue")
    text=input("Please input a text: ")
    use_break(text)
    nbr_iteration=input("Please input a number of iteration: ")
    nbr_skip=input("Please input the number for skiping the iteration: ")
    use_continue(nbr_iteration, nbr_skip) 

if __name__=='__main__':
    run()