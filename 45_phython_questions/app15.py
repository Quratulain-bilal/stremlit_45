# Program by Quratulain Shah
# Date: 2/18/2025
# This program demonstrates how to create a guest list, send invitations, 
# handle changes in the guest list, and send updated invitations.

# Initial guest list
guests = ["Albert Einstein", "Leonardo da Vinci", "Nikola Tesla"]

# Sending initial invitations
print("Initial Invitations:")
for guest in guests:
    print(f"Dear {guest},\nI would be honored to have you join me for dinner. Looking forward to an inspiring evening!\n")

# Guest who can't make it
unable_to_attend = "Nikola Tesla"
print(f"Unfortunately, {unable_to_attend} can't make it to dinner.\n")

# Replacing the guest who can't attend
new_guest = "Isaac Newton"
guests[guests.index(unable_to_attend)] = new_guest  # Replace Tesla with Newton

# Sending updated invitations
print("Updated Invitations:")
for guest in guests:
    print(f"Dear {guest},\nI would be honored to have you join me for dinner. Looking forward to an inspiring evening!\n")