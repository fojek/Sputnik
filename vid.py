import os
import time

i = 1

while 1:
	# Film de 5 minutes 300000
	video = 'raspivid -t 300000 -o ' + str(i) + '.h264'
	os.system(video)

	photo = 'raspistill -o ' + str(i) + '.jpg'
	os.system(photo)	

	time.sleep(2)
	
	if(i<5):
		i += 1
	else:
		i = 1
