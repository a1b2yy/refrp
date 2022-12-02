import rsa

def rsaEncrypt(str):
    with open('public.pem', "rb") as publickfile:
        p = publickfile.read()
        pubkey = rsa.PublicKey.load_pkcs1(p)
        #print(pubkey)

    with open('private.pem', "rb") as privatefile:
        p = privatefile.read()
        privkey = rsa.PrivateKey.load_pkcs1(p)
        #print(privkey)
    #print("pub: ", pubkey)
    #print("priv: ", privkey)
    content = str.encode('utf-8')
    crypto = rsa.encrypt(content, pubkey)
    return (crypto, privkey)

def rsaDecrypt(str, pk):
    content = rsa.decrypt(str, pk)
    con = content.decode('utf-8')
    return con


(a, b) = rsaEncrypt("iodsrjguisehguihrtiugjeirujgasjguiesnrieungiushntrgiuhnreiugniusrehnuigsntriuneruihgiuerhniunruiesngiureishngiunreisugnrukesngui")
content = rsaDecrypt(a, b)
print('解密后明文：'+ content)