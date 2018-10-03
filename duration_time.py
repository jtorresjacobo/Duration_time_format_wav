import os
import soundfile as sf
import utils_1


#counting time of audio format .wav
def analysing_format_wav(carpeta):
	semi=0
	for archivo in os.listdir(carpeta):
		archivos=archivo.split(".")	
		if archivos[1]=="wav":
			f = sf.SoundFile(carpeta+"/"+archivo)
			#seconds
			total=int(format(len(f) / f.samplerate))
			#total_seconds
			semi=semi+total
	utils_1.calculate_time(semi)
	
def input_extention():
	print("Ruta principal: "+ os.getcwd())
	extension=raw_input("ingrese extension de la ruta principal")
	path_of_wav_file=os.getcwd()+"/"+extension
	return path_of_wav_file

def main():
	file_with_extention=input_extention()
	print(file_with_extention)
	analysing_format_wav(file_with_extention)

if __name__ == "__main__":
	main()


		
