from hashlib import blake2b as b,blake2s as c,shake_128 as d,shake_256 as e,pbkdf2_hmac as a,new as g;from base64 import b64decode as h;from sys import argv as i;from itertools import product as j;from time import time as k;import string as l;import sys as m
def G(c) :
	n=0
	while 1:
		n+=1
		for a in j(c,repeat=n):yield a
def H(a):
	b=None
	if y==B(a):return f"[+] {a} is the password !",1
	else:
		if o:b=f"[-] {a} isn't working."
		return b,0
n=0;o=0;p=0;q=0;r=l.ascii_letters+l.digits;s=b'';t=1;u=b'';v=b'';w=0;x=None;y=None;z=print;A=len;F=open;I='utf-8'
try:y=i[-1];x=i[-2]
except:w=1
if "-b" in i:q=1;z("[+] Only bruteforce")
if "-p" in i:p=1;z("[+] Only password list")
if "-v" in i:o=1;z("[+] verbose is active")
if "-b64" in i:
	try:y=h(y).decode()
	except:m.exit("Error with base64")
	z("[+] Base64 is decode")
if "-a" in i :
	try:r=i[i.index("-a")+1]
	except:m.exit("Error with alphabet")
	z("[+] alphabet is use")
if "-s" in i:
	try:s=i[i.index("-s")+1].encode()
	except:m.exit("Error with salt")
	z("[+] salt is use")
if "-i" in i:
	try:t=int(i[i.index("-i")+1])
	except:m.exit("Error with iterations")
	z("[+] iterations is use")
if "-k" in i:
	try:u=i[i.index("-k")+1].encode()
	except:m.exit("Error with key")
	z("[+] key is use")
if "-pe" in i:
	try:v=i[i.index("-pe")+1].encode()
	except:m.exit("Error with person")
	z("[+] person is use")
if "-e" in i:
	try:
		I=i[i.index("-e")+1]
		if not I in ['ascii','big5','big5hkscs','cp037','cp273','cp424','cp437','cp500','cp720','cp737','cp775','cp850','cp852','cp855','cp856','cp857','cp858','cp860','cp861','cp862','cp863','cp864','cp865','cp866','cp869','cp874','cp875','cp932','cp949','cp950','cp1006','cp1026','cp1125','cp1140','cp1250','cp1251','cp1252','cp1253','cp1254','cp1255','cp1256','cp1257','cp1258','cp65001','euc_jp','euc_jis_2004','euc_jisx0213','euc_kr','gb2312','gbk','gb18030','hz','iso2022_jp','iso2022_jp_1','iso2022_jp_2','iso2022_jp_2004','iso2022_jp_3','iso2022_jp_ext','iso2022_kr','latin_1','iso8859_2','iso8859_3','iso8859_4','iso8859_5','iso8859_6','iso8859_7','iso8859_8','iso8859_9','iso8859_10','iso8859_11','iso8859_13','iso8859_14','iso8859_15','iso8859_16','johab','koi8_r','koi8_t','koi8_u','kz1048','mac_cyrillic','mac_greek','mac_iceland','mac_latin2','mac_roman','mac_turkish','ptcp154','shift_jis','shift_jis_2004','shift_jisx0213','utf_32','utf_32_be','utf_32_le','utf_16','utf_16_be','utf_16_le','utf_7','utf_8','utf_8_sig']:w=1
	except:m.exit("Error with encoding")
	z("[+] encoding is use")
