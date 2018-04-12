#!/usr/bin/python
"""
Para seleccionar la pareja de los reads de un archivo fastq F o R que estan en otro complementario
Hace lo mismo que /plataforma_laura/filtrarPEcabeceras.py, pero es algo mas rapido y no hay que generar el archivo de las cabeceras
"""
import sys

infile=sys.argv[1] #archivo F o R con las secuencias de las que queremos encontrar la pareja
complementaryfile=sys.argv[2] #archivo paired end complementario al de entrada
outfile=sys.argv[3] #archivo de salida con las secuencias seleccionadas del segundo archivo


try:
	inputfile = open(infile)
except IOError:
	print("%s does not exist!!" % infile)

try:
	compfile = open(complementaryfile)
except IOError:
	print("%s does not exist!!" % compfile)

try:
	output = open(outfile,'w')
except IOError:
	print("File %s cannot be created!!" % outfile)


for line in inputfile:
	line=line.rstrip()
	if len(line)>1:
		if line[0:2]=="@M":
			words=line.split()
#			print line
			cabecera=words[0]
			line2=compfile.readline()
			words2=line2.split()
#			print line2
			while words2[0] !=cabecera:
				line2=compfile.readline()
				words2=line2.split()
#			print line2
			output.write(line2)
			line2=compfile.readline()
			output.write(line2)
			line2=compfile.readline()
			output.write(line2)
			line2=compfile.readline()
			output.write(line2)
		 
compfile.close()

inputfile.close()

output.close()
