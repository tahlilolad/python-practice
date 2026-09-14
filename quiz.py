name = input("Welcome to my 2 question quiz! What is your name? ")
print("Hello " + name + "! Let's get started.")
score = 0
answer1 = input("Question 1: What language are we using right now? ").strip().lower()
if answer1 == "python":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Python.")
answer2 = input("Question 2: What does CPU stand for? ").strip().lower()
if answer2 == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Central Processing Unit.")
print(f"Quiz complete! Your final score is: {score} /2")
print("Thanks for playing " + name + "!")
