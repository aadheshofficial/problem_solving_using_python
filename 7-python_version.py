def print_title():
    import os 
    print(os.path.basename(__file__))
def get_python_version():
    import sys
    return sys.version

if __name__ == "__main__":
    print_title()
    ver = get_python_version()
    print("python version :",ver)