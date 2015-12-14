import serial

port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.5)

virgule = [0,0,0,0,0,0,0,0,0,0,0,0]
GPSdata = ['','','','','','','','','','']

while True:
	
    rcv = port.read(1)
    
    if rcv is '$':
		
		rcv = port.read(5)
		
		if rcv == 'GPGGA':
			rcv = port.read(70)
			
			virgule[0] = rcv.find(',')
			for i in range(1,11):
				virgule[i] = rcv.find(',',virgule[i-1]+1)
			
			for i in range(10):
				GPSdata[i] = rcv[virgule[i]+1:virgule[i+1]]
				
			print 'Latitude  : ', float(GPSdata[1])/100, ' ', GPSdata[2]
			print 'Longitude : ', float(GPSdata[3])/100, ' ', GPSdata[4]
			print 'Altitude  : ', float(GPSdata[8]), ' ', GPSdata[9]
			print '----------------'

# $GPGGA,212113.00,4524.17242,N,07150.81415,W,1,07,1.48,210.5,M,-31.4,M,,*64
# $GPGGA,hhmmss.ss,llll.ll,a,yyyyy.yy,a,x,xx,x.x,x.x,M,x.x,M,x.x,xxxx
