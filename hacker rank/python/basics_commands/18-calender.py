def print_title():
    import os 
    print(os.path.basename(__file__))

def print_calender(year,month):
    import calendar
    print(calendar.month(year,month))


if __name__ == "__main__":
    print_title()
    y = int(input("year :"))
    m = int(input("month : "))
    print_calender(y,m)

