#!usr/bin/python
# @author Aayush Ahuja
import os,sys


fileList = []
rootdir = sys.argv[1]
#rootdir = '.'

for root, subFolder, files in os.walk(rootdir):
	for file in files:
		s = file.split(".")
		if ("decrypt" not in file ) and  ("encrypt" not in file):
			fileList.append(os.path.join(root,file))

#print fileList
for x in fileList:
	hash = x.split('.')
	name = ""
	#print hash

	for i in hash:
		if unicode(i).isnumeric() == False:
			num = ""
			j = len(i)-1
			while j>0:
				if unicode(i[j]).isnumeric() == False:
					break
				else:
					num = i[j] + num
				j-=1
			if num:
				name+=chr(int(num))
		elif unicode(i).isnumeric() == True:
			name+=chr(int(i))
	try:
		os.rename(x,name)
		print "Renamed %s:%s" %(x,name)
	except:
		print "Error Occurred at %s : %s" %(x,name)