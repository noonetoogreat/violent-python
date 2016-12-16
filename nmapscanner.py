import nmap
import optparse

def nmapScan(tgtHost, tgtPort):
	nmScan = nmap.PortScanner()
	nmScan.scan(tgtHost, tgtPort)
	state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
	print '[*] ' + tgtHost + ' tcp/' + tgtPort + ' ' + state

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
	for tgtPort in tgtPorts:
		nmapScan(tgtHost, tgtPort)

if __name__ == '__main__':
	main()
