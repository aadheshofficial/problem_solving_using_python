def print_title():
    import os 
    print(os.path.basename(__file__))

def display_current_data_time():
    import datetime
    now = datetime.datetime.now()
    print("current date and time : ")
    print(now.strftime("%y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    print_title()
    display_current_data_time()