# Great Magicians: Start with a copy of your program from Exercise 
# 39. Write a function called make_great() that modifies the array of magicians 
# by adding the phrase the Great to each magician’s name.
# Call show_magicians() to see that the list has actually been modified.
def show_magicians(magicians):
    """Magicians ke naam display karne wala function"""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Magicians ke naam modify karne wala function jo 'the Great' add karega"""
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great"

# Magicians ki list
magicians = ["Harry Houdini", "David Blaine", "Dynamo"]

# Magicians ke naam modify karna
make_great(magicians)

# Updated list ko display karna
show_magicians(magicians)
