import re

from src.util import cw_meta
from src.util.lesson import Lesson


class Lesson7IMTEQuiz(Lesson):
	def __init__(self):
		super().__init__()
		self.lesson_title = f"I, M, T, E Quiz"
		self.lesson_description = f"In this quiz, your progress will not be shown until the quiz is complete."

		self.target_text = 'I TIME ME IT MET EM TIE'

	def key_event(self, cw_text):
		cw_text = re.sub("[^(IMTE )]", '█', cw_text)
		return cw_text

	def is_quiz(self):
		return True
