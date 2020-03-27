# Bruteforce
Petits scripts de bruteforce en python (version 3.8, avec une version plus ancienne il est possible que certains hashs et certains encodings ne soit pas supportés), amusez vous bien !

Le premier script est un script de bruteforce de hash :
  - Utilisations :
    - Générale : CrackHackx86.py [options] &lt;method&gt; &lt;hash&gt;
  
    - Simple :
      - CrackHackx86.py md5 b706835de79a2b4e80506f582af3676a
      
    - Uniquement avec un dictionnaire de mot de passe :
      - CrackHackx86.py -p sha1 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
      
    - Uniquement avec bruteforce (revient à lancer la commande simple et entrer 0 à la place d'un fichier) :
      - CrackHackx86.py -b shake_256 8927140c0e1daa0769590edc8d104d9b8b51c77707681c4738
      
    - Avec un alphabet particulier :
      - CrackHackx86.py -a 0123456789 md5-sha1 85d6066ab1d290b884a7f171042dc1ca67c68af40ca2b7bbae5a4d47564fd9fe80c783f1
      
    - Avec un encoding particulier (crack d'un mot de passe windows) :
      - CrackHackx86.py -e utf_16_le md4 554403f0a69c96f2e0f76196d475b447
    
    - Avec un salt :
      - CrackHackx86.py -s Secret sha512 5dd2e9c7435091e83e19a645954b4e361094067d73c23949d96ac46c991dd8dabac378e6ef82fd11af09c0674b5f80603c4ee351062afc799cbfb9973bd6e035
      
    - Avec des itérations :
      - CrackHackx86.py -i 10000 whirlpool 124d398221ab0c468e6a6228063a1edbe5a19d3e2d934c4735b3331fb26a427a9e69ca0ba794af673e948032755b39ad911dc490d9540f8fa76f8d9976fc3132

    - En base64 :
      - CrackHackx86.py -b64 sha512_224 M2Q1YTBiNzQyZjRjNjFkMzE1YzZjZTg2NDU3YTlmYTMwOTAzODgwZDMwNTU4YzY4Y2U0NzEzYjM=
      
    - Avec une clés (blake2s et blake2b uniquement) :
      - CrackHackx86.py -k Secret blake2b 788c180f73d12239896bf9e49ecd38f961e5100217bab232
      
    - Avec l'option person (blake2s et blake2b uniquement) :
      - CrackHackx86.py -pe Secret blake2s b15fdeda739a91e23e68a604498c828e7c1c4895f5953d80
      
  - Mot de passe Windows :
    - Lorsque vous récupérez les hashs de vos mots de passe Windows vous les trouverez sous cette forme :
      - John Doe:1000:aad3b435b51404eeaad3b435b51404ee:b9f917853e3dbf6e6831ecce60725930:::
    - Enfaite de manière générale ils sont visible comme ça :
      - NomUtilisateur:NombreCorrespondantAuTypeDeCompte:UnHash:MD4_duMotDePasse(encoding : UTF-16le):::
      
  - Mot de passe Linux :
    - Lorsque vous récupérez les hashs de vos mots de passe Linuw vous les trouverez sous cette forme :
      - John:$6$ABCDEFGHIJKLMNOP$XICo1SGZRjxn3r2NvLTfwPU4dJmg7iH6BtkD9YyVcu0F2wJSIgnCUBW7iu065cvrlM/d3jZOby.mEoftNLVRHX:1832;0:9997:8:::
    - Voila comment il est décomposé :
      - Nom:Hash:Nombre1:Nombre2:Nombre3:::
      - Le hash se décompose de la manière suivante :
        - $typeDeHash$salt$hash
    - Ils ne sont décryptable qu'avec la version Linux :
      - CrackHashLinux86.py crypt $6$WqWNz4bnyBa.ZqKQ$tdKA2jh5eAkzg4f2zjdxNg8wk3Oq6iTv/7jbygF8cRmyRLvblS/swx9nTKh3/KE1I6DG7oMr3bvBsnLTFITH91
    - Le mot de passe Linux prend 100 fois plus de temps (en moyenne) à être retrouvé que le mot de passe Windows (le même).

Le second script que je propose permet d'extraire un fichier zip crypté et de récupérer le mot de passe :
  - Utilisations :
    - Générale : CrackZipx64.py [options]
    
    - Verbose : CrackZipx64.py -v (non recommandée car elle prend plus de temps)
    
    - Dictionnaire uniquement : CrackZipx64.py -p
    
    - Bruteforce uniquement : CrackZipx64.py -b
    
    - Avec un alphabet particulier : CrackZipx64.py -a
    
    - Aide : CrackZipx64.py -h
    
A venir (probablement) : bruteforce ssh, bruteforce ftp, bruteforce HTTP basic auth.
    
    
