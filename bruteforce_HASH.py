from hashlib import algorithms_available, blake2b, blake2s, shake_128, shake_256, pbkdf2_hmac, new 
from binascii import hexlify
from base64 import b64decode
from sys import argv
from itertools import product
from time import time
import string
import sys

def bruteforce (caracteres) :
	n = 0
	while True :
		n += 1
		for a in product(caracteres, repeat = n) :
			yield a

def unhash (password) :
	phrase = None
	if hash_ == hash2(password) :
		return f"[+] {password} is the password !", True
	else :
		if verbose :
			phrase = f"[-] {password} isn't working."
		return phrase, False	

is_unhash = False
verbose = False
only_password = False
only_bruteforce = False
alphabet = string.ascii_letters + string.digits
salt = b''
iterations = 1
key = b''
person = b''
error = False
method = None
hash_ = None
encoding = 'utf-8'

try :
	hash_ = argv[-1]
	method = argv[-2]
except :
	error = True

if "-b" in argv :
	only_bruteforce = True
	print("[+] Only bruteforce")
if "-p" in argv :
	only_password = True
	print("[+] Only password list")
if "-v" in argv :
	verbose = True
	print("[+] Verbose is active")
if "-b64" in argv :
	try :
		hash_ = b64decode(hash_).decode()
	except :
		sys.exit("Erreur de base64")
	print("[+] Base64 is decode")
if "-a" in argv :
	try :
		alphabet = argv[argv.index("-a") + 1]
	except :
		sys.exit("Erreur avec l'alphabet")
	print("[+] alphabet is use")
if "-s" in argv :
	try :
		salt = argv[argv.index("-s") + 1].encode()
	except :
		sys.exit("Erreur avec le salt")
	print("[+] salt is use")
if "-i" in argv :
	try :
		iterations = int(argv[argv.index("-i") + 1])
	except :
		sys.exit("Erreur avec l'iterations")
	print("[+] iterations is use")
if "-k" in argv :
	try :
		key = argv[argv.index("-k") + 1].encode()
	except :
		sys.exit("Erreur avec la clés")
	print("[+] key is use")
if "-pe" in argv :
	try :
		person = argv[argv.index("-pe") + 1].encode()
	except :
		sys.exit("Error with person")
	print("[+] person is use")
if "-e" in argv :
	try :
		encoding = argv[argv.index("-e") + 1]
		if not encoding in ['ascii', 'big5', 'big5hkscs', 'cp037', 'cp273', 'cp424', 'cp437', 'cp500', 'cp720',
						'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp856', 'cp857', 'cp858', 'cp860', 'cp861',
						'cp862', 'cp863', 'cp864', 'cp865', 'cp866', 'cp869', 'cp874', 'cp875', 'cp932', 'cp949', 
						'cp950', 'cp1006', 'cp1026', 'cp1125', 'cp1140', 'cp1250', 'cp1251', 'cp1252', 'cp1253', 
						'cp1254', 'cp1255', 'cp1256', 'cp1257', 'cp1258', 'cp65001', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213',
						'euc_kr', 'gb2312', 'gbk', 'gb18030', 'hz', 'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2',
						'iso2022_jp_2004', 'iso2022_jp_3', 'iso2022_jp_ext', 'iso2022_kr', 'latin_1', 'iso8859_2',
						'iso8859_3', 'iso8859_4', 'iso8859_5', 'iso8859_6', 'iso8859_7', 'iso8859_8', 'iso8859_9',
						'iso8859_10', 'iso8859_11', 'iso8859_13', 'iso8859_14', 'iso8859_15', 'iso8859_16', 'johab',
						'koi8_r', 'koi8_t', 'koi8_u', 'kz1048', 'mac_cyrillic', 'mac_greek', 'mac_iceland', 'mac_latin2',
						'mac_roman', 'mac_turkish', 'ptcp154', 'shift_jis', 'shift_jis_2004', 'shift_jisx0213', 'utf_32',
						'utf_32_be', 'utf_32_le', 'utf_16', 'utf_16_be', 'utf_16_le', 'utf_7', 'utf_8', 'utf_8_sig'] :
			error = True
	except :
		sys.exit("Error with encoding")
	print("[+] person is use")
