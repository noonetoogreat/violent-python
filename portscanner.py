import optparse
from socket import *
from threading import *

screenLock = Semaphore(value = 1)

def connSkt(tgtHost, tgtPort):

	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))

		connSkt.send("ViolentPython\r\n")
		results = connSkt.recv(100)

		screenLock.acquire()

		print '[+] %d/tcp open' % tgtPort
		print '[+] ' + str(results.rstrip('\n'))

	except Exception, e:
		screenLock.acquire()
		print e 
		print '[-] %d/tcp closed' % tgtPort

	finally:
		screenLock.release()
		connSkt.close()

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "[-] Cannot resolve '%s' : Unknown host" % tgtHost
		return

	try:
		tgtName = gethostbyaddr(tgtIP)
		print '[+] Scan Results for: ', tgtName[0]
	except:
		print '[+] Scan Results for: ', tgtIP

	setdefaulttimeout(1)

	for tgtPort in tgtPorts:
		t = Thread(target = connSkt, args = (tgtHost, int(tgtPort)))
		t.start()
		


def main():
	parser = optparse.OptionParser("usage: %prog --host <target host> -p <target port/ports>")
	parser.add_option('--host', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target port')
	(options, args) = parser.parse_args()

	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(",")
	if tgtHost == None or tgtPorts[0] == None:
		print parser.usage
		exit(0)
	portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
	main()


