class QuizBrains:
    
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

    def serve_questions(self):
        self.score = 0
        while self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            reply = input(f"Q.{self.question_number} : {current_question.question} (True/False): ")
            if reply.lower() == current_question.correct_answer.lower():
                print("You got it right!")
                print(f"The correct answer was : {current_question.correct_answer}")
                self.score += 1
                print(f"Your score is : {self.score}/{self.question_number}") 
            else:
                print("You got it wrong!")
                print(f"The correct answer was : {current_question.correct_answer}")
                print(f"Your score is : {self.score}/{self.question_number}") 
            print('\n')

    def checkout_final_score(self):
        print("You've completed the quiz")
        print(f"Your final score is {self.score}/{self.question_number}")        

