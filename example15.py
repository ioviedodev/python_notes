# Use of Tuplas

def print_ram_data(constants):
    index_data=0
    for data in constants:    
        print("index: "+ str(index_data) + " | data: ", data)
        index_data+=1

def run():
    print("---Use of list---")
    constants=(0xFF,8,"Daniel",True)
    print("The data which are in ram_memory: ",constants)
    print_ram_data(constants)


if __name__=='__main__':
    run()
    