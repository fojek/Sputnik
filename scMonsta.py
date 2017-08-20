#!/usr/bin/python

import Adafruit_BMP.BMP085 as BMP085
import sqlite3 as lite
import sys
import time
import os 
import datetime

sensor = BMP085.BMP085()

def insereDB(t, p, a, sa):
	con = lite.connect('sputnik.db')
	cur = con.cursor()  
	
	requete = 'create table courant (altitue'
	
	requete = 'insert into science (time, temperature, pression, altitude, sl_pres) values ("' + str(datetime.datetime.now()) + '",' + str(t) + ',' + str(p) + ',' + str(a) + ',' + str(sa) + ');'

	cur.execute(requete)

	con.commit()
	


print 'Science Monsta pret.'

# Boucle principale
while 1:
        
		temp = sensor.read_temperature()
		pres = sensor.read_pressure()
		alt = sensor.read_altitude()
		sl_pres = sensor.read_sealevel_pressure()
		
		insereDB(temp, pres, alt, sl_pres)
		time.sleep(5)
