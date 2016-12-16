import zipfile
import optparse
from threading import Thread

def extractZip(zFile, password):
	try:
		zFile.extractall(pwd=password)
		print '[+] Password = ' + password
	except Exception, e:
		return 

def main():

	parser = optparse.OptionParser(usage="usage: %prog -f <zipfile> -d <dictionary>")
	parser.add_option('-f', dest='zname', type='string', help='specify zip file')
	parser.add_option('-d', dest='dictFile', type='string', help='specify dictionary file')

	(options, args) = parser.parse_args()

	if options.zname == None or options.dictFile == None:
		print parser.usage
		exit(0)
	else:
		zname = options.zname
		dictFile = options.dictFile

	zFile = zipfile.ZipFile(zname)
	dictFile = open(dictFile)
	for line in dictFile.readlines():
		password = line.rstrip('\n')
		t = Thread(target=extractZip, args=(zFile, password))
		t.start()

if __name__ == '__main__':
	main()



