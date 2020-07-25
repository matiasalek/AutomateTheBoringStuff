# Learned about the Try and Except statements in Python

def div42by(dividedBy):
    try:
        return 42 / dividedBy
    except ZeroDivisionError:
        print ('Error, you tried to divide by zero')

print (div42by(2))
print (div42by(0))
print (div42by(5))


#Another example using if statements

print ('How many cats do you have?')
cat = input()
try:
    if int(cat) >= 4:
        print ('That is a lot of cats.')
    else:
        print ('That is not that many cats.')
except ValueError:
    print ('You did not enter a number.')
