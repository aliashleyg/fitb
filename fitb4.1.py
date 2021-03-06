blanks = [
    '_______1________',
    '_______2________',
    '_______3________',
    '_______4________',
    '_______5________',
    '_______6________'
    ]

easy_quiz = ("The programming language, " + blanks[0] + ", was named after a"
            " television show called Monty Python's Flying Circus."
            " In Python, a " + blanks[1] + " loop makes the program run"
            " while a condition is true. " + blanks[2] + " is a valuable"
            " skill to learn to find errors (or bugs) in code. "
            " " + blanks[3] + " is a command that ends the program and"
            " returns the value.Python allows you to store a value in a"
            " " + blanks[4] + ". This paragraph of code inside"
            " quotation marks is called a " + blanks[5] + ".")

medium_quiz = (blanks[0] + " is a method where the solution to a problem"
              " depends on solutions to smaller instances of the same"
              " problem. Python is considered by most to be a(n)"
              " " + blanks[1] + " oriented programming language. A"
              " " + blanks[2] + " is a textual region of a Python program"
              " where a namespace is directly accessible. While some objects"
              " in Python are " + blanks[3] + " meaning, they can be"
              " changed, others are " + blanks[4] + " which means they"
              " return new objects. A " + blanks[5] + " is an unordered set"
              " of key: value pairs, with the requirement that the keys"
              " are unique.")

hard_quiz = (blanks[0] + " is a programming technique in which computer"
            " programs have the ability to treat programs as their data."
            " A shorthand version of function wrapping is called a Python"
            " " + blanks[1] + ". The Python " + blanks[2] + ""
            " " + blanks[3] + ", also known in the community as PEP 3118,"
            " is a framework in which Python objects can expose raw byte"
            " arrays to other Python objects. " + blanks[4] + " are"
            " computer program components that generalize subroutines for"
            " nonpreemptive multitasking. Anonymous functions are defined"
            " using the " + blanks[5] + " keyword.")

easy_answer = [
  'Python',
  'while',
  'Debugging',
  'Return',
  'variable',
  'string'
  ]

medium_answer = [
  'Recursion',
  'object',
  'scope',
  'mutable',
  'immutable',
  'dictionary'
  ]

hard_answer = [
  'Metaprogramming',
  'decorator',
  'buffer',
  'protocol',
  'Coroutines',
  'lambda'
  ]

"""
check if difficulty choice is a valid response

Args:
    user_difficulty_choice: raw input from user asking for level of
    difficulty.
Behavior:
    Confirms user's input to a list of valid inputs.
Returns:
    If input is valid, returns user_difficulty_choice;
    If input is invalid, promps user to reenter answer.
"""
def choose_level(user_difficulty_choice):
    valid_difficulty_choice = ['easy', 'medium', 'hard']
    if user_difficulty_choice.lower() in valid_difficulty_choice:
        return user_difficulty_choice
    else:
        while user_difficulty_choice not in valid_difficulty_choice:
            user_difficulty_choice = raw_input(
              "Please select the level of difficulty for your quiz:"
              " 'easy', 'medium', or 'hard'")
    return user_difficulty_choice

"""assign appropriate quiz string

  Args:
      user_difficulty_assignment: the result of user's difficulty
      choice, after being checked as a valid choice.
  Behavior:
      Evaluates which quiz will take the value of 'chosen quiz'
  Returns:
      Returns the string of the appropriate quiz: easy, medium,
      or hard.
"""


def assign_quiz(user_difficulty_assignment):
    if user_difficulty_assignment == 'easy':
        return easy_quiz
    elif user_difficulty_assignment == 'medium':
        return medium_quiz
    else:
        return hard_quiz

"""assign appropriate answer list

  Args:
      user_difficulty_assignment: the result of user's difficulty
      choice, after being checked as a valid choice.
  Behavior:
      Evaluates which answer list will take the value of
      'chosen answer'
  Returns:
      Returns the answer list for the appropriate level: easy, medium,
      or hard.
"""


def assign_answer(user_difficulty_assignment):
    if user_difficulty_assignment == 'easy':
        return easy_answer
    elif user_difficulty_assignment == 'medium':
        return medium_answer
    else:
        return hard_answer

"""determine number of misses, based on user input

  Args:
      number_of_strikes: raw input from user asking for number of
      misses.
  Behavior:
      Determines if user entered an integer between 3 and 99
  Returns:
      Returns the string number_of_strikes as integer if true;
      If not, prompts user to reenter.
"""

