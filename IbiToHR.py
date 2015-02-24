import sys
try:
	_FILE_PATH_INPUT  = sys.argv[1] 
	_FILE_PATH_OUTPUT  = sys.argv[2] 
except:
	print "usage: python IbiToHr.py <input_file> <outputfile>"
	sys.exit(1)


with open(_FILE_PATH_INPUT) as _FILE_INPUT:
	_linecount = 0
	_data = []
	for _line in _FILE_INPUT:
		if(_linecount < 1):
			_data.append(_line.replace("IBI","HR"))
		else:
			_values = _line.replace("\n","").split(",")
			_data.append(  str ( 60.0 / float (_values[1])) + "\n")
		_linecount += 1
	with open(_FILE_PATH_OUTPUT,"w") as _FILE_OUTPUT:
		_FILE_OUTPUT.writelines(_data)

