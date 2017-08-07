import os,sys,time

def enigme():
	print "C'est plus grand que Dieu,"
	print "Et plus mechant que le diable."
	print "Les pauvres l'ont; les riches en ont besoin."
	print "Si vous le mangez, vous mourrez."
	print 
	print "Qu'est-ce que c'est?"
	print
	test = raw_input("Reponse: ")

	time.sleep(1)
	
	return test

os.system("clear")
delais = 5
while(True):
	test = enigme()
	if(test == 'rien' or test == 'Rien'):
		print
		print
		print	
		while(True):
			os.system("clear")
			test = raw_input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\tRYTHME MONTREAL")
	else:
		tempsrestant = delais
		while(tempsrestant > 0):
			os.system("clear")
			print '\n\n\n\t\tErreur.\n\n\t\tReinitialisation dans ', tempsrestant,' secondes.'
			time.sleep(1)
			tempsrestant -= 1
			os.system("clear")
		delais += 10
		os.system("clear")
