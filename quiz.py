name = input("Welcome to my 2 question quiz! What is your name? ")
print("Hello " + name + "! Let's get started.")
score = 0

#Store each question and its correct answer together.
questions = [ 
    ("Question 1: What language are we using right now? ", "python"),
    ("Question 2: What does CPU stand for? ", "central processing unit"),
    ("Question 3: Does pineapple belong on pizza? ", "no"),
]

for question_text, correct_answer in questions:
    user_answer = input(question_text).strip().lower()
    if user_answer == correct_answer:
            print("Correct!")
            score += 1
    else:
            print(f"Wrong! the correct answer was: {correct_answer}")
print(f"Thanks for playing. Your final score is {score}/{len(questions)}")