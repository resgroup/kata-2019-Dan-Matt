import numpy as np
import datetime as dt

class BerlinClock:
	def __init__(self,time_string):
		time_format = '%H:%M:%S'
		self.date_time = dt.datetime.strptime(time_string,time_format)
		self.row_1_light = self.calculate_row_1_light()
		self.row_2_lights = self.calculate_row_2_lights()

	def calculate_row_1_light(self):
		if (self.date_time.second % 2) == 0:
			print("{0} is Even".format(self.date_time.second))
			light_state = 'Y'
		elif (self.date_time.second % 2) == 1:
			print("{0} is Odd".format(self.date_time.second))
			light_state = 'O'
		return light_state

	def calculate_row_2_lights(self):
		full_hours = int(self.date_time.hour/5)
		light_string = ''
		for i in range(0,full_hours):
			light_string += 'R'
		while len(light_string) < 4:
			light_string += 'O'
		return light_string
