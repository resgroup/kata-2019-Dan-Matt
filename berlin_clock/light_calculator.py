import numpy as np
import datetime as dt

class BerlinClock:
	def __init__(self,time_string):
		time_format = '%H:%M:%S'
		self.date_time = dt.datetime.strptime(time_string,time_format)
		self.seconds_light = self.calculate_seconds_light()
		self.five_hour_lights = self.calculate_5_hour_lights()
		self.one_hour_lights = self.calculate_1_hour_lights()
		self.five_minute_lights = self.calculate_5_minute_lights()
		self.one_minute_lights = self.calculate_1_minute_lights()

	def calculate_seconds_light(self):
		if (self.date_time.second % 2) == 0:
			return 'Y'
		return 'O'

	def calculate_5_hour_lights(self):
		full_hours = int(self.date_time.hour/5)
		light_string = ''
		for i in range(0,full_hours):
			light_string += 'R'
		while len(light_string) < 4:
			light_string += 'O'
		return light_string

	def calculate_1_hour_lights(self):
		remainder_hours = int(self.date_time.hour % 5)
		light_string = ''
		for i in range(0,remainder_hours):
			light_string += 'R'
		while len(light_string) < 4:
			light_string += 'O'
		return light_string

	def calculate_5_minute_lights(self):
		full_five_minutes = int(self.date_time.minute / 5)
		light_string = ''
		for i in range(0,full_five_minutes):
			light_string += 'Y'
		while len(light_string) < 11:
			light_string += 'O'
		return light_string

	def calculate_1_minute_lights(self):
		remainder_minutes = int(self.date_time.minute % 5)
		light_string = ''
		for i in range(0,remainder_minutes):
			light_string += 'Y'
		while len(light_string) < 4:
			light_string += 'O'
		return light_string