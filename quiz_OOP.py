
from question_model import Question
from question_data import questions
from quiz_brains import QuizBrains

question_list = []
for i in questions: 
    query = i['question']
    response = i['correct_answer']
    question_object = Question(query, response)
    question_list.append(question_object)

quiz = QuizBrains(question_list)
quiz.serve_questions()
quiz.checkout_final_score()



