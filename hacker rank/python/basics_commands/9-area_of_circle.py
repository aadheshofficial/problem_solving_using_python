def print_title():
    import os 
    print(os.path.basename(__file__))

def find_area_of_circle(r):
    from math import pi
    return (pi*r*r)

if __name__ == "__main__":
    print_title()
    r = float(input("enter radius : "))
    area = find_area_of_circle(r)
    print("area = ",area)