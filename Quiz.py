import data
import question_module
import random
import html


class Quiz:
    def __init__(self,):
        self.question_number = 0
        self.score = 0
        self.questions = []
        for question in data.question_data:
            self.questions.append(question_module.Question(html.unescape(question["question"]), question["correct_answer"]))

    def next_question(self):
        self.question_number += 1
        q_text = html.unescape(self.questions[self.question_number - 1].question)
        print(f"Question {self.question_number})", end=" ")
        return f"Q.{self.question_number}: {q_text}"

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def check_answer(self, user_answer):
        question = self.questions[self.question_number - 1]
        if question.check_answer(user_answer):
            self.score += 1
            print("You got it right!")
            print(f"Your current score is: {self.score}/{self.question_number}")
            return True
        else:
            print("That's wrong.")
            print(f"Your current score is: {self.score}/{self.question_number}")
            return False

    def final_score(self):
        print("\n#############################")
        print(
            f"You've completed the quiz!\nYour final score was: {self.score}/{self.question_number}"
        )
        print("#############################")

    def shuffle_questions(self):
        random.shuffle(self.questions)
