# GPS.py
# ------------
# Acquiert, décortique et publie les données GPS
# ------------
# 
# À faire :
#  - Connection à la base de données mySQL
#  - Publication des résultats
#
# ------------

import serial

# Connection au GPS
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.5)

# Tableaux pour décortiquer la chaine GPGGA
virgule = [0,0,0,0,0,0,0,0,0,0,0,0]
GPSdata = ['','','','','','','','','','']

# Boucle principale

while True:
	
	# On cherche le caractère de début de chaine
    rcv = port.read(1)
    if rcv is '$':
		
		# On cherche la chaine de type GPGGA
		rcv = port.read(5)
		if rcv == 'GPGGA':
			
			# On ramasse la chaîne au complet, et on trouve la position des ','
			rcv = port.read(70)
			virgule[0] = rcv.find(',')
			for i in range(1,11):
				virgule[i] = rcv.find(',',virgule[i-1]+1)
			
			# On extrait les données entre les virgules, selon
			# $GPGGA,212113.00,4524.17242,N,07150.81415,W,1,07,1.48,210.5,M,-31.4,M,,*64
			# $GPGGA,hhmmss.ss,llll.ll,a,yyyyy.yy,a,x,xx,x.x,x.x,M,x.x,M,x.x,xxxx			
			for i in range(10):
				GPSdata[i] = rcv[virgule[i]+1:virgule[i+1]]
			
			# Les données : Latitude, direction, Longitude, direction, Altitude, unité.
			# @ publier dans BDD
			print 'Latitude  : ', float(GPSdata[1])/100, ' ', GPSdata[2]
			print 'Longitude : ', float(GPSdata[3])/100, ' ', GPSdata[4]
			print 'Altitude  : ', float(GPSdata[8]), ' ', GPSdata[9]
			print '----------------'
