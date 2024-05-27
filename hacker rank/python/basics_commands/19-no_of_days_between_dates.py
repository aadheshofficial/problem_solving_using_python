from datetime import date

def print_title():
    import os 
    print(os.path.basename(__file__))

def cal_days(f_d,l_d):
    return l_d - f_d


if __name__ == "__main__":
    print_title()
    f = date(2025,5,6)
    l = date(2025,5,10)
    n = cal_days(f,l)
    print("number of days : ",n)