
class QuizBrain:
    def __init__(self,q_list):
        self.question_no=0
        self.question_list=q_list
        self.score=0

    def check_answer(self,answer, correct_answer):
        if answer==correct_answer.lower():
            self.score+=1
            print("You are right")
        else:
            print("You are wrong")
            print(f"Correct answer is: {correct_answer}")
        print(f"Current score is: {self.score}/{self.question_no}")

    def still_has_question(self):
        return self.question_no < len(self.question_list)


    def next_question(self):
        question_now=self.question_list[self.question_no]
        self.question_no+=1
        answer=input(f"Q.{self.question_no}: {question_now.text} (True/False): ").lower()
        self.check_answer(answer,question_now.answer)
