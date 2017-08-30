#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import time

class Weather:

	def __init__(self):
		self.conditions_file = "/var/cache/conditions.json"
		self.conditions_mtime = 0
		self.conditions = {}

		self.forecast_file = "/var/cache/forecast.json"
		self.forecast_mtime = 0
		self.forecast = {}

	def update(self):
		current_time = time.time()

		# update conditions
		if os.path.isfile(self.conditions_file):
			# check if file has been modified
			if os.path.getmtime(self.conditions_file) != self.conditions_mtime:
				self.conditions_mtime = os.path.getmtime(self.conditions_file)
				f = open(self.conditions_file, "r")
				self.conditions = json.load(f)
				f.close()
		else:
			# file can be unavailable if the cron is writing on it
			# reset only if it's older than an hour
			if current_time - self.conditions_mtime > 3600:
				self.conditions_mtime = 0
				self.conditions = {}

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
			return str(self.conditions['current_observation']['temp_f']) + "F"
		except:
			return ""

	def get_today_forecast(self):
		try:
			self.update()
			today = self.forecast['forecast']['simpleforecast']['forecastday'][0]
			return (str(today['high']['fahrenheit']), str(today['low']['fahrenheit']))
		except:
			return ("","")
