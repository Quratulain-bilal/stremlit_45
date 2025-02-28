# Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-else chain.
# • If the alien is green, print a message that the player earned 5 points.

# • If the alien is yellow, print a message that the player earned 10 points.

# • If the alien is red, print a message that the player earned 15 points.

# • Write three versions of this program, making sure each message is printed for the appropriate color alien.

alien_color="green"
if alien_color =="green":
    print("that the player earned 5 points.")
elif alien_color =="yellow":
  print("the player earned 10 points.")
else:
    print("the player earned 15 points.")
    
    
    #version 2
    
    alien_color = "yellow"  # Alien ka color yellow set kiya

if alien_color == "green":
    print("Player ne alien shoot kiya! 5 points mile.") 
elif alien_color == "yellow":
    print("Player ne alien shoot kiya! 10 points mile.") 
else:
    print("Player ne alien shoot kiya! 15 points mile.") 
    
    #version3
    alien_color = "red"  # Alien ka color red set kiya

if alien_color == "green":
    print("Player ne alien shoot kiya! 5 points mile.") 
elif alien_color == "yellow":
    print("Player ne alien shoot kiya! 10 points mile.") 
else:
    print("Player ne alien shoot kiya! 15 points mile.") 

