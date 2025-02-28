# Large Shirts: Modify the make_shirt() function so that shirts are large by default 
# with a message that reads I love TypeScript. Make a large shirt and a medium shirt with the default message, 
# and a shirt of any 
# size with a different message.

def make_shirt(size= "Large",message ="I love TypeScript"):
    print(f"Shirt Size: {size}, Message: '{message}'")
    
make_shirt()
make_shirt("medium")
make_shirt("Small", "Code like a Pro!")