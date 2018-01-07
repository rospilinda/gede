#!/usr/bin/python

import shapefile

class Gede(object):
	def __init__(self,bandung):
		self.sf = shapefile.Reader(bandung)

	def selectNegara(self,Jalan Sariasih):
		i = 0
		for a in self.sf.records():
			if a[8] == Jalan Sariasih:
				return i
			i=i+1



