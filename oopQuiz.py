class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    

class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_bank = question_bank
        
    def still_has_questions(self):
        return self.question_number < len(self.question_bank)
    
    def next_question(self):
        current_question = self.question_bank[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(current_question.answer, user_answer)
    
    def check_answer(self, correct_answer, user_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")    
    
def main():
    question_data = [
    {"text": "dejo is the goat", "answer": "True"},
    {"text": "Amira is beautiful", "answer": "True"},
    {"text": "dejo is not the goat", "answer": "False"},
    {"text": "dejo is sexy", "answer": "True"},
    ]

    question_bank = []
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        question_new = Question(question_text, question_answer)
        question_bank.append(question_new)


        quiz = QuizBrain(question_bank)
    
    while quiz.still_has_questions():
        quiz.next_question()
    
    print("You've completed the quiz!")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")

if __name__ == "__main__":
    main()
