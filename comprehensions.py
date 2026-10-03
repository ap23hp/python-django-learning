class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def describe(self):
        return f"{self.name} - £{self.price:.2f}"


MENU = [
    MenuItem("Latte", 2.80, "drink"),
    MenuItem("Tea", 1.90, "drink"),
    MenuItem("Croissant", 2.50, "food"),
    MenuItem("Sandwich", 4.75, "food"),
    MenuItem("Cake", 3.20, "food"),
]

# 1. All item names
names = [item.name for item in MENU]
print(names)

# 2. Names of food items only (the "if" filters)
food = [item.name for item in MENU if item.category == "food"]
print(food)

# 3. Every price with 10% added, rounded to 2 decimal places
with_tax = [round(item.price * 1.1, 2) for item in MENU]
print(with_tax)

# 4. A dictionary of name: category (curly braces, key: value)
categories = {item.name: item.category for item in MENU}
print(categories)

# 5. Total price of all drinks
drinks_total = sum(item.price for item in MENU if item.category == "drink")
print(f"£{drinks_total:.2f}")