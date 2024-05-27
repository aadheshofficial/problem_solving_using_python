def print_title():
    import os 
    print(os.path.basename(__file__))
def show_schedule():
    date = (2,5,24)
    print("%i / %i / %i" %date)

if __name__ == "__main__":
    print_title()
    show_schedule()