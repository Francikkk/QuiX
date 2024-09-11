class Question:
    def __init__(self, q_question, q_answer):
        self.question = q_question
        self.answer = q_answer
        
    def ask_question(self):
        print(self.question)

    def check_answer(self, user_answer):
        while user_answer not in ["True", "False"]:
            user_answer = input("\nInvalid entry retry:\n 'True' or 'False': ").capitalize()
        if user_answer in ["True", "False"]:
            return user_answer == self.answer
        
