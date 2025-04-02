import time
from lesson import Lesson
from quiz import Quiz

class ChatBot:
    def __init__(self):
        self.lesson = Lesson()
        self.quiz = Quiz()

    def start(self):
        print("Hello! I'm your Programming Tutor Bot. Let's learn Python together! 😊")
        time.sleep(1)

        while True:
            print("\nChoose a topic:")
            print("1. Introduction to Programming")
            print("2. Variables & Data Types")
            print("3. Conditional Statements")
            print("4. Loops")
            print("5. Functions")
            print("6. Lists & Dictionaries")
            print("7. Data Structures (Arrays, Stacks, Queues, Linked Lists)")
            print("8. Mini Projects")
            print("9. Take a Quiz")
            print("10. Exit")

            choice = input("Enter your choice (1-10): ")

            if choice == "1":
                self.lesson.introduction()
            elif choice == "2":
                self.lesson.variables()
            elif choice == "3":
                self.lesson.conditionals()
            elif choice == "4":
                self.lesson.loops()
            elif choice == "5":
                self.lesson.functions()
            elif choice == "6":
                self.lesson.lists_dictionaries()
            elif choice == "7":
                self.lesson.data_structures()
            elif choice == "8":
                self.lesson.mini_projects()
            elif choice == "9":
                self.quiz.start_quiz()
            elif choice == "10":
                print("Goodbye! Happy coding! 🚀")
                break
            else:
                print("Invalid choice. Please enter a number between 1-10.")
