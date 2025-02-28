# Program by Quratulain Shah
# Date: 2/18/2025
# This program demonstrates how to manage a guest list, handle changes, 
# expand the list, and shrink it when necessary.

# Initial guest list with new names
guest_name = ['Anna', 'Shan', 'Sunny', 'Nimra', 'Ayesha']

# Sending initial invitations to all guests
print("Initial Invitations:")
for i in guest_name:
    print(f"Dear {i},\nI would be honored to have you join me for dinner. Looking forward to an inspiring evening!\n")

# Changing Guest List: One guest can't make it
unable_to_attend = "Ayesha"
print(f"Unfortunately, {unable_to_attend} can't make it to dinner.\n")

# Replacing the guest who can't attend with a new guest
new_guest = "Zara"
guest_name[guest_name.index(unable_to_attend)] = new_guest  # Replace 'Ayesha' with 'Zara'

# Sending updated invitations after replacing the guest
print("Updated Invitations:")
for i in guest_name:
    print(f"Dear {i},\nI would be honored to have you join me for dinner. Looking forward to an inspiring evening!\n")

# More Guests: Found a bigger dinner table
print("Great news! I found a bigger dinner table, so more guests will be invited.\n")

# Adding one new guest to the beginning of the list
guest_name.insert(0, "Fariha")  # Add 'Fariha' at the start

# Adding one new guest to the middle of the list
middle_index = len(guest_name) // 2  # Find the middle index
guest_name.insert(middle_index, "Tania")  # Add 'Tania' in the middle

# Adding one new guest to the end of the list
guest_name.append("Sadia")  # Add 'Sadia' at the end

# Sending new invitations to the expanded guest list
print("New Invitations with Additional Guests:")
for i in guest_name:
    print(f"Dear {i},\nI would be honored to have you join me for dinner. Looking forward to an inspiring evening!\n")

# Shrinking Guest List: New dinner table won’t arrive in time
print("\nI just found out that the new dinner table won’t arrive in time, so I can invite only two guests.\n")

# Removing guests until only two remain
while len(guest_name) > 2:
    removed_guest = guest_name.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Final two guests
print(f"\n{guest_name[0]}, you are still invited to dinner!")
print(f"{guest_name[1]}, you are still invited to dinner!\n")

# Removing the last two names
del guest_name[0]
del guest_name[0]

# Confirming the list is empty
print("Final guest list:", guest_name)  # Should print an empty list []