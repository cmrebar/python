#Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]["last_name"] = 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)

#Iterate Through a List of Dictionaries

def iterateDictionary(my_dict):
    for x in range(0,len(my_dict)):
        for key, val in my_dict[x].items():
            print(key, '-', val)
        

students = [
    {'first_name':'Michael', 'last_name':'Jordan'},
    {'first_name':'John', 'last_name':'Rosales'},
    {'first_name':'Mark', 'last_name':'Guillen'},
    {'first_name':'KB', 'last_name':'Tonel'}
    ]


iterateDictionary(students) 

#Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    for x in range(0,len(some_list)):
        print(some_list[x][key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#Iterate Through a Dictionary with List Values

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key.upper())
        for x in range(0,len(some_dict[key])):
            print(some_dict[key][x])

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)


