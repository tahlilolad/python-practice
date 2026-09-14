contacts = {
    "alice": "555-0199",
    "bob": "555-0142",
    "tahlil": "555-0178",
}

print("Welcome to the contact book!")
while True:
 search_name = input("What is the name of the person you want to look up? ").strip().lower()
 if search_name in contacts:
    print(f"Phone number for {search_name.title()}: {contacts[search_name]}")
    break #Valid name found. Exit the loop.
 else:
    print("Sorry! That person is not in the book.")