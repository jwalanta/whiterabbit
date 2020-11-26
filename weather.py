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

		self.airnow_file = "/var/cache/airnow.json"
		self.airnow_mtime = 0
		self.airnow = {}

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

		# update airnow
		if os.path.isfile(self.airnow_file):
			# check if file has been modified
			if os.path.getmtime(self.airnow_file) != self.airnow_mtime:
				f = open(self.airnow_file, "r")
				airnow = json.load(f)
				f.close()

				# error will be raised by now if the file is empty
				# check if the required forecast keys are there
				if len(airnow) > 0:
					self.airnow = airnow
					self.airnow_mtime = os.path.getmtime(self.airnow_file)
		else:
			# file can be unavailable if the cron is writing on it
			# reset only if it's older than an hour
			if current_time - self.airnow_mtime > 3600:
				self.airnow_mtime = 0
				self.airnow = {}


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

	def get_current_aqi(self):
		try:
			self.update()
		except Exception as e:
			pass

		if len(self.airnow) > 0:
			return self.airnow[0]["aqi"]
		else:
			return -1

	def get_current_aqi_color(self):
		aqi = self.get_current_aqi()

		if aqi >=0 and aqi <= 50:
			return (0,1,0) # green
		elif aqi >=51 and aqi <= 100:
			return (1,1,0) # yellow
		elif aqi >=101 and aqi <= 200:
			return (1,0,0) # red
		elif aqi >=201:
			return (1,0,1) # purple
		else:
			return (1,1,1) # white  
