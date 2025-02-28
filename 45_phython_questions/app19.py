# Guest List: If you could invite anyone, living or deceased, to dinner, 
# who would you invite? Make a list that includes at least three people
# you’d like to invite to dinner. Then use your list to print 
# a message to each person, inviting them to dinner.

guest_name = ['Anna', 'Shan', 'Sunny', 'Ayesha', 'Aiman']

for i in guest_name:
    print(f"Dear {i},\nI would be honored to have you join me for dinner. Looking forward to an inspiring evening!\n")


# Changing Guest List: You just heard that one of your guests can’t make the dinner,
# so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

# • Start with your program from Exercise 14. Add a print statement at the end of your
# program stating the name of the guest who can’t make it.

# • Modify your list, replacing the name of the guest who can’t make it with the name
# of the new person you are inviting.

# • Print a second set of invitation messages, one for each person who is still in your list.

# Initial guest list
guests = ["Anna", "Shan", "Ayesha"]

# Guest who can't make it
unable_to_attend = "Ayesha"
print(f"Unfortunately, {unable_to_attend} can't make it to dinner.\n")

# Replacing the guest who can't attend
new_guest = "Zara"
guests[guests.index(unable_to_attend)] = new_guest  # Replace Ayesha with Zara

# Sending new invitations
for guest in guests:
    print(f"Dear {guest},\nI would be honored to have you join me for dinner. Looking forward to an inspiring evening!\n")


# More Guests: You just found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner.
# • Start with your program from Exercise 15. Add a print statement to the end of your 
# program informing people that you found a bigger dinner table.

# • Add one new guest to the beginning of your array.

# • Add one new guest to the middle of your array. • Use append() to add one new guest to the end of your 
# list. • Print a new set of invitation messages, one for each person in your list.

print("Great news! I found a bigger dinner table, so more guests will be invited.\n")

# Adding new guests
guests.insert(0, "Fariha")  # Add to beginning
guests.insert(len(guests) // 2, "Tania")  # Add to middle
guests.append("Sadia")  # Add to end

# Sending new invitations
for guest in guests:
    print(f"Dear {guest},\nI would be honored to have you join me for dinner. Looking forward to an inspiring evening!\n")


# Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 16. Add a new line that prints
# a message saying that you can invite only two people for dinner.

# • Remove guests from your list one at a time until only two names remain
# in your list. Each time you pop a name from your list, print a message
# to that person letting them know you’re sorry you can’t invite them to dinner.

# • Print a message to each of the two people still on your list, letting them know 
# they’re still invited.

# • Remove the last two names from your list, so you have an empty list. Print your list
# to make sure you actually have an empty list at the end of your program.


print("\nI just found out that the new dinner table won’t arrive in time, so I can invite only two guests.\n")

# Removing guests until only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Final two guests
print(f"\n{guests[0]}, you are still invited to dinner!")
print(f"{guests[1]}, you are still invited to dinner!\n")

# Removing the last two names
del guests[0]
del guests[0]

# Confirming the list is empty
print("Final guest list:", guests)  # Should print an empty list []


# Dinner Guests: Working with one of the programs from Exercises 14 through 18, 
# print a message indicating the number of people you are inviting to dinner.
print(f"\nTotal guests invited: {len(guests)}")
print("Final guest list:", guests)