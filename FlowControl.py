# Flow control, second part of ABSWPython Udemy

#if statements
name = 'Bob'
age = 3000
if name == 'Matias':
    print ('Hi Matias')
elif age < 12:
    print ('You are not Matias')
elif age > 2000:
    print ('You are too old.')
elif age > 100:
    print ('You are old but not THAT old')
print ('Done')


print ('Enter a name: ')
name = input()
if name:
    print ('Your name is: ' + name)
else:
    print ('You did not enter a name.')


# for loops
for i in range(5):
    print ('Numero' + str(i))

#for loops Gauss
total = 0
for num in range(101):
    total = total + num
print (total)
