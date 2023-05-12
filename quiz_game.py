print("Hello , Welcome the Quiz_Monkey");

playing  = input ("Do you want to play? ");

questions = [
    "What does CPU stand for? ",
    "What does GPU stand for? ",
    "What does RAM stand for? ",
    "What does PSU stand for? ",
]

answers = [
    "Central processing Unit",
    "Graphics processing Unit",
    "Random access memory",
    "Power supply unit"
]

def conduct_quiz(questions,answers):
    score = 0
    total_questions = len(questions)

    for i in range(total_questions):
        print(f"\nQuestion {i+1} : {questions[i]}")
        user_answer = input("Your answer: ")

        if user_answer.lower() == answers[i].lower():
            print("Correnct answer!")
            score += 1
        else:
            print(f"Incorrect answer ! The correct answer is {answers[i]}")

    print("\nQuiz completed")
    print(f"Your score: {score} for total {total_questions} questions")

if playing.lower()  != "yes":
    quit()
else:
    conduct_quiz(questions,answers)