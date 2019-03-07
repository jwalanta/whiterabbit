#!/usr/bin/env python
# -*- coding: utf-8 -*-

import board
import neopixel

# LED strip configuration:
LED_COUNT      = 144 * 5    # Number of LED pixels.
LED_PIN        = board.D18  # GPIO pin connected to the pixels (18 uses PWM!).
LED_BRIGHTNESS = 1          # Set to 0 for darkest and 1 for brightest

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
LED_ORDER = neopixel.GRB

class NeopixelWrapper:

	def __init__(self):
		self.strip = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=1, auto_write=False, pixel_order=LED_ORDER)

	def matrix_to_array(self, matrix):
		arr = []
		rows = len(matrix)
		cols = len(matrix[0])
		for r in range(rows):
			for c in range(cols):
				if r % 2 == 1:
					arr.append(matrix[r][c])
				else:
					arr.append(matrix[r][143-c])

		return arr

	def display(self, matrix):
		arr = self.matrix_to_array(matrix)
		for i in range(len(arr)):
			self.strip[i] = arr[i]

		self.strip.show()



