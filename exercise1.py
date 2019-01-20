# for val in "codingDojo!":
#     if val == "o":
#         continue
#     print (val)

# # for val in "string":
# #     if val == "i":
# #         break
# #     print(val)
# list = [3,5,1,2]
# for i in list:
#     print(i)

# list = [3,5,1,2]
# for i in range(list):
#     print(i)


# list = [3,5,1,2,5,6,7,6,4,3,2,3,342,23,4,23,4,23,42,7,4,5,5,4,56,45]
# for i in range(len(list)):
#     print(i)


# def biggie(arr)

class Case:
    def __init__(self,color,length,width,material):
        self.color = color
        self.length = length
        self.width = width
        self.material = material
    def drop(self):
        print(f"hi my color is {self.color} and i am made out of {self.material}")
        return self



case1 = Case("red"," ", " ", "nylon")
case1.drop().drop().drop().drop().drop()