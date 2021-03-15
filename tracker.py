'''Class object for calorie tracking'''

from day import Day

#https://docs.python.org/3/library/datetime.html
from datetime import date, timedelta as td

class Tracker():
	"""Object used for tracking calorie intake on a weekly basis"""
	def __init__(self, week=None, start_date=None):
		#if there's already a Tracker on record for this week,
		#don't create a new Tracker object
		if not week:
			self.week = self.autofill_week()
			self.start_date = self.set_start_date()
		else:
			self.week = week
			self.start_date = start_date

	#creates empty day-objects
	def autofill_week(self):
		week = [Day()]*7
		#[Monday, Tuesday, ..., Sunday]
		return week

	def set_start_date(self):
		"""start dates are Mondays (sorry Garfield)"""
		curr_date = date.today()	#grab the current date
		delta = td(days=curr_date.weekday())	#Monday+delta=curr_date.weekday
		
		#if it's a Tuesday, we want the start date to be on a Monday,
		#so we subtract off delta
		start_date = curr_date - delta
		return start_date