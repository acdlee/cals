'''Control center for Cals project'''
from tracker import Tracker
from ui import UI

#https://docs.python.org/3/library/datetime.html
from datetime import date, timedelta as td

#deserialize python objects
import pickle

#debugging tool
DEBUG = 0
import sys

#handle the logic flow of the program here
def main():	
	#initial setup for the tracker object
	tracker = setup()

	#start UI
	ui = UI(tracker)


#this function handles some initial semantics with 
#tracker objects and particular weeks
def setup():
	"""	
		before making a new tracker class, we have to 
		check if there already exists a tracker class 
		for the current week
	"""

	#search for an existing file (handles the-very first week-case)
	try:
		#try to open the pickle file
		pkl_file = open('curr_tracker', 'rb')	#current week's tracker
	except Exception as e:
		if DEBUG:
			#if debugging, print the error ...
			print(e)
			#... and exit the program
			sys.exit()

		#no file was found, then we should create our first
		#	tracker object
		return Tracker()

	#if here, that means we have a Tracker object
	#-> let's load the pickled Tracker object
	curr_tracker = pickle.load(pkl_file)

	ret_tracker = curr_tracker	#default is the pickled Tracker

	#now determine if we need to create a new week's Tracker
	curr_date = date.today()	#today's date
	bound = td(days=6)			#lower bound for a new week

	#check the dates
	if (curr_date - curr_tracker.start_date) > bound:
		#!!!we want to save the old Tracker info before
		#!!!creating a new one

		#create a new Tracker() obejct
		ret_tracker = Tracker()

	#close the file
	pkl_file.close()

	return ret_tracker

if __name__ == '__main__':
	main()