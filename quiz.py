class Quiz:
    def __init__(self):
        self.questions = {
            "What function is used to print output in Python?": "print",
            "Which data type is used to store decimal numbers?": "float",
            "What keyword is used to define a function in Python?": "def",
            "What type of loop runs while a condition is True?": "while",
            "What is a collection of key-value pairs in Python called?": "dictionary",
            "What data structure uses Last In First Out (LIFO)?": "stack",
            "What is the name of the data structure that stores elements in First In First Out (FIFO) order?": "queue",
            "How do you create an array in Python?": "array",
            "What is the default starting index for arrays and lists in Python?": "0",
            "How do you define a class in Python?": "class"
        }

    def start_quiz(self):
        print("\nLet's test your knowledge! Answer the following questions:\n")
        score = 0
        for question, answer in self.questions.items():
            user_answer = input(f"{question} ").strip().lower()
            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {answer}.")
        print(f"\nYour final score: {score}/{len(self.questions)}")
        input("Press Enter to continue...\n")
