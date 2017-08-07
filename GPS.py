# Pinout pour le GPS / RPi:
# 1 2
# 3 4
# 5 6
# 7 8
# 9 10
#
# Vcc sur pin 1 (3.3V)
# Gnd sur pin 9 (Gnd)
# Rxd sur pin 8 (Txd)
# Txd sur pin 10 (Rxd)

import serial
import sqlite3 as lite
import sys
import gammu
import time

def insereDB():
	con = lite.connect('sputnik.db')
	cur = con.cursor()  
	
	time = str(infoGPS['heure']) + ':' + str(infoGPS['minute']) + ':' + str(infoGPS['seconde'])
	
	requete = 'insert into position (time, latitude, longitude) values ("' + time + '",' + str(infoGPS['lat_angle']) + ',' + str(infoGPS['lon_angle']) + ');' 
	print requete
	cur.execute(requete)
	con.commit()

def getInfo( str ):

        # Separe aux ','
        infos = str.split(',')

        # Verifie la validite des coordonnees
        if len(infos[2]) == 0:
                return 0
        
        # Heure
        infoGPS['heure'] = int(infos[1][0:2])
        infoGPS['minute'] = int(infos[1][2:4])
        infoGPS['seconde'] = int(infos[1][4:6])

        # Latitude, longitude, altitude
        infoGPS['lat_angle'] = infos[2]
        infoGPS['lat_coord'] = infos[3]
        infoGPS['lon_angle'] = infos[4]
        infoGPS['lon_coord'] = infos[5]
        infoGPS['altitude'] = infos[11]

        return 1

### GPS init
gps = serial.Serial('/dev/ttyAMA0',9600, timeout=5)

infoGPS = { 'heure' : 0,
                'minute' : 0,
                'seconde' : 0,
                'lat_angle' : 0,
                'lat_coord' : '',
                'lon_angle' : 0,
                'lon_coord' : '',
                'altitude' : 0}
                
if not gps.isOpen():
	print 'Erreur : impossible d ouvrir le port serie.'
	exit()

print 'Connection etablie.'

### 3G init
# Create object for talking with phone
state_machine = gammu.StateMachine()

# Load config file
state_machine.ReadConfig()

# Connect to the phone
state_machine.Init()

message = {
    'Text': 'Sputnik 11 pret au decollage.',
    'SMSC': {'Location': 1},
    'Number': '18195708580',
}

state_machine.SendSMS(message)

# Boucle principale
while 1:
        data = gps.readline()
        
        if len(data) > 6:

                type = data[0:6]
                
                if type == "$GPGGA":
                        if(getInfo(data[6:len(data)])):
                                print 'Nouvelles coordonnees : '
                                print infoGPS
                                insereDB()
                                message['Text'] = 'Position : ' + infoGPS['lat_angle'] + ',' + infoGPS['lon_angle'] + ', altitude : ' + infoGPS['altitude']
                                state_machine.SendSMS(message)
                                time.sleep(30)
                        else:
								print 'Pas de connection satellite.'
