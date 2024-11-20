questions = [
    ["What does CPU stand for?", ["Central Processing Unit", "Central Program Unit", "Computer Personal Unit", "Central Processor Unit"], 1],
    ["Which language is used for data analysis?", ["Java", "Python", "HTML", "CSS"], 2],
    ["What is the main purpose of a database?", ["Data Storage", "Data Analysis", "Data Processing", "Data Visualization"], 1],
    ["What does AI stand for?", ["Artificial Intelligence", "Algorithmic Interface", "Automated Information", "Artificial Interface"], 1],
    ["What is cleaned and structured data called?", ["Raw Data", "Structured Data", "Processed Data", "Unstructured Data"], 3]
]

def start_quiz():
    score = 0
    print("Welcome to the Quiz!\n")

    for q in questions:
        print(q[0])
        for i, option in enumerate(q[1]):
            print(f"{i + 1}. {option}")

        try:
            answer = int(input("Select your answer (1-4): "))
            if answer == q[2]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {q[1][q[2] - 1]}\n")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.\n")

    print(f"Your final score is {score} out of {len(questions)}.")

start_quiz()
