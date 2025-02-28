# No Users: Add an if test to Exercise 28 to make sure the list of users is not empty.
# • If the list is empty, print the message We need to find some users!

# • Remove all of the usernames from your array, and make sure the correct message is printed.

user_admin =['aimo','nimra','sunny','shan','anna','admin']

user_admin.clear()
print (user_admin)
if user_admin == []:
    print("We need to find some users!")
else:
    for user in user_admin:
     print(f"Hello {user}, welcome back!")