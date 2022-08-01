# Project Password generator
import random

#Constants
LEN_PASSWORD                    = 20
SPECIAL_CHARACTER               = "SC"
LETTER_UPPERCASE                = "LU"
LETTER_LOWERCASE                = "LL"
NUMBERS                         = "NN"
INDEX_CATEGORY_CURRENT_ID       = 0
INDEX_CATEGORY_CURRENT_VALUE    = 1

force_mode                      = True
index_current_count_lst         = 0
removed_categories              = []

#POSSIBLE CHARACTER VALUES
MAYUS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z')
MINUS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
NUMS  = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
CHARS = ('*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"')

#Contraints for categories - It has de itentifiers
categories_fixed    = [SPECIAL_CHARACTER, LETTER_UPPERCASE, NUMBERS, LETTER_LOWERCASE]                      #List
#Contraints for pasword -at least this minimun requirements-
constraints         = { SPECIAL_CHARACTER:2, LETTER_UPPERCASE:5, NUMBERS:2, LETTER_LOWERCASE:5}             #Dictionary
#Current contraint count
current_count_lst   = [[SPECIAL_CHARACTER,0],[LETTER_UPPERCASE,0],[NUMBERS,0],[LETTER_LOWERCASE,0]]         #List

def get_current_count_lst(categories,current_count_lst,index_category):
    global index_current_count_lst
    current_count   = -1
    index           = 0
    for category in current_count_lst:         
        if(category[INDEX_CATEGORY_CURRENT_ID]==categories[index_category]):
            current_count   = category[INDEX_CATEGORY_CURRENT_VALUE]
            index_current_count_lst         = index
        index+=1
    return current_count


def check_is_category_needed(index_category,categories,constraints,current_count_lst,password):
    key             = categories[index_category]
    requirment      = constraints[key]
    current_count   = get_current_count_lst(categories,current_count_lst,index_category)
    global force_mode

    if(current_count<requirment):
        return True
    else:
        if(len(removed_categories)<len(categories)):   
            removed_categories.append(index_category)     
            return False
        else:
            force_mode = False
            if(len(password)<LEN_PASSWORD):
                return True
            else: 
                return False

def categories_get_rage(categories):
    return len(categories)-1

def generate_category(categories):
    index_random_category = 0
    categories_range=categories_get_rage(categories) #removed_categories
    
    index_random_category=random.randint(0,categories_range)

    return index_random_category


def get_random_char(categories,index_random_category):
    char_random                 = 0xFF
    random_index_char           = 0

    if(categories[index_random_category]    == SPECIAL_CHARACTER):
        random_index_char=random.randint(0,len(CHARS)-1)
        char_random=CHARS[random_index_char]
    elif(categories[index_random_category]  == LETTER_UPPERCASE):
        random_index_char=random.randint(0,len(MAYUS)-1)
        char_random=MAYUS[random_index_char]
    elif(categories[index_random_category]  == LETTER_LOWERCASE):
        random_index_char=random.randint(0,len(MINUS)-1)
        char_random=MINUS[random_index_char]           
    else: #NUMBERS
        random_index_char=random.randint(0,len(NUMS)-1)
        char_random=NUMS[random_index_char]

    return char_random 

def key_generation(password,constraints,categories, current_count_lst):
    global index_current_count_lst
    category_needed     =   True
 
    while(len(password)<LEN_PASSWORD):
        index_current_count_lst     = 0
        index_random_category       = generate_category(categories)
        category_needed             = check_is_category_needed(index_random_category,categories,constraints,current_count_lst,password)
        char_random                 = 0xFF

        if(category_needed):
            current_count_lst[index_current_count_lst][INDEX_CATEGORY_CURRENT_VALUE]+=1
            char_random=get_random_char(categories,index_random_category) 
            password.append(char_random)     

def run():
    print("---Generate passwords---")
    categories_mirror = categories_fixed
    password=[]
    password_str=""
    print("constraints: ",constraints)
    

    key_generation(password, constraints, categories_mirror, current_count_lst)
    password_str="".join(password)
    print("PASSWORD: ",password_str)
    print("LEN_PASSWORD: ", len(password_str))
    print("current_count_lst: ",current_count_lst)

if __name__=='__main__':
    run()
    