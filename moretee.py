
# 加密
import rsa
(pubkey, privkey) = rsa.newkeys(2048)
pk = pubkey
 
bytes_value = b"haha" * 30
length = len(bytes_value)
 
val_list = []
for i in range(0, length, 245):
    tpl = bytes_value[i:i + 245]
    val = rsa.encrypt(tpl, pk)
    val_list.append(val)
 
ret = b''.join(val_list)
 
# 解密
pk = privkey
 
length = len(ret)
val_list = []
for i in range(0, length, 256):
    tpl = ret[i:i + 256]
    val = rsa.decrypt(tpl, pk)
    val_list.append(val)
 
ret = b''.join(val_list)