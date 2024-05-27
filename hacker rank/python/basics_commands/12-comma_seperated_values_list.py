def print_title():
    import os 
    print(os.path.basename(__file__))

def seperate_elements(s):
    return s.split(",")

if __name__ == "__main__":
    print_title()
    s = input("enter element with , : ")
    l = seperate_elements(s)
    print(l)