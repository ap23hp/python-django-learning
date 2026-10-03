class Category:
    def __init__(self, name, keywords):
        self.name = name
        self.keywords = keywords

    def matches(self, text):
        text = text.lower()
        for word in self.keywords:
            if word in text:
                return True
        return False


CATEGORIES = [
    Category("Costs and charges", ["rent", "charge", "fees"]),
    Category("Building management", ["leak", "repair", "damp"]),
    Category("Lease extension", ["extend", "extension", "years left"]),
    Category("Pets", ["dog", "cat", "pet"]),
]


def triage(text):
    for category in CATEGORIES:
        if category.matches(text):
            return category.name
    return None


print(triage("Water LEAK in the hallway"))
print(triage("How many years left on my lease"))
print(triage("Can I keep a dog?"))
print(triage("My neighbour is noisy"))