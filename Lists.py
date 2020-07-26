# List are arrays in other programming languages.

list = ['cat', 'bat', 'rat', 'elephant']

# list are indexed, starting at 0. Cat is position 0, bat is position 1 and so on.

list[2] #rat

#can start index in negative like -1 which is the last element from end to start position.
# for example : list[-1] is elephant.

list[1:3] #goes from position 1, bat, to rat, because 3 is not included
#this is called slice
#can use slices to replace elements inside a list



#combining list (arrays) and FOR loops

supplies =  ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i]) #this prints each array element with a for loop

#multiple assignement
cat = ['fat', 'orange', 'small']

weight, color, size = cat #this assigns each element from the list to each new variable // weight = fat, etc etc

#another multiple assignement is
colors, sizes, weights = 'black','big','fats' #just like above, this assigns each string to the variables, one at
#a time

#swap assignment
a = 'AAA'
b = 'BBB'

#in order to swap them just multiple assigment
a, b = b, a

#learned about list methods (Functions) that are usable in lists (arrays)
#some examples are list.index, append, insert, remove, sort
