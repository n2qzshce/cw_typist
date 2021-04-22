import re

from src.tutor.lessons.lesson import Lesson


class Lesson3(Lesson):
	def __init__(self):
		super().__init__()
		self.number = 3
		self.lesson_title = "Spacing:"
		self.lesson_description = f"Where a short pause represents a new character, a longer pause represents a space." \
			f" The pause in between characters is usually as long as a 'dot,' and the pause in between words is as long" \
			f" or longer than a dash."

		self.target_text = 'EE E EEE E EE EEE'

	def key_event(self, cw_text):
		cw_text = re.sub("[^(E )]", '', cw_text)
		return cw_text
