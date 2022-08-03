
def set_divider(divider: int):
    def make_division(number: int)->float:
        return number/divider
    return make_division

def repeater(mult_number: int):
    def text_multiplied(string: str)->str:
        assert type(string)==str, "Only use string!"
        return string*mult_number
    return text_multiplied

def run():
    print("Use of closure")

    print("Text repeater")
    repeater_of_5=repeater(5)
    print(repeater_of_5("You can!"))

    print("Division by 5")
    division_by_5=set_divider(5)
    print(type(division_by_5(37)))
    print(division_by_5(37))
if __name__=='__main__':
    run()