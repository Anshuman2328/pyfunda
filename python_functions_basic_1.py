
# def a():
#     return 5
# print(a())     

# 5

# def a():
#     return 5
# print(a()+a())     

# # 10

# def a():
#     return 5
#     return 10
# print(a())     

# 5

# def a():
#     return 5
#     print(10)
# print(a())     

# 5 since return 5 will terminate the above function

# def a():
#     print(5)
# x = a()
# print(x)     

# 5 and nothing since no parameter is being passed


# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))   

# it will print 3 and 5 and none since last print just says to print the 3 + 5


# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))

# string of 25

# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())

# 100 and 10

# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))     

# 7, 14 and 21

# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))     

# returns 8

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)  

# 500, 500, 300 and 500 due to indentation 

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)  

# 500, 500, 300, 500

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)

#  500, 500, 300, 300

# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()

#  1, 3, 2

# list = [3,5,1,2]
# for i in list:
#     print(i)


# list = [3,5,1,2]
# for i in range(list):
#     print(i)

# list = [3,5,1,2]
# for i in range(len(list)):
#     print(i)


# examples from before
# sum = 0
# for num in range(1, 5):
#     if num % 2 != 0:
#         sum+= num
#     num+=1
# print("sum of odd no.s are ", sum)

# for i in range(2022, 0):
#     if i > 2022:
#         i = i - 4
#         print(i)



# num = 5
# len(list) = num
# def cd(num):
#     for i in range (num, 0, -1):
#         # len(list) = num
#         # list.append(num)
#         print(i)
#     # return newarr
# y = cd(5)
# print(y)


# def cd(num):


# x = "hello python"
# print (x)
# y = 42
# print (y)

# ninjas = ["carson", "ash", 18, 32]
# print(len(ninjas))
# print(ninjas[2])
# ninjas.append("anjali")
# ninjas.append(28)
# print(ninjas242)