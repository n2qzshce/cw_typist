from src.tutor.lessons.lesson import Lesson
from src.util import cw_meta


class Lesson1(Lesson):
	def __init__(self):
		super().__init__()
		self.lesson_description = f"E: {cw_meta.formatted('E')}\nDo not worry about spacing, just focus on getting " \
			"an even pace. Remember to leave a small interval between each pulse to indicate the end of a letter."

		self.target_text = 'EEEE'

	def key_event(self, cw_textbox):
		cw_textbox.text = cw_textbox.text.replace(' ', '')
