import random
import operator

def random_problem():
    operators = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
        '^' : operator.pow
    }

    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operation = random.choice(list(operators.keys()))

    answer = round(operators.operation(number1, number2), 3)
    print(f"What is {number1} {operation} {number2}?")

    return answer

def error_handling():
    while True:
        try:
            return float(input("Please enter a valid number: "))
        except ValueError:
            print("Invalid input. Try again.")

def ask_question():
    answer = random_problem()
    try:
        guess = float(input("Enter your answer: "))
    except ValueError:
        guess = error_handling()

    return guess == answer

def game():
    score = 0
    while True:
        if ask_question():
            score += 1
            print("Correct!\n")
        else:
            print("Incorrect!")
            break

    print(f"\nGame Over\nYour score is {score}")

game()
