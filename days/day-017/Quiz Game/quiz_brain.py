# TODO: asking the questions
# TODO: Checking if the answer was correct
# TODO: Checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def check_answer(self,u_ans,c_ans):
        if u_ans == c_ans:
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong")
        print(f"The correct answer was : {c_ans}")

    def next_question(self):
        c_que = self.questions_list[self.question_number].text
        c_ans = self.questions_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {c_que}, (True/False) ?: ")
        self.check_answer(user_answer,c_ans)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)