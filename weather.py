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
				self.forecast_mtime = os.path.getmtime(self.forecast_file)
				f = open(self.forecast_file, "r")
				self.forecast = json.load(f)
				f.close()
		else:
			# file can be unavailable if the cron is writing on it
			# reset only if it's older than an hour
			if current_time - self.forecast_mtime > 3600:
				self.forecast_mtime = 0
				self.forecast = {}

	def get_current_temperature(self):
		try:
			self.update()
			return str(self.forecast['currentobservation']['Temp']) + "F"
		except:
			return ""

	def get_today_forecast(self):
		try:
			self.update()
			t = self.forecast["data"]["temperature"]
			return (max(t[0],t[1]), min(t[0],t[1]))
		except:
			return ("","")
