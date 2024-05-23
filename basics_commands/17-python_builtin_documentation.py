def print_title():
    import os 
    print(os.path.basename(__file__))
def documentation():
    print(int.__doc__)

if __name__ == "__main__":
    print_title()
    documentation()