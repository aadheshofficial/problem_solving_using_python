def print_title():
    import os 
    print(os.path.basename(__file__))

def get_numbers(n):
    a = []
    for i in range(n):
        data = int(input("enter :"))
        a.append(data)
    return a

def find_avg_of_list(a,n):
    sum = 0
    for i in a:
        sum += i
    return float(sum/n)


if __name__ == "__main__":
    print_title()
    n = int(input("enter n :"))
    a = get_numbers(n)
    avg = find_avg_of_list(a,n)
    print(avg)