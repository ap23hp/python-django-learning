print(5+3)
print("hello")

# This line is ignored by Python

name="Apra"
age = 30
price = 9.99
is_ready = True
nothing = None
#True and False take a capital letter.
#None is Python's null.
# Python names use snake_case
# f strings like js template litrals
print(f"My name is {name}")

#In Python, indentation is the braces."
text = "My Service Charge"
print(text.lower())
print(text.upper())
print("Charge" in text)
print(type(name))
print(type(age))
print(type(None))
if age>18:
    print("adult")
elif age >=13:
    print("teenager")
else:
    print("child")
print("always runn")

# name = input("What's your name? ")
# print(f"Hi {name}")
# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

keywords = ["rent", "charge", "fees"]

print(keywords[0])      # rent
print(len(keywords))    # 3 
keywords.append("levy") # append() instead of .push()
print(keywords)
# Lists work like JavaScript arrays
for word in keywords:
    print(word)

for i in range(3):
    print(i)   # 0, 1, 2 (the end number isn't included)

category = {
"name": "Costs and charges",
"keywords": ["rent", "charge", "fees"]
}

print(category["name"])
print(category.get("phone"))   # None, instead of crashing

# Keys need quotes. Writing {name: ...} without quotes is an error in Python.
# category["phone"] would crash with a KeyError if the key doesn't exist. .get() returns None instead.

for key, value in category.items():
    print(f"{key}: {value}")

    