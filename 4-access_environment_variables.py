def print_title():
    import os 
    print(os.path.basename(__file__))
def get_path_env_var():
    import os
    return os.environ["PATH"]

if __name__ == "__main__":
    print_title()
    path = get_path_env_var()
    print(path)