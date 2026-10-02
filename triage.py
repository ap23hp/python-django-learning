from category import CATEGORIES            # "from file import thing", lowercase, no .py

def triage(text):                            # "def" instead of "function"
    text = text.lower()                      #  .lower(), and save the result back into text

    for category in CATEGORIES:              #  "for", indented inside the function
        for keyword in category["keywords"]: #  get the keyword list out of the dictionary
            if keyword in text:              #  colon at the end; is the KEYWORD in the TEXT?
                return category["name"]      #  square brackets, not a dot

    return None                              #  after BOTH loops, only reached if nothing matched

print(triage("Water LEAK in the hallway"))         #  print() shows the returned value
print(triage("How many years left on my lease"))
print(triage("Can I keep a dog?"))