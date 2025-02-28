# Checking Usernames: Do the following to create a program that simulates how websites 
# ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.

# • Make another list of five usernames called new_users. 
# Make sure one or two of the new usernames are also in the current_users list.

# • Loop through the new_users list to see if each new username
# has already been used. If it has, print a message that the person
# will need to enter a new username. If a username has not been used, 
# print a message saying that the username is available.

# • Make sure your comparison is case insensitive.
# If 'John' has been used, 'JOHN' should not be accepted.


# Pehle se mojood usernames
current_users = ['nimra', 'aiman', 'kainat', 'sunny', 'shan', 'anna']

# Naye usernames jo user enter kar raha hai
new_users = ['alian', 'ali', 'asad', 'mann', 'salah', 'chanda']

# Current users ko lower case me convert kar ke store karna (case insensitive check ke liye)
current_users_lower = [user.lower() for user in current_users]

# Loop new_users ke liye
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, '{new_user}' username already liya gaya hai, naya username choose karein.")
    else:
        print(f"'{new_user}' username available hai!")
