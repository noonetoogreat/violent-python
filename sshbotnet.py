from pexpect import pxssh

PROMPT = ['# ', '>>> ', '> ', '\$ ', '$ ']

def sendcommand(child, cmd):
	child.sendline(cmd)
	child.prompt(PROMPT)
	print child.before

def connect(user, host, password):
	s = pxssh.pxssh()
	try:
		s.login(host, user, password)
	except:
		print "[-] Connection error."
		return
	s.prompt(PROMPT)
	return s

def main():
	host = raw_input("Enter host name")
	user = raw_input("Enter username")
	password = raw_input("Enter password")
	child = connect(user, host, password)
	if child != None:
		sendcommand(child, 'cat /etc/passwd | grep root')

if __name__ == '__main__':
	main()

'''
from pexpect import pxssh
import getpass
try:
    s = pxssh.pxssh()
    hostname = raw_input('hostname: ')
    username = raw_input('username: ')
    password = getpass.getpass('password: ')
    s.login(hostname, username, password)
    s.sendline('uptime')   # run a command
    s.prompt()             # match the prompt
    print(s.before)        # print everything before the prompt.
    s.sendline('ls -l')
    s.prompt()
    print(s.before)
    s.sendline('df')
    s.prompt()
    print(s.before)
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)
'''