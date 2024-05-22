def print_title():
    import os 
    print(os.path.basename(__file__))

def cal(n):
    n2 = int("%s%s"%(n,n))
    n3 = int("%s%s%s"%(n,n,n))
    s = n+n2+n3
    return s

if __name__ == "__main__":
    print_title()
    n = int(input("enter n :" ))
    sum = cal(n)
    print("n + nn + nnn = ",sum)