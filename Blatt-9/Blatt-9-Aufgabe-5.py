import binascii

e = 2**16 + 1
n = int("00:9b:09:f3:ca:d9:8f:c3:9c:a9:4a:e8:fa:fe:68:0e:b7:69:bc:4b:3e:c7:27:a6:f3:3f:27:63:72:c8:68:b7:1a:c7:6d:70:0f:12:06:cd:31:72:bc:a7:fc:a5:f3:a0:02:6a:ed:26:e8:1f:5d:03:6d:c6:af:01:44:28:b0:c3:2d:91:74:cc:2b:ef:5c:70:77:9d:09:b6:fa:1f:ec:4e:29:91:7e:2a:28:46:a8:22:f2:c5:59:10:86:f8:62:b1:ee:1b:99:09:1d:82:a4:72:3d:85:3e:0f:14:00:bd:41:54:7c:21:0e:6f:b0:c1:ac:1e:1a:f3:23:92:e9:7b:0a:b2:46:18:0d:a1:e1:ae:9a:f2:b8:96:53:85:ce:85:b2:03:ed:b7:22:98:b9:76:f8:2d:04:ce:f6:b3:b4:cc:43:75:ee:07:f7:f6:15:49:bc:b3:d7:18:e5:86:e3:77:ac:6f:1e:92:0f:a0:7d:ac:04:42:f5:7e:53:fc:8f:95:af:a5:01:5f:7e:a8:b0:01:3a:ad:94:24:69:57:38:ad:8d:d7:0c:27:6b:89:c7:fa:69:71:04:4a:8e:28:25:9b:f0:58:65:23:53:ec:c7:2c:4e:af:b9:32:d9:de:75:fa:e8:4a:70:13:9c:79:7e:b2:36:40:3a:e4:d4:35:ef:07:a1:59".replace(':', ''), 16)
s = open('sig.bin', 'rb',).read()
shex = binascii.b2a_hex(s)
print(shex)

sInt = int(shex, 16)
t = pow(sInt,e,n)

print(t)
print('%n' % t)