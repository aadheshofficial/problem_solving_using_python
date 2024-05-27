# There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if is on top of  then .
# When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.
# Example

# Result: No
# After choosing the rightmost element, , choose the leftmost element, . After than, the choices are  and . These are both larger than the top block of size .

# Result: Yes
# Choose blocks from right to left in order to successfully stack the blocks.
# Input Format
# The first line contains a single integer , the number of test cases.
# For each test case, there are  lines.
# The first line of each test case contains , the number of cubes.
# The second line contains  space separated integers, denoting the sideLengths of each cube in that order.
# Constraints



# Output Format
# For each test case, output a single line containing either Yes or No.
# Sample Input
# STDIN        Function
# -----        --------
# 2            T = 2
# 6            blocks[] size n = 6
# 4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
# 3            blocks[] size n = 3
# 1 3 2        blocks = [1, 3, 2]
# Sample Output
# Yes
# No
# Explanation
# In the first test case, pick in this order: left - , right - , left - , right - , left - , right - .
# In the second test case, no order gives an appropriate arrangement of vertical cubes. will always come after either  or .

# Enter your code here. Read input from STDIN. Print output to STDOUT
def can_stack_cubes(cube_lengths):
    left = 0
    right = len(cube_lengths) - 1
    last_cube = float('inf')

    while left <= right:
        if cube_lengths[left] <= last_cube and cube_lengths[right] <= last_cube:
            if cube_lengths[left] >= cube_lengths[right]:
                last_cube = cube_lengths[left]
                left += 1
            else:
                last_cube = cube_lengths[right]
                right -= 1
        elif cube_lengths[left] <= last_cube:
            last_cube = cube_lengths[left]
            left += 1
        elif cube_lengths[right] <= last_cube:
            last_cube = cube_lengths[right]
            right -= 1
        else:
            return "No"
    return "Yes"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        n = int(data[index])
        cubes = list(map(int, data[index + 1: index + 1 + n]))
        index += 1 + n
        results.append(can_stack_cubes(cubes))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
