def print_title():
    import os 
    print(os.path.basename(__file__))

def sum_of_first_n_numbers(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

if __name__ == "__main__":
    print_title()
    n = int(input("enter n:"))
    sum = sum_of_first_n_numbers(n)
    print(sum)