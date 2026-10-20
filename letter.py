def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi",]
    for name in names:
        print(write_letter(name, "Princess Peach"))
    invited = ", ".join(names)
    print(f"Princess Peach invited: {invited}")
    


def write_letter(reciever, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Dear {reciever},

        You are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """


main()