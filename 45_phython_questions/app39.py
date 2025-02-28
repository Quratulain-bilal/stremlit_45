# City Names: Write a function called city_country() 
# that takes in the name of a city and its country. 
# The function should return a string formatted like this:

# "Lahore, Pakistan"

# Call your function with at least three city-country pairs, 
# and print the value that’s returned.
def city_country(city, country):
    return f"{city}, {country}"  # Formatted string return kar raha hai

# Function ko call karna aur return value ko print karna
print(city_country("Lahore", "Pakistan"))
print(city_country("Tokyo", "Japan"))
print(city_country("New York", "USA"))
