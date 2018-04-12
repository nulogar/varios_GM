#!/usr/bin/python
"""
Para anotar strain_comparison_result.txt  (procedente de la pipelineTB o sus derivados) a partir de un gff de la cepa en cuestion (de genbank) SIN CABECERA
No muy testado con diferentes gff. Comprobar que todo vaya bien
"""
import sys

infile=sys.argv[1] #archivo strain_comparison_result.txt (procedente de la pipelineTB o sus derivados) a anotar
eqfile=sys.argv[2] #archivo gff anotado, eliminada la cabecera
outputfile=sys.argv[3] #salida

try:
	inputfile = open(infile)
except IOError:
	print("%s does not exist!!" %infile)

try:
	output = open(outputfile,'w')
except IOError:
	print("File %s cannot be created!!" % outputfile)


for line in inputfile:
	line=line.rstrip()
	words=line.split()
	if words[0]=='Position':
		output.write(line+"\t"+"Product"+"\n")
	else:
		pos=int(words[0])
#		print pos
		try:
			eqsfile = open(eqfile)
		except IOError:
			print("%s does not exist!!" %eqfile)
		flag=0
		producto="NA"
		for line1 in eqsfile:
			line1=line1.rstrip()
#			print line
			words=line1.split('\t')
#			print words[1]
			features=words[8]
			separados=features.split(';')
#			print separados
			for i in separados:
				campos=i.split('=')
#				print campos
				if campos[0]=='product':
					start= int(words[3])
					stop= int(words[4])
					if pos>=start and pos<=stop:
						flag=1
						producto=campos[1]
#		print producto
		eqsfile.close()
		if flag ==1:
			output.write(line+"\t"+producto+"\n")
		else:
			output.write(line+"\n")
	#if words[1]=="RefSeq" and words[2]!="riboswitch":
		#print line


inputfile.close()
output.close()
