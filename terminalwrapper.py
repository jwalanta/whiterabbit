#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class TerminalWrapper:

	def display(self, matrix):

		rows = len(matrix)
		cols = len(matrix[0])

		# clear screen
		sys.stderr.write("\x1b[2J\x1b[H")

		sys.stdout.write(" ")
		for c in xrange(cols):
			sys.stdout.write(str(c%10))
		print

		count = 0
		for r in xrange(rows):
			sys.stdout.write(str(r))
			for c in xrange(cols):
				if matrix[r][c] > 0:
					sys.stdout.write("█")
					count = count + 1
				else:
					sys.stdout.write(" ")
			print

		print "Pixel Count =", count
		print "Power @ 10mA per pixel = ", count * 10
