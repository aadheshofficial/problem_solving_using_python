def print_title():
    import os 
    print(os.path.basename(__file__))

def list_all_files():
    from os import listdir
    from os.path import isfile,join
    files = []
    for f in listdir('.'):
        if isfile(f):
            files.append(f)
    return files


if __name__ == "__main__":
    print_title()
    files = list_all_files()
    print(files)