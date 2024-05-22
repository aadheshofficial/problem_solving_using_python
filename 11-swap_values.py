def print_title():
    import os 
    print(os.path.basename(__file__))

def swap():
    a = 1
    b = 2
    print("a:",a)
    print("b:",b)
    c = a
    a = b
    b = c
    print("a:",a)
    print("b:",b)

if __name__ == "__main__":
    print_title()
    swap()