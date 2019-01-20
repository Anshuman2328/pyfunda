

# Countdown - Create a function that accepts a number as an input.
# Return a new array that counts down by one, 
# from the number (as arrays 'zero'th element) down to 0 (as the last element).
# For example countDown(5) should return [5,4,3,2,1,0].

# array = []
# def countdown(num):
#     for num in range(num, -1,-1):
#         array.append(num)
#     print(len(array))
#     return array
# print(len(array))
# y = countdown(9)
# print(y)

# &&************* This above function takes a num, returns an array, and
# gives the lenght of original array/list and new array/list






# Print and Return - Your function will receive an array with two numbers.
# Print the first value, and return the second.

# arr = []
# def prval(arr):
#     print(arr[0])
#     return arr[1]
# y = prval([2,3,4,5,6,7,8,9])
# print(y)

#  This function takes an array, prints first index position and returns second index position and 
# then prints the 2nd index


# First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.

# arr = []
# sum = 0
# def firstplus(arr):
#     sum = (arr[0]) + len(arr)
#     return sum
# y = firstplus([1,2,3,4,5,5,4,3,2,4,5,4,6,7,8,6,4,3,9])
# print (y)

#  above function returns first plus length




# Values Greater than Second - 
# Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.
# Print how many values this is.  If the array is only one element long, have the function return False

# newarr = []
# def greater(arr):
#     count = 0
#     for i in range (0,len(arr), 1):
#         if len(arr) == 1:
#             return False
#         elif arr[i] > arr[1]:
#             newarr.append(arr[i])
#             count = count + 1
#         else:
#             continue
#     print(count)
#     return newarr
# y = greater([15])
# print(y)

# This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value.
# This function should take two numbers and return a list of length size containing only the number in value.
# For example, lengthAndValue(4,7) should return [7,7,7,7].


# arr = []
# def lenval(size,val):
#     for i in range (0,size,1):
#         arr.append(val)
#     return arr
# y = lenval(26,98)
# print(y)


# this takes 2 no.s and returns an array with sexond no repeated first num times.

# arr = []
# def lenval(size,val):
#     for i in range(0,6,1):
#         arr[i] = 9
#         arr.append(arr[i])
#     return arr
# y = lenval(6,9)
# print(y)



# class Node:
#     def__init__(self,val):
#         self.next = None
#         self.val = val

# class Slist:
#     def__init__(self):
#         self.head = None
#     def append(self,val)
#         mynode = node(val)
#         if self.head == None:
#             self.head = mynode
#         else :
#             current = self.head
#             while current.next != None
#                 current.next = mynode
#         return self

    

# mylist = Slist()



# def funcname(self, parameter_list):
#     raise NotImplementedError
