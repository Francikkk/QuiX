import art
from Quiz import Quiz
from replit import clear
from UI import QuizInterface

quiz = Quiz()
quiz.shuffle_questions()
quiz_ui = QuizInterface(quiz)

while quiz.still_has_questions():
    clear()
    print(art.logo)
    current_question = quiz.next_question()
    current_question.ask_question()
    #user_answer = input("Enter 'True' or 'False': ").capitalize()
    #quiz.check_answer(user_answer, current_question)
    input("\nPress any key to continue...")
clear()
quiz.final_score()
