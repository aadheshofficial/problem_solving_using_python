from math import pi

def print_title():
    import os 
    print(os.path.basename(__file__))

def vol(r):
    return (4/3*(pi*r**3))

if __name__ == "__main__":
    print_title()
    r = float(input("enter radius :"))
    v = vol(r)
    print("volume of sphere : ",v)