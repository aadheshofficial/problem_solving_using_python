def print_title():
    import os 
    print(os.path.basename(__file__))

def find_extension(file):
    f_ext = file.split(".")
    return f_ext[-1]

if __name__ == "__main__":
    print_title()
    file = input("enter file name with extension :")
    ext = find_extension(file)
    print("extension : ",repr(ext))