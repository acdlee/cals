"""class object for the user interface"""

class UI():
	"""user interaction with Tracker"""
	def __init__(self, tracker):
		self.run_script()


	def run_script(self):
		intro_msg = """
		Welcome to your calorie tracker. Please select
		an option:
		[1] Adjust calories
		[2] View week totals
		[3]	View month totals

		"""