
def calculate_time(seconds):
	hora=semi/3600
	minutos=(semi-hora*3600)/60
	segundos=semi-minutos*60-hora*3600
	#print hour,minutes,seconds
	return "hora: "+str(hora) + "\n"+"minutos: "+str(minutos)+"\n"+"segundos: " + str(segundos)
