# More Conditional Tests: You don’t have to limit the number of tests you
# create to 10. If you want to try more comparisons, write more tests. Have
# at least one True and one False result for each of the following:
# • Tests for equality and inequality with strings

# • Tests using the lower case function

# • Numerical tests involving equality and inequality, greater than 
# and less than, greater than or equal to, and less than or equal to

# • Tests using "and" and "or" operators

# • Test whether an item is in a array

# • Test whether an item is not in a array

# • Tests for equality and inequality with strings
print("apple"=="apple")
print("apple"!="apple")
print("apple"!="orange")

# • Tests using the lower case function
print("APPLE".lower())



# • Numerical tests involving equality and inequality, greater than 
# and less than, greater than or equal to, and less than or equal to
print(10 ==10)
print(10<=10)
print(20<10)
print(5!=5)
print(50>=59)
print(60<60)


# • Tests using "and" and "or" operators
print(10 == 10 and 10!=10) #false
print(23<10)or(5!=8) #false
print(2<=2) and (9>=100) # false
print(10!=10) or (5==29)
print(3>=3) and (9<200)


# 5. Test whether an item is in a list
fruits=['apple','mango','banana','grapes']
print('apple' in fruits)
print('orange' in fruits)