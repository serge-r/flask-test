#!flask/bin/python3

import opnssl

ca = opnssl.CA(CAPath="/home/serge/test-app/testCA/easyrsa3/pki/",
			   treePath="/home/serge/test-app/testCA/easyrsa3")

print(ca.certs)

ca.revokeCert("client1")
