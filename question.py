class Question:
    content_question = ''
    correct_answer = ''
    count_points = 0

    def __init__(self, content_question, correct_answer, count_point):
        self.content_question = content_question
        self.correct_answer = correct_answer
        self.count_points = count_point

    def __str__(self):
        return self.content_question
