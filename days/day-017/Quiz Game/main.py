from question_model import Question
from opentdb_data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_bank.append(Question(q["question"],q["correct_answer"]))


qb = QuizBrain(question_bank)
while qb.still_has_questions():
    qb.next_question()

print("You've Completed the Quiz")
print(f"Your final Score is : {qb.score}/{len(question_bank)}")