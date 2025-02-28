
# • Print your array in its original order.

# • Print your array in alphabetical order without modifying the actual list.

# • Show that your array is still in its original order by printing it.

# • Print your array in reverse alphabetical order without changing the order of the original list.

# • Show that your array is still in its original order by printing it again.

# • Reverse the order of your list. Print the array to show that its order has changed.

# • Reverse the order of your list again. Print the list to show it’s back to its original order.

# • Sort your array so it’s stored in alphabetical order. Print the array to show that its order has been changed.

# • Sort to change your array so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.



# Step 1: Original list of places
places = ["lahore", "sakkhar", "islamabad", "lahore", "karachi"]
print("Original list:", places)

# Step 2: Alphabetical order (without modifying original list)
print("Alphabetical order:", sorted(places))

# Step 3: Checking original order is still same
print("Still original order:", places)

# Step 4: Reverse alphabetical order (without modifying original list)
print("Reverse alphabetical order:", sorted(places, reverse=True))

# Step 5: Checking original order is still same
print("Still original order:", places)

# Step 6: Reverse the list order (modifies the list)
places.reverse()
print("Reversed list:", places)

# Step 7: Reverse again to bring it back to original order
places.reverse()
print("Back to original order:", places)

# Step 8: Sort alphabetically (modifies the list)
places.sort()
print("Alphabetically sorted list:", places)

# Step 9: Sort in reverse alphabetical order (modifies the list)
places.sort(reverse=True)
print("Reverse alphabetically sorted list:", places)
