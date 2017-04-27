#!flask/bin/python3

import opnssl

ca = opnssl.CA(CAPath="/home/serge/repos/easy-rsa/easyrsa3/pki",
	    treePath="/home/serge/repos/easy-rsa/easyrsa3")

res = ca.CAInit()
print ("Satus {} errors: {}". format(res[0], res[1]))

print ("Certificates:")
for cert in ca.getCerts() :
	for key,value in cert.items() :
		print (key, value)
	print ("\n")

result = ca.createCert("client2",needPass=False)


print(result[0])

#print(result[1].decode())
