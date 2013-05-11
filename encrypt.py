#!usr/bin/python
# @author Aayush Ahuja
import os,sys


fileList = []
rootdir = sys.argv[1]
#rootdir = '.'

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for file in files:
	if ("decrypt" not in file ) and ("encrypt" not in file):
		if len(file) > 30:
			newfile = ""
			s = file.split('.')
			c = 27;i=0
			while c>0:
				if len(s[i]) < c:
					newfile+=s[i]
				else:
					newfile+=s[i][0:c]
				c-=1
			newfile+=s[-1]

		fileList.append(file)


#print fileList

for x in fileList:
	hash = ""
	for i in x:
		try:
			i = i.encode('utf-8','ignore')
			h = str(ord(i)) + "."
			hash+=h
		except:
			continue	
	hash = hash[:-1]
	try:
		os.rename(x,hash)
		#print "Renamed %s : %s" %(x,hash)
	except:
		print "Error Renaming %s : %s" %(x,hash)


print "TOTAL NUMBER OF FILES: %s"%(str(len(fileList)))
