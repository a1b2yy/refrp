import rsa
(pubkey, privkey) = rsa.newkeys(2048)

pub = pubkey.save_pkcs1()
pubfile = open('public.pem', 'wb')
pubfile.write(pub)
pubfile.close()

pri = privkey.save_pkcs1()
prifile = open('private.pem', 'wb')
prifile.write(pri)
prifile.close()
#