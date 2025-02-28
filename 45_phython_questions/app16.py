# Program by Quratulain Shah
# Date: 2/18/2025
# This program demonstrates how to manage a guest list, handle changes, 
# and expand the list when more space becomes available.

# Initial guest list
guest_name = ['sara', 'amina', 'zainab', 'mahira', 'hiba']

# Sending initial invitations
print("Initial Invitations:")
for i in guest_name:
    print(f"Dear {i},\nI would be honored to have you join me for dinner. Looking forward to an inspiring evening!\n")

# Changing Guest List: One guest can't make it
unable_to_attend = "hiba"
print(f"Unfortunately, {unable_to_attend} can't make it to dinner.\n")

# Replacing the guest who can't attend
new_guest = "noor"
guest_name[guest_name.index(unable_to_attend)] = new_guest  # Replace 'hiba' with 'noor'

# Sending updated invitations
print("Updated Invitations:")
for i in guest_name:
    print(f"Dear {i},\nI would be honored to have you join me for dinner. Looking forward to an inspiring evening!\n")

# More Guests: Found a bigger dinner table
print("Great news! I found a bigger dinner table, so more guests will be invited.\n")

# Adding one new guest to the beginning of the list
guest_name.insert(0, "fariha")

# Adding one new guest to the middle of the list
middle_index = len(guest_name) // 2  # Find the middle index
guest_name.insert(middle_index, "tania")

# Adding one new guest to the end of the list
guest_name.append("sadia")

# Sending new invitations to the expanded list
print("New Invitations with Additional Guests:")
for i in guest_name:
    print(f"Dear {i},\nI would be honored to have you join me for dinner. Looking forward to an inspiring evening!\n")