#!/usr/bin/python2
import zipfile
import optparse
from threading import Thread
def main():
	parser = optparse.OptionParser("Usage: %prog  " + "-f <zipfile> -d <dictionary>")
	parser.add_option('-f', dest='zname', type='string', help='specify zip file')
	parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
	(options, args) = parser.parse_args()
	if (options.zname == None) | (options.dname == None):
		print parser.usage
		exit(0)
	else:
		zname = options.zname
		dname = options.dname
	zFile = zipfile.ZipFile(zname)
	passfile = open(dname)
	for line in passfile.readlines():
		password = line.strip('\n')
		t = Thread(target=extractFile, args=(zFile, password))
		t.start()
		
def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password)
		print '[+] Password is ' + password + '\n'
	except:
		pass

if __name__ == '__main__':
	main()

