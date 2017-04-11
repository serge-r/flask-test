#!flask/bin/python3

import opnssl

ca = opnssl.CA(CAPath="/home/serge/test-app/testCA/easyrsa3/pki/",
			   treePath="/home/serge/test-app/testCA/easyrsa3")

print(ca.certs)

result = ca.revokeCert("client1")

#print(result[0])

#print(result[1].decode())
