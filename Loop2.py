"""
# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def bigsize(new_list):
    for i in range(len(new_list)):
        if new_list[i] > 0 :
            new_list[i] = "big"
    return new_list
print(bigsize([-2,-3,5,6]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
def countpositives(lst):
    x = len(lst)
    count = 0
    for i in range(x):
        if lst[i] > 0:
            count = count + 1 
        lst[4] = count
    return lst    

print(countpositives([1,2,3,-1,-3]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
def sums(lst):
    sum = 0
    for val in lst:
        sum += val
    return sum
print(sums([1,2,3]))

# Average - Create a function that takes a list and returns the average of all the values.
def average(lst):
    sum = 0
    for val in lst:
        sum += val
    avg = sum/len(lst)
    return avg
print(average([4,6,8]))

# Length - Create a function that takes a list and returns the length of the list.
def length(lst):
    llist = 0
    for llist in lst:
        llist = len(lst)
    return llist
print(length([1,2,3,6,5,4,8]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum(lst):
    if len(lst) == 0:
        return False
    min = lst[0]
    for val in lst:
        if val < min:
            min = val
    return min
print(minimum([1,0,-2,-5,5,6]))

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
def maximum(lst):
    if len(lst) == 0:
        return False
    max = lst[0]
    for val in lst:
        if val > max:
            max = val
    return max
print(maximum([1,0,-2,-5,5,6]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def untimateanalysis(lst):
    new_dictonary = {
        'sumtotal': None,
        'maximum': None,
        'minimum': None,
        'average': None,
        'length': 0
    }
    if len(lst) == 0:
        return new_dictonary
    else:
        new_dictonary['sumtotal'] = 0
        new_dictonary['maximum'] = lst[0]
        new_dictonary['minimum'] = lst[0]
    for val in lst:
        if val > new_dictonary['maximum']:
            new_dictonary['maximum'] = val
        elif val < new_dictonary['minimum']:
            new_dictonary['minimum'] = val

        new_dictonary['sumtotal'] += val
        new_dictonary['length'] += 1
    new_dictonary['average'] = new_dictonary['sumtotal']/len(lst)
    return new_dictonary
print(untimateanalysis([10,55,-2,5,15]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
def reverselist(lst):
    half_len = int(len(lst) / 2)
    for i in range(half_len):
        lst[i] , lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst
print(reverselist([1,5,9,10,-15]))
"""