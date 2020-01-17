"""
# Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(num):
    nums = []
    for val in range(num,-1,-1):
        nums.append(val)
    return nums
print(countdown(15))

# Print and Return - Create a function that will receive a list with two numbers. 
# Print the first value and return the second.
def pr(nums_list):
    print(nums_list[0])
    return(nums_list[1])
print(pr([5,2]))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def fpl(lst):
    return lst[0] + len(lst)
print(fpl([5,2,3,5,6]))

# Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def val_g(orig_list):
    new_list = []
    sec_val = orig_list[1]
    for idx in range(len(orig_list)):
        if orig_list[idx] > sec_val:
            new_list.append(orig_list[idx])
    print(len(new_list))
    return new_list
print(val_g([3,5,8,4,7,9,6,1]))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value.
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def l_v(size, value):
    new_list = []
    for num_times in range(size):
        new_list.append(value)
    return new_list

print(l_v(4,7))
"""




