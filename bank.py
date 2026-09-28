"""
CSI 1101: Home Federal Savings Bank Greeting Checker

Prompts the user for a greeting:
- Outputs $0 if the greeting starts with "hello".
- Outputs $20 if the greeting starts with "h" (and not "hello").
- Outputs $100 for any other greeting.

Ignores leading whitespace and treats inputs case-insensitively.
"""

def main():
    user_greeting = input().strip().lower()
    if user_greeting .startswith ('hello'):
        print("$0")
    elif user_greeting .startswith('h'):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
