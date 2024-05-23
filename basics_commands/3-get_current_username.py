def print_title():
    import os 
    print(os.path.basename(__file__))

def get_current_username():
    import getpass
    return getpass.getuser()

if __name__ == "__main__":
    print_title()
    user = get_current_username()
    print("username : ",user)