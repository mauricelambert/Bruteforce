from zipfile import ZipFile, is_zipfile
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

def unzip (zip_file, password) :
	phrase = None
	try :
		zip_file.extractall(pwd = password.encode())
		return f"[+] {password} is the password ! ZipFile is decrypt !", True
	except :
		if verbose :
			phrase = f"[-] {password} isn't working."
		return phrase, False	

is_unzip = False
verbose = False
only_password = False
only_bruteforce = False
alphabet = string.ascii_letters + string.digits

if "-h" in argv or "-b" in argv and "-p" in argv :
	print("""Options :
	-b : bruteforce only (not with option -p)
	-p : password list only (not with option -b)
	-v : verbose
	-a <alphabet> : alphabet for bruteforce (not with -p)
		can't contains &
	-h : help""")
	sys.exit()

if "-b" in argv :
	only_bruteforce = True
	print("[+] Only bruteforce")
if "-p" in argv :
	only_password = True
	print("[+] Only password list")
if "-a" in argv :
	try :
		alphabet = argv[argv.index("-a") + 1]
	except :
		sys.exit("Erreur avec l'alphabet")
	print("[+] alphabet is use")
if "-v" in argv :
	verbose = True
	print("[+] Verbose is active")

if not "-h" in argv :
	file = input("Entrez le nom de votre fichier zip : ")
	if not is_zipfile(file) :
		sys.exit("Erreur le fichier n'est pas un fichier zip")
	zip_file = ZipFile(file)

debut = time()

if not only_bruteforce :
	passwords = input("Entrez le fichier contenant les passwords ou entrez 0 : ")
	debut = time()
	if passwords != "0" :
		f = open(passwords, "r")

		for password in f.readlines() :
			password = password[:-1]
			phrase, is_unzip = unzip(zip_file, password)

			if verbose and not is_unzip :
				print(phrase)
			elif is_unzip :
				print(phrase)
				break
			
		f.close()

if not only_password and not is_unzip :
	for password in bruteforce(alphabet) :
		password = "".join(password)
		phrase, is_unzip = unzip(zip_file, password)
		if verbose and not is_unzip :
			print(phrase)

		if is_unzip :
			print(phrase)
			break

if not is_unzip :
	print("[-] Password not found")
print(f"Le script à mis : {time() - debut} secondes.")
input("Tapez sur entrée pour quitter...")
