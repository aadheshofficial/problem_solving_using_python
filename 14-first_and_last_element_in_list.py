def print_title():
    import os 
    print(os.path.basename(__file__))

def first_and_last(l):
    return l[0],l[-1]

if __name__ == "__main__":
    print_title()
    l = [0,1,2,3,4,5,6]
    first ,last = first_and_last(l)
    print("first : ",first," last : ",last)