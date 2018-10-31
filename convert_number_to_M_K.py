f = open("delete.txt", "r")
for line in f:
	line = line.replace("\n", "")
	l = []
	for i in line.split("\t"):
		try:
			l.append(float(i))
		except:
			l.append(i)
	for i in l:
		try:
		    if i > 1000000:
		        print str(round(i/1000000,1))+"M",
		    elif i > 1000:
		        print str(round(i/1000,1))+"K",
		except:
			print i,
	print
