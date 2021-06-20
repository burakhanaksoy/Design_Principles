from abc import ABC, abstractmethod
import random


class SolveQuestionStrategy(ABC):
    @abstractmethod
    def process_questions(self, question_list): pass


class StartingFromFirstQuestionStrategy(SolveQuestionStrategy):
    def process_questions(self, question_list):
        """ 
        Returns questions in their normal order
        """
        return question_list


class StartingFromLastQuestionStrategy(SolveQuestionStrategy):
    def process_questions(self, question_list):
        """ 
        Returns questions in a reverse order
        """
        return list(reversed(question_list))


class SiniftaKalmaStrategy(SolveQuestionStrategy):
    def process_questions(self, question_list):
        """ 
        Returns an empty list, follow this strategy 
        if you don't want to pass the exam 

        """
        return []


class RandomSolvingStrategy(SolveQuestionStrategy):
    def process_questions(self, question_list):
        """ 
        Returns a shuffled list

        """
        list_copy = question_list.copy()

        random.shuffle(list_copy)
        return list_copy


STRATEGY_LIST = {
    'start_first': StartingFromFirstQuestionStrategy(),
    'start_last': StartingFromLastQuestionStrategy(),
    'sinifta_kal': SiniftaKalmaStrategy(),
    'random': RandomSolvingStrategy()

}


class Question:
    """ Class for questions to be used in exams """

    def __init__(self, content, field):
        self.content = content
        self.field = field


class Exam:
    """ Class for Exam """

    def __init__(self, strategy=StartingFromFirstQuestionStrategy()):
        """ Initializer for Exam Class  """
        self.questions = []
        self.strategy = strategy

    def add_question(self, question):
        self.questions.append(question)

    def change_strategy(self, strategy):
        """ Use this to change strategy """
        self.strategy = strategy

    def solve_exam(self):
        question_list = list()
        question_list = self.strategy.process_questions(self.questions)

        if len(question_list) == 0:
            print("Congratulations, you failed the exam...")
            return

        for q in question_list:
            print(
                f'Solving the {q.field} question using "{str(self.strategy).split(".")[1].split(" ")[0]}" strategy\n')


if __name__ == '__main__':
    question1 = Question(
        "What is the difference between a tuple and a list?", 'Python')
    question2 = Question("What is a race condition?", 'General Software')
    question3 = Question(
        "I have an I/O bound operation, do I use multithreading or multiprocessing?", "General Software")
    question4 = Question(
        'How do I use Strategy design pattern?', 'General Software')

    exam = Exam()
    exam.add_question(question1)
    exam.add_question(question2)
    exam.add_question(question3)
    exam.add_question(question4)

    # exam.solve_exam()

    exam.change_strategy(STRATEGY_LIST['sinifta_kal'])
    exam.solve_exam()
