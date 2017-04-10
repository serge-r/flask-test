#!flask/bin/python

import os,sys
import subprocess
import random

PASS_LEN=12

class CA:
	'''
	Defines a new CA instance
	'''
	def __init__(self,CAPath='./pki',treePath='./easyrsa3'):
		'''
		Init CA
		Get a certs from index.txt
		'''
		os.chdir(treePath)
		indexFile = CAPath + "/index.txt"
		# Add a check filePath to correct CA
		self.certs = self._parseIndex(indexFile)
		self.exePath = treePath
			
	def _parseIndex(self,filePath):
		''' 
		Read index.txt file from CA database,
		parse a certificate data
		returns a list of certificates
			TODO: add a exception to test a files exists
		'''
		certs = []
		with open(filePath, "r") as indexFile:
			lines = indexFile.readlines()
			for line in lines:
				res = line.split('\t')
				print (len(res))
				if (len(res) > 2):
					certs.append({'status': 	res[0],
								  'expire': 	res[1],
								  'revokeDate': res[2],
								  'serial': 	res[3],
								  'fileName':	res[4],
								  'subject':	self._parseSubject(res[5])})
		return certs

	def _parseSubject(self,subjectLine):
		'''
		Parse a certificate subject field
		Returns a dict
		'''
		subject = {}
		for line in subjectLine.split('/'):
			res = line.split('=')
			len(res)
			if (len(res) >= 2):
				subject[res[0]] = res[1]
	
		return subject

	def _randomPass(len=PASS_LEN):
		""" Creates and return random string 
		Liters == letters
		"""
		digits = "0123456789"
		liters = "abcdefghijklmnopqrstuvwxyz+--()"
		upLiters = liters.upper()

		literList = list(liters + digits + upLiters)
		random.shuffle(literList)
		password = "".join(random.choice(literList) for x in xrange(len))

		return password

	def createCert(self,certCN,needPass=True):
		'''
		TODO: add a check
		'''
		if (not needPass):
			cmd = [self.exePath,'build-full-client',certCN,'nopass']
			p = subprocess.Popen(cmd,stdout=subprocess.STDOUT,stdin=subprocess.PIPE,stderr=subprocess.STDOUT)
			grep_stdout = p.communicate()[0]

		else:
			cmd = [self.exePath,'build-full-client',certCN]
			password = self._randomPass()
			sentString = password + '\n' + password + '\n'
			p = subprocess.Popen(cmd,stdout=subprocess.STDOUT,stdin=subprocess.PIPE,stderr=subprocess.STDOUT)
			grep_stdout = p.communicate(input=sentString.encode('ascii'))[0]

		return_code = p.wait()
		return (return_code,grep_stdout)

	def revokeCert(self,certCN):
		'''
		TODO: add a check
		'''
		p = subprocess.Popen([self.exePath, 'revoke', certCN],stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.STDOUT)
		grep_stdout = p.communicate(input=b'yes\n')[0]
		return_code = p.wait()

		return (return_code,grep_stdout)

