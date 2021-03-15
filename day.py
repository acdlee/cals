"""day object for a (week) tracker object"""

class Day(object):
	"""calorie in/out for a day"""
	def __init__(self, net_cals=0, cal_in=0, cal_out=0):
		#three variables keeping track of total calorie intake,
		#	outake, and net calories for a day
		self.net_cals = net_cals
		self.cal_in = cal_in
		self.cal_out = cal_out


	#add a flat number of calories to the day
	def add_calories(self, cals):
		self.cal_in += cals
		self.net_cals += cals

	#remove a flat number of calories to the day
	def sub_calories(self, cals):
		self.cal_out += cals
		self.net_cals -= cals




	"""MUTATORS AND ACCESSORS"""
	def get_net_cals(self):
		return self.net_cals

	def set_net_cals(self, net_cals):
		self.net_cals = net_cals

	def get_cal_in(self):
		return self.get_cal_in

	def set_cal_in(self, cal_in):
		self.cal_in = cal_in

	def get_cal_out(self):
		return self.get_cal_out

	def set_cal_in(self, cal_out):
		self.cal_out = cal_out