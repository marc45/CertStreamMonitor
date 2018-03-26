#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is a part of CertStreamMonitor

import os
import sys
import logging
import configparser

class ConfParser:
	'''Configuration file parser'''
	def __init__(self, Confile=None):
		try:
			self.config = configparser.ConfigParser()

			with open(Confile, 'r', encoding='utf-8') as f:
				self.config.readfp(f)

				# search strings
				self.SearchString = self.config['SEARCH']['SearchKeywords']

				# Databases
				self.DBFile = self.config['DATABASE']['DBFile']
				self.TABLEname = self.config['DATABASE']['TABLEname']

				# Logging
				self.LogFile = self.config['LOGGING']['LogFile']

		except IOError:
			#print("[!!!] Configuration file Error: "+Confile)
			logging.error(" Configuration file Error: "+Confile)

		except:
			err = sys.exc_info()
			#print("[!!!] ConfParser Error: "+str(err))
			logging.error(" ConfParser Error: "+str(err))
