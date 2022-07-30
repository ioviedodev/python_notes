# Create a program that let the user add data to the memory or delete -Use of list-

def manage_op1_menu(ram_memory):
    data="0"
    data=input("Please insert a data: ")
    ram_memory.append(data)
    print("Adding sucessfully!")
    print(ram_memory)

def manage_op2_menu(ram_memory):
    while True:
        index=input("Please input the data index to be removed: ")
        if(index.isnumeric()):
            index=int(index)
            ram_memory.pop(index)
            print("Remove sucessfully!")
            print(ram_memory)  
            break
        else:
            print("Please input a valid index!!")
    return index 

def manage_main_menu(ram_memory):
    option="0"
    while option!="3":
        option=input("Please select an option: ")
        if(option=="1"):
            print("Selected option: ",option)
            manage_op1_menu(ram_memory)
            
        elif(option=="2"):
            print("Selected option: ",option)
            manage_op2_menu(ram_memory)

        elif(option=="3"):
            print("Selected option: ",option)
            print("Closing")
            break
        else:
            print("Please input a valid option!!")

def print_ram_data(ram_memory):
    index_data=0
    for data in ram_memory:    
        print("index: "+ str(index_data) + " | data: ", data)
        index_data+=1

def run():
    print("---Use of list---")
    ram_memory=[0xFF,8,"Daniel",True]
    print("The data which are in ram_memory: ",ram_memory)
    print_ram_data(ram_memory)
    print("\nDo you want to: \n1)Add data\n2)Delete data(Give index)\n3)Exit")
    manage_main_menu(ram_memory)


if __name__=='__main__':
    run()
    