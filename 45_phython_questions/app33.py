# Ordinal Numbers: Ordinal numbers indicate their position in a array, such as 1st or 2nd.
# Most ordinal numbers end in th, except 1, 2, and 3.
# • Store the numbers 1 through 9 in a array.

# • Loop through the array.

# • Use an if-else chain inside the loop to print the proper ordinal ending for each number.
# Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

# Numbers 1 se 9 tak store karna
numbers = list(range(1, 10))  

# Loop chalana har number ke liye
for number in numbers:
    if number == 1:
        print(f"{number}st")  # 1 ke liye 'st'
    elif number == 2:
        print(f"{number}nd")  # 2 ke liye 'nd'
    elif number == 3:
        print(f"{number}rd")  # 3 ke liye 'rd'
    else:
        print(f"{number}th")  # Baqi sab ke liye 'th'
