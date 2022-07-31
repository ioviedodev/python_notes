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

#POSSIBLE CHARACTER VALUES
MAYUS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z')
MINUS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
NUMS  = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
CHARS = ('*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"')

#Contraints for categories - It has de itentifiers
categories_fixed    = [SPECIAL_CHARACTER, LETTER_UPPERCASE, NUMBERS, LETTER_LOWERCASE]                                       #List
#Contraints for pasword -at least this minimun requirements-
constraints         = { SPECIAL_CHARACTER:2, LETTER_UPPERCASE:5, NUMBERS:2, LETTER_LOWERCASE:5}                             #Dictionary
#Current contraint count
current_count_lst   = [[SPECIAL_CHARACTER,0],[LETTER_UPPERCASE,0],[LETTER_LOWERCASE,0],[LETTER_LOWERCASE,0]]          #List

def get_current_count_lst(categories,current_count_lst,index_category):
    current_count   = -1
    for category in current_count_lst:         
        if(category[INDEX_CATEGORY_CURRENT_ID]==categories[index_category]):
            current_count   = category[INDEX_CATEGORY_CURRENT_VALUE]
    return current_count


def check_is_category_needed(index_category,categories,constraints,current_count_lst):
    key             = categories[index_category]
    requirment      = constraints[key]
    current_count   = get_current_count_lst(categories,current_count_lst,index_category)
    if(force_mode):
        if(current_count_lst<requirment):
            return True
        else:
            if(len(categories)>0):        
                categories.pop(index_category)
            else:
                force_mode=False
                categories=categories_fixed  
            return False
    else:
        return True

def categories_get_rage(categories):
    return len(categories)-1

def generate_category(constraints,categories, current_count_lst):
    categories_range=categories_get_rage(categories)
    index_random_category=random.randint(0,categories_range)
    return index_random_category


def key_generation(constraints,categories, current_count_lst, len_constraint):
    finished            =   False
    category_needed     =   True
    nbr_char_generated  =   0
    password=[]

    while(category_needed and len(password)<LEN_PASSWORD):
        index_random_category   =   generate_category(constraints,categories, current_count_lst)
        category_needed         =   check_is_category_needed(index_random_category,categories,constraints,current_count_lst)
        
 

def run():
    print("---Generate passwords---")
    categories_mirror = categories_fixed

    print(constraints)
    print(current_count_lst)

    key_generation(constraints,categories_mirror, current_count_lst, LEN_PASSWORD)

if __name__=='__main__':
    run()
    