# Magicians: Make a array of magician’s names. Pass the array to a function called show_magicians(),
# which prints the name of each magician in the array.


def show_magicians(magicians):
   for magician in magicians:  # Har magician ka naam print karega
    print(magician)

magicians_list = ["Harry Houdini", "David Blaine", "Dynamo", "Criss Angel"]

show_magicians(magicians_list)