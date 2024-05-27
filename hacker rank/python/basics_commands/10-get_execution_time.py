def print_title():
    import os 
    print(os.path.basename(__file__))

def cal_time():
    import time
    st = time.time()
    for i in range(1000):
        print(i)
    et = time.time()
    print("execution time :",(et-st))

if __name__ == "__main__":
    print_title()
    cal_time()