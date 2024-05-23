def print_title():
    import os 
    print(os.path.basename(__file__))

    

if __name__ == "__main__":
    print_title()
    import cProfile
    def garbage():
        print(1,2)
    cProfile.run('garbage()')