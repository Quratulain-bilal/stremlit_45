def make_sandwich(*items):
    """Sandwich ke items accept karne aur summary print karne wala function"""
    print("\nMaking a sandwich with the following ingredients:")
    for item in items:
        print(f"- {item}")
    print("Enjoy your sandwich!")

# Function ko different number of arguments ke sath call karna
make_sandwich("Cheese", "Tomato", "Lettuce")
make_sandwich("Chicken", "Mayo")
make_sandwich("Egg", "Bacon", "Avocado", "Mustard")
