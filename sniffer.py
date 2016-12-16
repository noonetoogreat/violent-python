import socket
import sys
import os

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(5)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except Exception, e:
		print "[-] Error = " + ip + ':' + str(port) + " " + str(e)

def checkVulns(banner, file='vuln_banners.txt'):
	f = open('vuln_banners.txt', 'r')
	for line in f.readlines():
		if line.rstrip('\n') in banner:
			print '[+] Server is vulnerable: ' + line.rstrip('\n')
	else:
		print '[-] FTP Server is not vulerable'

def main():

	filename = ''

	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print '[-] ' + filename + ' does not exist.'
			exit(0)
		if not os.access(filename, os.R_OK):
			print '[-] ' + filename + ' access denied.'
			exit(0)
		print '[+] Reading Vulnerabilities from: ' + filename

	portList = [21, 22, 25, 80]

	for x in xrange(0, 255):

		ip1 = '127.0.0.' + str(x)

		for port in portList:

			banner1 = retBanner(ip1, port)

			if banner1:
				print '[+] ' + ip1 + ': ' + banner1.strip('\n')
				checkVulns(banner1)

if __name__ == '__main__':
	main()  