def strikes(number_of_strikes):
    min_val = 2
    max_val = 99
    while number_of_strikes:
        if number_of_strikes.isdigit():
            if int(number_of_strikes) > min_val and int(number_of_strikes) < max_val:
                return int(number_of_strikes)
            else:
                print ("Please choose a number between 3 and 99 to continue. "
                      "Now let's try that again.")
                number_of_strikes = raw_input(
                      "How many strikes do you want until your game is over?")
        else:
            print ("Please choose a number between 3 and 99 to continue. "
                  "Now let's try that again.")
            number_of_strikes = raw_input(
                      "How many strikes do you want until your game is over?")

"""outputs new quiz string with correct answer

  Args:
      chosen_quiz: assigned from user input
      blanks: list with blanks to be replaced with correct answers
      question_number: the iterator through list
      chosen_answers: assigned from user input
  Behavior:
      takes chosen_quiz, replaces the blank that was answered with the correct
      answer
  Returns:
     updated quiz with correct answer filled in blank
"""

def correct_answer(chosen_quiz,blanks,question_number,chosen_answers):
  chosen_quiz = chosen_quiz.replace(
  blanks[question_number], chosen_answers[question_number])
  return chosen_quiz

"""increments through list after correct answer

  Args:
      user_answer: user input to presented question
      question_number: the iterator through list
      chosen_answers: assigned from user input   
  Behavior:
      takes question number; increments it by one
  Returns:
     returns incremented question number
"""

def question_incrementer(user_answer, chosen_answers, question_number):
    question_number = question_number + 1
    return question_number

"""returns correct message at end of game

  Args:
      total_strikes: the number of misses a user chose for him/herself
  Behavior:
      returns final statement at end of quiz
  Returns:
     returns congratulatory message if user answered all questions right;
     returns game over message if user used up all of their strikes
"""

def end_game(total_strikes):
  if total_strikes == None:
    return "I'm sorry. You have reached your maximum number of strikes. Please come back and try again soon. Goodbye."
  else:
    return "Congratulations! You answered all questions correctly. Thanks for playing. Goodbye."

"""tracks number of strikes a user has incurred

  Args:
      total_strikes: the number of misses a user chose for him/herself
  Behavior:
      print statement telling user how many strikes s/he has left
  Returns:
     returns total_strikes back
"""

def wrong_answer(total_strikes):
  if total_strikes > 0:
    print (
          "Whoops! Wrong answer. But don't worry, you still "
          "have " + str(total_strikes) + " number of tries "
          "left.")
    return total_strikes
  else:
    return None

"""the main function that loops through quiz questions

  Args:
      chosen_answers: assigned from user input 
      chosen_answers: assigned from user input  
      total_strikes: the number of misses a user chose for him/herself
  Behavior:
      while question number is < than the number of answers in the chosen_answer list,
      user is asked for the answer to the current question. If the answer is correct,
      the correct_answer function is called; if the answer is wrong,
      the wrong_answer function is called 
  Returns:
     returns the result of the end_game function, which is a message based on the
     outcome of the game. 
"""  

def run_quiz(chosen_answers,chosen_quiz, total_strikes):
  question_number = 0
  total_strikes = int(total_strikes)
  print chosen_quiz
  while question_number < len(chosen_answers) and total_strikes > 0:
    user_answer = raw_input(
      "What is the answer to " + str(question_number + 1) + "?")
    if user_answer == chosen_answers[question_number]:
      chosen_quiz = correct_answer(chosen_quiz,blanks,question_number,chosen_answers)
      question_number = question_incrementer(user_answer, chosen_answers, question_number)
      print chosen_quiz
    else:
      total_strikes = total_strikes - 1
      total_strikes = wrong_answer(total_strikes)
  return end_game(total_strikes)

    

user_difficulty_choice = raw_input(
    "Please select the level of difficulty for your quiz: 'easy', 'medium', "
    "or 'hard'")
user_difficulty_assignment = choose_level(user_difficulty_choice)
chosen_quiz = assign_quiz(user_difficulty_assignment)
chosen_answers = assign_answer(user_difficulty_assignment)
number_of_strikes = raw_input(
    "How many strikes do you want until your game is over?")
total_strikes = strikes(number_of_strikes)
print run_quiz(chosen_answers, chosen_quiz, number_of_strikes)

