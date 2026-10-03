class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def describe(self):
        return f"{self.name} - £{self.price:.2f}"      # return the text, don't print it

    def is_cheap(self, limit=3):
        if self.price < limit:
            return True
        return False


MENU = [
    MenuItem("Latte", 2.80, "drink"),
    MenuItem("Tea", 1.90, "drink"),
    MenuItem("Croissant", 2.50, "food"),
    MenuItem("Sandwich", 4.75, "food"),
    MenuItem("Cake", 3.20, "food"),
]


def show_menu():
    number = 1
    for item in MENU:
        print(f"{number}. {item.describe()}")   # number + the text describe() returns
        number = number + 1

def find_item(name):
    name=name.lower()
    for menuitem in MENU:
        if(menuitem.name.lower()==name):
                return menuitem
    return None   
def cheap_items():
    result = []
    for item in MENU:
        if item.is_cheap():
            result.append(item.name)
    return result


print(cheap_items())   # ['Latte', 'Tea', 'Croissant']
show_menu()                                     #  outside the function
print(find_item("LATTE").describe())   # Latte - £2.80
print(find_item("pizza"))              # None
print(cheap_items())