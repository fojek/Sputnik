import serial

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

gps = serial.Serial('/dev/ttyAMA0',9600)

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

while 1:
        data = gps.readline()
        
        if len(data) > 6:

                type = data[0:6]
                
                if type == "$GPGGA":
                        if(getInfo(data[6:len(data)])):
                                print 'Nouvelles coordonnees : '
                                print infoGPS
                        else:
                                print 'Pas de connection satellite.'


