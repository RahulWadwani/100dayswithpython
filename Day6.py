# data types and variable
# what is a variable 

# container that holds data

a = 1
print(a)


# data type 
# type of value a variable can hold 
a = 1
b = True
c = "Rahul"
d = None

print('The type of a is ',type(a))
print('The type of b is ',type(b))
print('The type of c is ',type(c))
print('The type of d is ',type(d))

# built in data type
a = 1.1
b = complex(8,2) 
c = 8+2j
print('The type of a is ',type(a))
print('The type of b is ',type(b))
print('The type of c is ',type(c))


#list 
# list of items mutable
list1 = [1,2,3,[4,5,6],'rahul',1.2]
print(list1)


# tuple 
# list of item but immutable
tuple1 = (1,2,3,(4,5,6),'rahul',1.2)
print(tuple1)


# mapped : dictionary
# collection of key and value pair
map1 = {"Name": "Rohini",'roll' : 34} 
print(map1)

# everything in python is an object 