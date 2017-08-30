#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Minimal BDF font reader
"""

class BDFFont:
	def __init__(self, filename):

		self.data = {}

		f = open(filename, "r")

		while True:
			line = f.readline()
			if line == "":
				break

			if line.startswith("FONTBOUNDINGBOX"):
				parts = line.split(" ")
				self.width = int(parts[1])
				self.height = int(parts[2])

			if line.startswith("ENCODING"):

				ascii = int(line[9:].strip())
				self.data[ascii] = []

				while True:
					ll = f.readline().strip()
					if len(ll) == 2:
						self.data[ascii].append(int("0x" + ll, 16))	

					if ll.strip() == "ENDCHAR":
						break

				self.data[ascii] = [0] * (self.height-len(self.data[ascii]) - 2 ) + self.data[ascii]

		f.close()

	def get_char(self, char):
		if ord(char) in self.data:
			return self.data[ord(char)]
		else:
			return [0] * self.height

	def get_width(self):
		return self.width

	def get_height(self):
		return self.height