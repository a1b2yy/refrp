# -*- coding: utf-8 -*-
import rsa

# rsa加密
def rsaEncrypt(str):
    # 生成公钥、私钥
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
    # 明文编码格式
    content = str.encode('utf-8')
    # 公钥加密
    crypto = rsa.encrypt(content, pubkey)
    return (crypto, privkey)


# rsa解密
def rsaDecrypt(str, pk):
    # 私钥解密
    content = rsa.decrypt(str, pk)
    con = content.decode('utf-8')
    return con


(a, b) = rsaEncrypt("iodsrjguisehguihrtiugjeirujgasjguiesnrieungiushntrgiuhnreiugniusrehnuigsntriuneruihgiuerhniunruiesngiureishngiunreisugnrukesngui")
#print(a)
content = rsaDecrypt(a, b)
print('解密后明文：'+ content)