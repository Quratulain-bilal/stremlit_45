# Album: Write a function called make_album() 
# that builds a Object describing a music album. The function should take in an artist name and 
# an album title, and it should return a Object containing these two pieces of information. 
# Use the function to make three dictionaries representing different albums. Print each return 
# value to show that Objects are storing the album information correctly. Add an optional parameter
# to make_album() that allows you to store the 
# number of tracks on an album. If the calling line includes a value for the number of tracks, 
# add that value to the album’s
# Object. Make at least 
# one new function call that includes the number of tracks on an album.

# Function to create album dictionary
def make_album(artist, title, tracks=None):  # Optional parameter tracks
    album = {
        "artist": artist,
        "title": title
    }
    if tracks:  # Agar tracks provided hain to dictionary mein add karo
        album["tracks"] = tracks
    return album

# Function ko different albums ke liye call karna
album1 = make_album("Atif Aslam", "Doorie")
album2 = make_album("Taylor Swift", "1989")
album3 = make_album("Coldplay", "Parachutes", tracks=10)  # Tracks include karna

# Albums ko print karna
print(album1)
print(album2)
print(album3)
