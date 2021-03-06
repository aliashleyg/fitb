blanks = ['_______1________', '_______2________', '_______3________', '_______4________', '_______5________', '_______6________']
easy_quiz = "The programming language, " + blanks[0] + ", was named after a television show called Monty Python's Flying Circus. In Python, a " + blanks[1] + " loop makes the program run while a condition is true." + blanks[2] + " is a valuable skill to learn to find errors (or bugs) in code." + blanks[3] + " is a command that ends the program and returns the value.Python allows you to store a value in a " + blanks[4] + ".This paragraph of code inside quotation marks is called a " + blanks[5] + "."
easy_answer = ['Python', 'while', 'Debugging', 'Return', 'variable','string']
medium_quiz = blanks[0] + " is a method where the solution to a problem depends on solutions to smaller instances of the same problem. Python is considered by most to be a(n) " + blanks[1] + " oriented programming language. A " + blanks[2] + " is a textual region of a Python program where a namespace is directly accessible. While some objects in Python are " + blanks[3] + " meaning, they can be changed, others are " + blanks[4] + " which means they return new objects. A " + blanks[5] + " is an unordered set of key: value pairs, with the requirement that the keys are unique."
medium_answer = ['Recursion','object','scope','mutable','immutable','dictionary']
hard_quiz = blanks[0] + " is a programming technique in which computer programs have the ability to treat programs as their data. A shorthand version of function wrapping is called a Python " +blanks[1] + ". The Python " + blanks[2] + " " + blanks[3] + ", also known in the community as PEP 3118, is a framework in which Python objects can expose raw byte arrays to other Python objects. " + blanks[4] + " are computer program components that generalize subroutines for nonpreemptive multitasking. Anonymous functions are defined using the " + blanks[5] + "keyword."
hard_answer = ['Metaprogramming','decorator','buffer', 'protocol','Coroutines','lambda']         

#confirms user input is valid and returns appropriate value for quiz assignment
def choose_level(user_difficulty_choice):
    valid_difficulty_choice = ['easy','medium','hard']
    if user_difficulty_choice in valid_difficulty_choice:
        return user_difficulty_choice
    else:
        while user_difficulty_choice not in valid_difficulty_choice:
            user_difficulty_choice = raw_input("Please select the level of difficulty for your quiz: 'easy', 'medium', or 'hard'")
    return user_difficulty_choice          

#assigns appropriate quiz from user input
def assign_quiz(user_difficulty_assignment):
    if user_difficulty_assignment == 'easy':
        return easy_quiz
    elif user_difficulty_assignment == 'medium':
        return medium_quiz
    else:
        return hard_quiz

#assigns appropriate answers from user input
def assign_answer(user_difficulty_assignment):
    if user_difficulty_assignment == 'easy':
        return easy_answer
    elif user_difficulty_assignment == 'medium':
        return medium_answer
    else:
        return hard_answer

def quiz (chosen_quiz, chosen_answers, blanks):
    answer_number = 1
    question_number = 0
    print chosen_quiz
    while answer_number <= len(chosen_answers):
        user_answer = raw_input("What is the answer to " + str(answer_number) + "?")
        if user_answer == chosen_answers[question_number]:
            chosen_quiz = chosen_quiz.replace(blanks[question_number],chosen_answers[question_number])
            answer_number += 1
            question_number +=1
            print chosen_quiz
    print "Wow! Congratulations! You passed the quiz! Thanks for playing. Goodbye."

user_difficulty_choice = raw_input("Please select the level of difficulty for your quiz: 'easy', 'medium', or 'hard'")
user_difficulty_assignment = choose_level(user_difficulty_choice)
chosen_quiz = assign_quiz(user_difficulty_assignment)
chosen_answers = assign_answer(user_difficulty_assignment)
print quiz(chosen_quiz, chosen_answers, blanks)