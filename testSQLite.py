#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('sputnik.db')
    
    time = 13
    latitude = 25.13324
    longitude = -28.45544
    
    cur = con.cursor()  
    
    for i in range(0, 5):
		
		time += 1
		latitude += 0.5
		longitude -= 0.5
		
		requete = 'insert into position (time, latitude, longitude) values (' + str(time) + ',' + str(latitude) + ',' + str(longitude) + ');' 
    
		cur.execute(requete)
		
		#cur = con.cursor()    
		cur.execute('SELECT * from position')
		
		data = cur.fetchall()
		
		print "==========="
		for row in data:
			for col in row:
				print col
    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
		con.commit()
		con.close()
