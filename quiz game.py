import random

# Define quiz questions and answer choices as a dictionary
quiz_questions = {
    "What is the capital of France?": ["a) London", "b) Berlin", "c) Paris", "d) Madrid"],
    "What is the largest planet in our solar system?": ["a) Earth", "b) Mars", "c) Venus", "d) Jupiter"],
    "How many continents are there on Earth?": ["a) 4", "b) 5", "c) 6", "d) 7"],
    "Which gas do plants absorb from the atmosphere?": ["a) Oxygen", "b) Carbon dioxide", "c) Nitrogen", "d) Hydrogen"],
    "Who wrote the play 'Romeo and Juliet'?": ["a) Charles Dickens", "b) Mark Twain", "c) William Shakespeare", "d) Jane Austen"],
}

# Define correct answers
correct_answers = {
    "What is the capital of France?": "c",
    "What is the largest planet in our solar system?": "d",
    "How many continents are there on Earth?": "d",
    "Which gas do plants absorb from the atmosphere?": "b",
    "Who wrote the play 'Romeo and Juliet'?": "c",
}

def quiz_game():
    print("Welcome to the Multiple-Choice Quiz Game!")
    print("You will be asked multiple-choice questions.")
    print("Select the letter (a, b, c, or d) corresponding to your answer.")
    print("Enter 'q' to quit at any time.")

    score = 0

    # Shuffle the questions to make the quiz more engaging
    questions = list(quiz_questions.keys())
    random.shuffle(questions)

    for question in questions:
        print("\nQuestion:", question)
        for choice in quiz_questions[question]:
            print(choice)

        user_answer = input("Your Answer: ").lower()

        if user_answer == 'q':
            break

        if user_answer == correct_answers[question]:
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is: {correct_answers[question]}")

    print("\nQuiz Completed!")
    print("Your Score:", score, "/", len(quiz_questions))

def main():
    while True:
        quiz_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
