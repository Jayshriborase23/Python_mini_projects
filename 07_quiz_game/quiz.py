print("===== Python Quiz Game =====")

score = 0

questions = [
    {
        "question": "Which language is used for AI/ML?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /*", "D. --"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. List", "D. Boolean"],
        "answer": "D"
    },
    {
        "question": "Which loop is commonly used when the number of iterations is known?",
        "options": ["A. for", "B. if", "C. try", "D. def"],
        "answer": "A"
    }
]

for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == question["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")
        print("Correct answer:", question["answer"])

print("\n===== Quiz Result =====")
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent! 🎉")
elif percentage >= 60:
    print("Good Job! 👍")
elif percentage >= 40:
    print("Keep Practicing! 💪")
else:
    print("Need More Practice! 📚")
