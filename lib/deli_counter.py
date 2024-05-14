katz_deli = []

def line(katz_deli):
    line_list = []
    if len(katz_deli) == 0 or katz_deli == '':
        print("The line is currently empty.") 
    else : 
        for name in katz_deli:
            line_list.append(f"{katz_deli.index(name) + 1}. {name}")
        line_list_string = " ".join(line_list)
        print(f"The line is currently: {line_list_string}")      


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {katz_deli.index(name) + 1} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else :
        print(f"Currently serving {katz_deli[0]}.")
        del(katz_deli[0])