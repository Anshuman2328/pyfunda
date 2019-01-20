

# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big".
# Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].


# def biggie(arr):
#     for i in range (len(arr)):
#         if arr[i] > 0:
#             arr[i] = "big"
#     return arr
# y = biggie([-1,2,3,-5])
# print(y)


# Count Positives - Given an array of numbers,
# create a function to replace last value with number of positive values.
#  Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.
# (Note that zero is not considered to be a positive number).


# arr = []
# def positives(arr):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] > 0:
#             count+= 1
#             arr[len(arr)-1] = count
#     return arr
# y = positives([-1,1,1,1,3,4,5,6,7,8,6,4,2,3])
# print(y)


# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.
# For example sumTotal([1,2,3,4]) should return 10


# arr =[]
# def total(arr):
#     sum = 0
#     for i in range (len(arr)):
#         sum = sum + arr[i]
#     return sum
# y = total([1,2,3,4])
# print(y)


# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.
# For example multiples([1,2,3,4]) should return 2.5

# arr = []
# def average(arr):
#     sum = 0
#     for i in range(len(arr)):
#         sum = sum + arr[i]
#     return sum/len(arr)
# y = average([1,2,3,4])
# print(y)

# Length - Create a function that takes an array as an argument and returns the length of the array.
# For example length([1,2,3,4]) should return 4

# def length(arr):
#     return len(arr)
# y = length([1,2,3,4])
# print(y)

# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.
# If the passed array is empty, have the function return false.
# For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.


# def minimum(arr):
#     if len(arr) == 0:
#         return False
#     min = arr[0]
#     for i in range(len(arr)):
#         if arr[i] < min:
#             min = arr[i]
#     return min
# y = minimum([1,2,3,4,-1])
# print(y)

# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.
# If the passed array is empty, have the function return false.
# For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.


# def maximum(arr):
#     if len(arr) == 0:
#         return False
#     max = arr[0]
#     for i in range(len(arr)):
#         if arr[i] > max:
#             max = arr[i]
#     return max
# y = maximum([1,2,3,4])
# print(y)



# UltimateAnalyze - Create a function that takes an array as an argument and
# returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.

# anlyze = {}
# def ulti(arr):
#     maxval = arr[0]
#     minval = arr[0]
#     sum = 0
#     for i in range(len(arr)):
#         if arr[i] > maxval:
#             maxval = arr[i]
#         anlyze['maxval'] = maxval
#         if arr[i] < minval:
#             minval = arr[i]
#         anlyze['minval'] = minval
#         sum = sum + arr[i]
#         anlyze['sum'] = sum
#         anlyze['avg'] = sum/len(arr)
#         anlyze['length'] = len(arr)
        
#     return ()
# y = ulti([1,2,3,4,5,6,7,8,9,10])
# print(y)
# print(anlyze)
        


# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.
# Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1].
# This challenge is known to appear during basic technical interviews.

# def reverse(list):
#     # temp = 0
#     for i in range (0, len(list)//2,1):
#         temp = list[i]
#         list[i] = list[len(list) - 1 - i]
#         list[len(list) -1 - i] = temp
#     return list
# print(reverse([1,2,3,4,5,6,7,8,9]))



# name = 'ash'
# age = 27
# # group = 'coding dojo'
# # print(f'my name is {name} and i am {age} years old and my group name is {group}')
# print(name.title())   
