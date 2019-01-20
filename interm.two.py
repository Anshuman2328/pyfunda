

arr = [10,7,8,3,2,9]

def sel(arr):
    for i in range(len(arr) +1):
        if arr[i]  < arr[i+1]:
            i = i+1
        else:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1]
    return(arr)
print(sel(arr))





# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15
# print (x)

# students[0]['last_name'] = "Bryant"
# print(students)

# sports_directory["soccer"][0] = "Andres"
# print(sports_directory)

# z[0]["y"] = 30
# print(z)


# 2. Create a function that given a list of dictionaries,
#  it loops through each dictionary in the list 
# and prints each key and the associated value.
# For example, given the following list:
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def studs(dict):

#     for x in students:
#         for i,j in x.items():

#             print(f'{i} - {j}')  

# studs(students)


# 3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.
#  For example, iterateDictionary2('first_name', students) should output


# def studs (dict):
#     for x in students:
#         print(x['first_name'])

# studs(students)

# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# Create a function that prints the name of each location and also how many locations the Dojo currently has.
# Have the function also print the name of each instructor and how many instructors the Dojo currently has


# def cd(dict):
#     print(str(len(dojo['locations'])) +' '+ 'locations')
#     for v in  dojo['locations']:
#         print(v)
#     print(str(len(dojo['instructors'])) +' '+ 'instructors')
#     for w in dojo['instructors']:
#         print(w)


#     for k,v in dojo.items():
#         print(f'{v}')
# cd(dict)


