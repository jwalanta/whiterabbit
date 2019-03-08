#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

class TerminalWrapper:

	def display(self, matrix):

		rows = len(matrix)
		cols = len(matrix[0])

		# clear screen
		os.system("clear")

		sys.stdout.write(" ")
		for c in range(cols):
			sys.stdout.write(str(c%10))
		print()

		count = 0
		for r in range(rows):
			sys.stdout.write(str(r))
			for c in range(cols):
				if matrix[r][c] == (0,0,0) or matrix[r][c] == 0:
					sys.stdout.write(" ")
				else:
					sys.stdout.write("█")
					count = count + 1

			print()

		print("Pixel Count =", count)
		print("Power @ 10mA per pixel = ", count * 10)
