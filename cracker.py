import crypt
import hashlib

'''
def testPass(cryptPass):
	salt = cryptPass[0:2]

	dictFile = open("dictionary.txt", "r")
	for word in dictFile:
		word = word.rstrip('\n')
		cryptWord = crypt.crypt(word, salt)
		if cryptWord == cryptPass:
			print '[+] Found Password: ' + word
			return
	print '[-] Password not found.'

def main():
	passFile = open("passwords.txt", "r")
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(":")[0]
			cryptPass = line.split(":")[1].strip(' ')
			print '[+] Cracking password for user: ' + user
			testPass(cryptPass)
'''
def testPass(cryptPass):
	salt = cryptPass[3:11]
	word = cryptPass[17:104]
	dictFile = open("dictionary.txt", "r")
	for word in dictFile:
		word = word.rstrip('\n')
		cryptWord = hashlib.sha512(salt + word).digest()
		print cryptWord
		if cryptWord == cryptPass:
			print '[+] Found Password: ' + word
			return
	print '[-] Password not found.'

def main():
	passFile = open("passwords_2.txt", "r")
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(":")[0]
			cryptPass = line.split(":")[1].strip(' ')
			print '[+] Cracking password for user: ' + user
			testPass(cryptPass)	

if __name__ == "__main__":
	main()
