import numpy as np
import datetime as dt

class BerlinClock:
	def __init__(self,time_string):
		time_format = '%H:%M:%s'
		self.date_time = dt.datetime.strptime(time_string,time_format)

	def calculate_row_1_light(self):
		seconds = self.date_time.second()
		if (seconds % 2) == 0:
			print("{0} is Even".format(seconds))
			light_state = 'Y'
		else:
			print("{0} is Odd".format(seconds))
			light_state = 'O'

		return light_state