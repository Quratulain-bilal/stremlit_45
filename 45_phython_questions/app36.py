# T-Shirt: Write a function called make_shirt() that accepts a size 
# and the text of a message that should be printed on the shirt. The function should print a 
# sentence summarizing the size of the shirt and the me
# ssage printed on it. Call the function.# Function Definition
def make_shirt(size, message):
    """
    This function accepts the size of a shirt and the text of a message
    that should be printed on the shirt. It prints a sentence summarizing
    the size and the message.
    """
    print(f"A {size}-sized shirt will be printed with the message: '{message}'.")

# Calling the Function with Example Inputs
print("Example 1:")
make_shirt('Large', 'Python is Fun!')

print("\nExample 2:")
make_shirt('Medium', 'I Love Coding')

print("\nExample 3:")
make_shirt('Small', 'Stay Curious')