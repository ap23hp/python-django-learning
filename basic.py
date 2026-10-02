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

name = input("What's your name? ")
print(f"Hi {name}")
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

