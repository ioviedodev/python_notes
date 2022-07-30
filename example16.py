# Show use of dictionary

def print_citizens(citizens):
    print("----Citizen----")
    for citizen in citizens.items():    
        print("citizen: ", citizen)

def print_id_citizens(citizens):
    print("----ID_Citizen----")
    for id_citizen in citizens.keys():    
        print("citizen id: ",id_citizen)

def print_name_citizens(citizens):
    print("----NAME_Citizen----")
    for name_citizen in citizens.values():    
        print("citizen id: ",name_citizen)


def run():
    print("---Show use of dictionary---")
    citizens={
        "08351":"Daniel",
        "07351":"Ivan",
        "06351":"Cristina",
    }
    print_citizens(citizens)
    print_id_citizens(citizens)
    print_name_citizens(citizens)

if __name__=='__main__':
    run()
    