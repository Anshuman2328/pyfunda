#Basic - Print all the numbers/integers from 0 to 150.

# for num in range (0,151):
#     print ("the num is " , num)



#Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.

# for num in range (5,101):
#     if num % 5 ==0:
#         print("The num is ", num, " A multple of 5 ")

#Counting, the Dojo Way - Print integers 1 to 100.
#If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

# for num in range (0,101):
#     if num % 10==0:
#         print("Coding Dojo")
#     elif num % 5 == 0:
#         print("Coding")
#     else:
#         print(num)

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

# sum = 0
# for num in range(1, 5):
#     if num % 2 != 0:
#         sum+= num
#     num+=1
# print("sum of odd no.s are ", sum)
    

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).

# num = 2022
# while (num >4):
#     num = num -4
#     print(num)

# Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult,
#  print multiples of mult from lowNum to highNum, using a FOR loop.
# For (2,9,3), print 3 6 9 (on successive lines)


# lownum = 3
# highnum = 15
# mult = 3
# for num in range (lownum, highnum +1):
#     if (num % mult == 0):
#         print (num)
