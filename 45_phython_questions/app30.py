# Hello Admin: Make a array of five or more usernames, including the 
# name 'admin'. Imagine you are writing code that will print a 
# greeting to each user after they log in to a website. Loop through the array, 
# and print a greeting to each user:
# • If the username is 'admin', print a special greeting, such as Hello admin, 
# would you like to see a status report?

# • Otherwise, print a generic greeting, such as Hello Eric, thank you 
# for logging in again.
user_admin =['nimra','aiman','kainat','sunny','shan','anna']

for user in user_admin:
    if user .lower() == 'admin':
        print(" Hello admin would you like to see a status report?")
    else:
        print(f" Hello {user}, thank you for logging in again.")

