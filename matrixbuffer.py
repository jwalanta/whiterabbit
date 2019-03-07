#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Matrix Buffer to compute output
"""

import time

class MatrixBuffer:

	ALIGN_LEFT   = -1
	ALIGN_CENTER = 0
	ALIGN_RIGHT  = 1
	CHAR_SPACING = 1

	def __init__(self, rows, cols, font, display_wrapper):
		self.rows = rows
		self.cols = cols
		self.font = font
		self.display_wrapper = display_wrapper
		self.matrix = [[0 for c in range(cols)] for r in range(rows)]

	def get_rows(self):
		return self.rows

	def get_cols(self):
		return self.cols

	def get_matrix(self):
		return self.matrix

	def write_pixel(self, r, c, value):
		if r >= 0 and r < self.rows and c >=0 and c < self.cols:
			self.matrix[r][c] = value

	def write_char(self, r, c, char, color):
		char_data = self.font.get_char(char)
		row = r
		for n in char_data:
			col = c
			for p in list(bin(n)[2:].zfill(8)):
				if p == '0':
					self.write_pixel(row, col, (0,0,0))
				else:
					self.write_pixel(row, col, color)
					
				col = col + 1
			row = row + 1

	def write_string_at(self, row, col, str, color):
		for c in str:
			self.write_char(row, col, c, color)
			col = col + self.font.get_width() + self.CHAR_SPACING

	def write_string(self, str, color, align=ALIGN_LEFT):		
		if len(str) > self.cols:
			str = str[0:self.cols]

		if align == self.ALIGN_LEFT:
			self.write_string_at(0, 1, str, color)
		elif align == self.ALIGN_RIGHT:
			self.write_string_at(0, self.cols - len(str) * (self.font.get_width() + self.CHAR_SPACING), str, color)
		elif align == self.ALIGN_CENTER:
			self.write_string_at(0, int( (self.cols - len(str) * (self.font.get_width() + self.CHAR_SPACING)) / 2 ), str, color )

	def scroll_string(self, str, color, delay=0.01):

		# first display string and pause
		self.clear()
		self.write_string_at(0, 0, str, color)
		self.show()
		time.sleep(3)

		# start scrolling
		for st in range(len(str)):
			for offset in range(self.font.get_width() + self.CHAR_SPACING):
				self.clear()
				self.write_string_at(0, -offset, str[st:], color)
				self.show()
				time.sleep(delay)

		self.clear()
		self.show()

	def clear(self):
		for r in range(self.rows):
			for c in range(self.cols):
				self.matrix[r][c] = 0

	def show(self):
		self.display_wrapper.display(self.matrix)

