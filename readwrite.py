def read():
	f = open("input", 'r')
	
	# read a
	line = f.readline()
	split = line.split()
	a = float(split[2])

	# read b
	line = f.readline()
	split = line.split()
	b = float(split[2])

	# read c
	line = f.readline()
	split = line.split()
	c = float(split[2])
	
	return(a,b,c)

	f.close()
