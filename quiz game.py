# 5. Quiz Game
# Create a basic quiz game that:
# Contains a list of 5–10 questions stored in a dictionary (or list of dicts).
# Asks the user each question and records their answers.
# At the end, displays:
# The user’s score (e.g., 7/10)
# Correct answers for any questions they got wrong

# List of quiz questions and answers
quiz = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What planet is known as the Red Planet?", "answer": "mars"},
    {"question": "Who wrote 'Romeo and Juliet'?", "answer": "shakespeare"},
    {"question": "What is the largest mammal in the world?", "answer": "blue whale"},
    {"question": "What is the boiling point of water in Celsius?", "answer": "100"},
    {"question": "Which element has the chemical symbol 'O'?", "answer": "oxygen"},
    {"question": "What is 9 * 8?", "answer": "72"},
    {"question": "What is the currency of Japan?", "answer": "yen"},
    {"question": "In which continent is the Amazon Rainforest?", "answer": "south america"},
    {"question": "Who painted the Mona Lisa?", "answer": "da vinci"}
]

score = 0
wrong_answers = []

print("🎯 Welcome to the Quiz Game!")
print("Answer the following questions:\n")

# Ask each question
for i, q in enumerate(quiz, 1):
    user_answer = input(f"{i}. {q['question']} ").strip().lower()
    correct_answer = q['answer']
    if user_answer == correct_answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong. The correct answer will be shown at the end.\n")
        wrong_answers.append({"question": q['question'], "your_answer": user_answer, "correct_answer": correct_answer})

# Show final score
print(f"🏁 Quiz Complete! Your Score: {score}/{len(quiz)}")

# Show correct answers for wrong questions
if wrong_answers:
    print("\n📘 Review of Incorrect Answers:")
    for wa in wrong_answers:
        print(f"- Q: {wa['question']}")
        print(f"  Your Answer: {wa['your_answer']}")
        print(f"  Correct Answer: {wa['correct_answer']}\n")
else:
    print("🎉 Perfect score! Well done!")