if "-le" in i:z("Encodings : "+"; ".join(['ascii','big5','big5hkscs','cp037','cp273','cp424','cp437','cp500','cp720','cp737','cp775','cp850','cp852','cp855','cp856','cp857','cp858','cp860','cp861','cp862','cp863','cp864','cp865','cp866','cp869','cp874','cp875','cp932','cp949','cp950','cp1006','cp1026','cp1125','cp1140','cp1250','cp1251','cp1252','cp1253','cp1254','cp1255','cp1256','cp1257','cp1258','cp65001','euc_jp','euc_jis_2004','euc_jisx0213','euc_kr','gb2312','gbk','gb18030','hz','iso2022_jp','iso2022_jp_1','iso2022_jp_2','iso2022_jp_2004','iso2022_jp_3','iso2022_jp_ext','iso2022_kr','latin_1','iso8859_2','iso8859_3','iso8859_4','iso8859_5','iso8859_6','iso8859_7','iso8859_8','iso8859_9','iso8859_10','iso8859_11','iso8859_13','iso8859_14','iso8859_15','iso8859_16','johab','koi8_r','koi8_t','koi8_u','kz1048','mac_cyrillic','mac_greek','mac_iceland','mac_latin2','mac_roman','mac_turkish','ptcp154','shift_jis','shift_jis_2004','shift_jisx0213','utf_32','utf_32_be','utf_32_le','utf_16','utf_16_be','utf_16_le','utf_7','utf_8','utf_8_sig']));m.exit()
if x in ['crypt','ripemd160','shake_128','sha3_384','sha512_256','sm3','sha512','shake_256','blake2b','mdc2','md5-sha1','sha3_224','sha512_224','sha3_512','sha384','md5','md4','sha224','sha256','sha3_256','blake2s','whirlpool','sha1']:
	if x in ["blake2s","blake2b","shake_128","shake_256"]:
		if x=="blake2b":
			def B(k):return b(k.encode(I),salt=s, key=u,person=v,digest_size=A(y)//2).hexdigest()
		elif x=="blake2s":
			def B(k):return c(k.encode(I), salt=s, key=u, person=v, digest_size=A(y)//2).hexdigest()
		elif x=="shake_128":
			def B(k):return d(k.encode(I)).hexdigest(A(y)//2)
		elif x=="shake_256":
			def B(k):return e(k.encode(I)).hexdigest(A(y)//2)
	elif x in ["sha3_384","sha512_256","sha3_224","sha512_224","sha3_512","sha3_256"]:
		def B(k):return g(x,k.encode(I)).hexdigest()
	elif x=='crypt':
		from crypt import crypt as J
		try:K=y.split('$');s="$"+"$".join(K[1:3]);w=J('a',salt=s)=='*0'
		except:w=0
		def B(k):return J(k,salt=s)
	else:
		if s==b'':
			def B(k):return g(x,k.encode(I)).hexdigest()
		else:
			def B(k):return a(x,k.encode(I),s,t).hex()
else:w=1
if "-h" in i or "-b" in i and "-p" in i or w:z("""Usage : python3 HashCrack.py [Options] <method> <hash>
Options :
	-s <salt> : salt (ascii characters only)
	-i <iterations> : iterations (default = 1)
	-k <key> : key (for blake2d, blake2s) (ascii characters only)
	-pe <person> : person (for blake2s, blake2d) (ascii characters only)
	-b64 : if the hash is encode in base64
	-b : bruteforce only (not with option -p)
	-p : password list only (not with option -b)
	-v : verbose
	-a <alphabet> : alphabet for bruteforce (not with -p)
		can't contains &
	-e <encoding> : encoding
		-le : encodings list (98 encodings)
	-h : help
Methods :
	crypt (hash must be between SIMPLE quot : '<hash>', NOT "<hash>" AND NOT <hash>)
	ripemd160
	shake_128 (no salt, no iterations)
	sha3_384 (no salt, no iterations)
	sha512_256 (no salt, no iterations)
	sm3
	sha512
	shake_256 (no salt, no iterations)
	blake2b (no iterations)
	mdc2
	md5-sha1
	sha3_224 (no salt, no iterations)
	sha512_224 (no salt, no iterations)
	sha3_512 (no salt, no iterations)
	sha384
	md5
	md4
	sha224
	sha256
	sha3_256 (no salt, no iterations)
	blake2s (no iterations)
	whirlpool
	sha1""");m.exit()
if A(B('a'))!=A(y) and x!="crypt":m.exit("Error with hash size")
C=k()
if not q:
	D=input("Filenam for password list or 0 : ");C=k()
	if D!="0":
		f=F(D,"r")
		for D in f.readlines():
			D=D[:-1];E,n=H(D)
			if o and not n:z(E)
			elif n:z(E);break
		f.close()
if not p and not n:
	for D in G(r):
		D="".join(D);E,n=H(D)
		if o and not n:z(E)
		if n:z(E);break
if not n:z("[-] Password not found")
else:f=F("save.txt", "a");f.write(f"{y} :\n	Password : {D}\n	Arguments : {' '.join([a for a in i])}\n\n");f.close()
z(f"This script take : {k()-C} secondes.")
input("Hit enter to exit...")
