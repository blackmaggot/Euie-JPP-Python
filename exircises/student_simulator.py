__author__ = 'WiktorMarchewka'
import random
import ocena


class QuestionsGenerator(object):
    answers_range = random.randint(1, 6)
    amount_of_questions = random.randint(3, 15)
    answer_dictionary = {}
    def setting_answers_dictionary(self):
        answers_list = {}
        for x in range(1, self.amount_of_questions):
            answers_list.update({
                x: random.randint(1, self.answers_range)
            })
        return answers_list

class StupidStudent(object):
     questions_instance = QuestionsGenerator()
     qa = questions_instance.setting_answers_dictionary()
     def student_answers(self):
        instance_of_questions = QuestionsGenerator()
        dumb_answers_list = {}
        answers_length = instance_of_questions.answers_range
        for x in range(1, instance_of_questions.amount_of_questions, 1):
            dumb_answers_list.update({x: random.randint(1, answers_length)})
        return dumb_answers_list

class Jury(object):
    def __init__(self):
        self.student_answers = StupidStudent().student_answers()
        self.correct_answers = QuestionsGenerator().setting_answers_dictionary()
        self.points_per_answer = {'correct': random.randint(1, 3), 'false': random.randint(-2, 0)}

    def student_amount_of_correct_answers(self):
        amount = 0
        for x in range(1, (len(self.correct_answers)+1)):
            if self.correct_answers[x] == self.student_answers[x]:
                amount += 1
        return amount
    def verdict_student_points(self):
        verdict = self.student_amount_of_correct_answers()*self.points_per_answer.get('correct')+((len(self.correct_answers)-self.student_amount_of_correct_answers())*self.points_per_answer.get('false'))
        return verdict
    def student_rating(self):
        rating = ocena.ocena(self.verdict_student_points(), (len(self.correct_answers)*self.points_per_answer.get('correct')))
        return rating
    def results_printer(self):
        print('----------------------------------------------------------------------------------------')
        print 'Amount of questions: ', len(self.correct_answers)
        print 'points for correct question: ', self.points_per_answer.get('correct')
        print 'points for false question: ', self.points_per_answer.get('false')
        print 'student correct answers: ', self.student_amount_of_correct_answers()
        print 'student false answers: ', len(self.correct_answers)-self.student_amount_of_correct_answers()
        print 'points gained by student: ', self.verdict_student_points()
        print 'Student rating: ', self.student_rating()
        print('----------------------------------------------------------------------------------------')




for x in range(1, random.randint(3, 15)):
    test = Jury()
    test.results_printer()