if "-le" in argv :
	print("Encodings : " + "; ".join(['ascii', 'big5', 'big5hkscs', 'cp037', 'cp273', 'cp424', 'cp437', 'cp500', 'cp720',
						'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp856', 'cp857', 'cp858', 'cp860', 'cp861',
						'cp862', 'cp863', 'cp864', 'cp865', 'cp866', 'cp869', 'cp874', 'cp875', 'cp932', 'cp949', 
						'cp950', 'cp1006', 'cp1026', 'cp1125', 'cp1140', 'cp1250', 'cp1251', 'cp1252', 'cp1253', 
						'cp1254', 'cp1255', 'cp1256', 'cp1257', 'cp1258', 'cp65001', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213',
						'euc_kr', 'gb2312', 'gbk', 'gb18030', 'hz', 'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2',
						'iso2022_jp_2004', 'iso2022_jp_3', 'iso2022_jp_ext', 'iso2022_kr', 'latin_1', 'iso8859_2',
						'iso8859_3', 'iso8859_4', 'iso8859_5', 'iso8859_6', 'iso8859_7', 'iso8859_8', 'iso8859_9',
						'iso8859_10', 'iso8859_11', 'iso8859_13', 'iso8859_14', 'iso8859_15', 'iso8859_16', 'johab',
						'koi8_r', 'koi8_t', 'koi8_u', 'kz1048', 'mac_cyrillic', 'mac_greek', 'mac_iceland', 'mac_latin2',
						'mac_roman', 'mac_turkish', 'ptcp154', 'shift_jis', 'shift_jis_2004', 'shift_jisx0213', 'utf_32',
						'utf_32_be', 'utf_32_le', 'utf_16', 'utf_16_be', 'utf_16_le', 'utf_7', 'utf_8', 'utf_8_sig']))
	sys.exit()

if method in ['ripemd160', 'shake_128', 'sha3_384', 'sha512_256', 'sm3', 'sha512', 'shake_256', 'blake2b', 'mdc2', 
		'md5-sha1', 'sha3_224', 'sha512_224', 'sha3_512', 'sha384', 'md5', 'md4', 'sha224', 'sha256', 'sha3_256', 'blake2s', 'whirlpool', 'sha1'] :

	if method in ["blake2s", "blake2b", "shake_128", "shake_256"] :
		if method == "blake2b" :
			def hash2 (password) :
				return blake2b(password.encode(encoding), salt = salt, key = key, person = person, digest_size = len(hash_)//2).hexdigest()
		elif method == "blake2s" :
			def hash2 (password) :
				return blake2s(password.encode(encoding), salt = salt, key = key, person = person, digest_size = len(hash_)//2).hexdigest()
		elif method == "shake_128" :
			def hash2 (password) :
				return shake_128(password.encode(encoding)).hexdigest(len(hash_)//2)
		elif method == "shake_256" :
			def hash2 (password) :
				return shake_256(password.encode(encoding)).hexdigest(len(hash_)//2)
	elif method in ["sha3_384", "sha512_256", "sha3_224", "sha512_224", "sha3_512", "sha3_256"] :
		def hash2 (password) :
			return new(method, password.encode(encoding)).hexdigest()
	else :
		if salt == b'' :
			def hash2 (password) :
				return new(method, password.encode(encoding)).hexdigest()
		else :
			def hash2 (password) :
				return pbkdf2_hmac(method, password.encode(encoding), salt, iterations).hex()
else :
	error = True

if "-h" in argv or "-b" in argv and "-p" in argv or error :
	print("""Usage : python3 HashCrack.py [Options] <method> <hash>
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
		-le : list des encodings (98) possibles
	-h : help
Methods :
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
	sha1""")
	sys.exit()

if len(hash2('a')) != len(hash_) :
	sys.exit("Error with hash size")

debut = time()

if not only_bruteforce :
	passwords = input("Entrez le fichier contenant les passwords ou entrez 0 : ")
	debut = time()
	if passwords != "0" :
		f = open(passwords, "r")

		for password in f.readlines() :
			password = password[:-1]
			phrase, is_unhash = unhash(password)

			if verbose and not is_unhash :
				print(phrase)
			elif is_unhash :
				print(phrase)
				break
			
		f.close()

if not only_password and not is_unhash :
	for password in bruteforce(alphabet) :
		password = "".join(password)
		phrase, is_unhash = unhash(password)
		if verbose and not is_unhash :
			print(phrase)

		if is_unhash :
			print(phrase)
			break

if not is_unhash :
	print("[-] Password not found")
else :
	f = open("save.txt", "a")
	f.write(f"{hash_} :\n	Password : {password}\n	Arguments : {' '.join([a for a in argv])}\n\n")
	f.close()
print(f"Le script à mis : {time() - debut} secondes.")
input("Tapez sur entrée pour quitter...")