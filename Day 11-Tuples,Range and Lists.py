#tuples and immutability
my_tuple = (30,55,43)
print(my_tuple[0]) #Output will be 30
my_tuple[1] = 93 
#Line 4 will raise an error
#because tuples are immutable

#lists and mutability
my_list = [67,45,39]
my_list.append(54) #54 will be added as an item in my_list
my_list[2] = 43 #the third element in my_list will be modified
print(my_list) # Output: [67,45,43,54]

#range
for i in range(3):
    print(i)  #output: 0 1 2