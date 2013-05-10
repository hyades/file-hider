#!usr/bin/python
# @author Aayush Ahuja
import os,sys


fileList = []
rootdir = sys.argv[1]
#rootdir = '.'

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for file in files:
	s = file.split(".")
	if ("decrypt" not in file ) and ("encrypt" not in file):
		fileList.append(file)


#print fileList

for x in fileList:
	hash = ""
	for i in x:
		h = str(ord(i)) + "."
		hash+=h
	hash = hash[:-1]
	try:
		os.rename(x,hash)
		print "Renamed %s : %s" %(x,hash)
	except:
		print "Error"


print "TOTAL NUMBER OF FILES: %s"%(str(len(fileList)))
