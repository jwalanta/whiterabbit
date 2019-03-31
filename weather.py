#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import time

class Weather:

	def __init__(self):
		self.forecast_file = "/var/cache/forecast.json"
		self.forecast_mtime = 0
		self.forecast = {}

	def update(self):
		current_time = time.time()

		# update forecast
		if os.path.isfile(self.forecast_file):
			# check if file has been modified
			if os.path.getmtime(self.forecast_file) != self.forecast_mtime:
				f = open(self.forecast_file, "r")
				forecast = json.load(f)
				f.close()

				# error will be raised by now if the file is empty
				# check if the required forecast keys are there
				if "currentobservation" in forecast and "data" in forecast:
					self.forecast = forecast
					self.forecast_mtime = os.path.getmtime(self.forecast_file)
		else:
			# file can be unavailable if the cron is writing on it
			# reset only if it's older than an hour
			if current_time - self.forecast_mtime > 3600:
				self.forecast_mtime = 0
				self.forecast = {}

	def get_current_temperature(self):
		try:
			self.update()
		except Exception as e:
			pass

		if "currentobservation" in self.forecast:
			return str(self.forecast['currentobservation']['Temp']) + "F"
		else:
			return ""

	def get_today_forecast(self):
		try:
			self.update()
		except Exception as e:
			pass

		if "data" in self.forecast:
			t = self.forecast["data"]["temperature"]
			return (max(t[0],t[1]), min(t[0],t[1]))
		else:
			return ("","")
