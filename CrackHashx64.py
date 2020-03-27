U
    ;!~^�  �                f   @   s  d dl mZmZmZmZm	Z
mZ d dlmZ d dlmZ d dlmZ d dlmZ d dlZd dlZdd� Zd	d
� Zd Zd Zd Zd Z ej!ej" Z#dZ$dZ%dZ&dZ'd Z(dZ)dZ*e+Z,e-Z.e/Z0dZ1zed Z*ed Z)W n   dZ(Y nX dekr�dZ e,d� dek�rdZe,d� dek�rdZe,d� dek�rXzee*��2� Z*W n   e�3d� Y nX e,d� dek�r�zee�4d�d  Z#W n   e�3d� Y nX e,d� dek�r�zee�4d�d  �5� Z$W n   e�3d� Y nX e,d� dek�r ze6ee�4d�d  �Z%W n   e�3d � Y nX e,d!� d"ek�rdzee�4d"�d  �5� Z&W n   e�3d#� Y nX e,d$� d%ek�r�zee�4d%�d  �5� Z'W n   e�3d&� Y nX e,d'� d(ek�r�z$ee�4d(�d  Z1e1d)k�r�dZ(W n   e�3d*� Y nX e,d+� d,ek�r�e,d-d.�7d/d0d1d2d3d4d5d6d7d8d9d:d;d<d=d>d?d@dAdBdCdDdEdFdGdHdIdJdKdLdMdNdOdPdQdRdSdTdUdVdWdXdYdZd[d\d]d^d_d`dadbdcdddedfdgdhdidjdkdldmdndodpdqdrdsdtdudvdwdxdydzd{d|d}d~dd�d�d�d�d�d�d�d�d�d�d�d�d�d�d�d�d�gb� � e�3�  e)d�k�rte)d�k�rBe)d�k�rd�d�� Z8n:e)d�k�rd�d�� Z8n&e)d�k�r.d�d�� Z8ne)d�k�rrd�d�� Z8n0e)d�k�rVd�d�� Z8ne$dk�rjd�d�� Z8nd�d�� Z8ndZ(d�ek�s�dek�r�dek�s�e(�r�e,d�� e�3�  e.e8d���e.e*�k�r�e�3d�� e� Z9e �sTe:d��Z;e� Z9e;d�k�rTe0e;d��Z<e<�=� D ]HZ;e;dd� Z;ee;�\Z>Ze�r4e�s4e,e>� ne�re,e>�  �qL�qe<�?�  e�s�e�s�ee#�D ]DZ;d��7e;�Z;ee;�\Z>Ze�r�e�s�e,e>� e�rhe,e>�  �q��qhe�s�e,d�� n>e0d�d��Z<e<�@e*� d�e;� d�d��7d�d�� eD ��� d��� e<�?�  e,d�e� e9 � d��� e:d�� dS )��    )�blake2b�blake2s�	shake_128�	shake_256�pbkdf2_hmac�new)�	b64decode)�argv)�product)�timeNc                 c   s*   d}|d7 }t | |d�D ]
}|V  qqd S )Nr   �   )�repeat)�j)�c�n�a� r   �CrackHash.py�G   s     r   c                 C   s<   d }t t| �kr d| � d�dfS tr0d| � d�}|dfS d S )Nz[+] z is the password !r   z[-] z isn't working.r   )�y�B�o)r   �br   r   r   �H   s      r   �    r   zutf-8����������z-bz[+] Only bruteforcez-pz[+] Only password listz-vz[+] verbose is activez-b64zError with base64z[+] Base64 is decodez-azError with alphabetz[+] alphabet is usez-szError with saltz[+] salt is usez-izError with iterationsz[+] iterations is usez-kzError with keyz[+] key is usez-pezError with personz[+] person is usez-e)b�ascii�big5�	big5hkscs�cp037�cp273�cp424�cp437�cp500�cp720�cp737�cp775�cp850�cp852�cp855�cp856�cp857�cp858�cp860�cp861�cp862�cp863�cp864�cp865�cp866�cp869�cp874�cp875�cp932�cp949�cp950�cp1006�cp1026�cp1125�cp1140�cp1250�cp1251�cp1252�cp1253�cp1254�cp1255�cp1256�cp1257�cp1258�cp65001�euc_jp�euc_jis_2004�euc_jisx0213�euc_kr�gb2312�gbk�gb18030�hz�
iso2022_jp�iso2022_jp_1�iso2022_jp_2�iso2022_jp_2004�iso2022_jp_3�iso2022_jp_ext�
iso2022_kr�latin_1�	iso8859_2�	iso8859_3�	iso8859_4�	iso8859_5�	iso8859_6�	iso8859_7�	iso8859_8�	iso8859_9�
iso8859_10�
iso8859_11�
iso8859_13�
iso8859_14�
iso8859_15�
iso8859_16�johab�koi8_r�koi8_t�koi8_u�kz1048�mac_cyrillic�	mac_greek�mac_iceland�
mac_latin2�	mac_roman�mac_turkish�ptcp154�	shift_jis�shift_jis_2004�shift_jisx0213�utf_32�	utf_32_be�	utf_32_le�utf_16�	utf_16_be�	utf_16_le�utf_7�utf_8�	utf_8_sigzError with encodingz[+] encoding is usez-lezEncodings : z; r   r   r   r    r!   r"   r#   r$   r%   r&   r'   r(   r)   r*   r+   r,   r-   r.   r/   r0   r1   r2   r3   r4   r5   r6   r7   r8   r9   r:   r;   r<   r=   r>   r?   r@   rA   rB   rC   rD   rE   rF   rG   rH   rI   rJ   rK   rL   rM   rN   rO   rP   rQ   rR   rS   rT   rU   rV   rW   rX   rY   rZ   r[   r\   r]   r^   r_   r`   ra   rb   rc   rd   re   rf   rg   rh   ri   rj   rk   rl   rm   rn   ro   rp   rq   rr   rs   rt   ru   rv   rw   rx   ry   rz   r{   r|   r}   r~   )Z	ripemd160r   �sha3_384�
sha512_256Zsm3�sha512r   r   Zmdc2zmd5-sha1�sha3_224�
sha512_224�sha3_512�sha384Zmd5Zmd4Zsha224Zsha256�sha3_256r   Z	whirlpoolZsha1)r   r   r   r   r   c                 C   s$   t | �t�ttttt�d d��� S �N�   )Zsalt�keyZperson�digest_size)	r   �encode�I�s�u�v�Ar   �	hexdigest��kr   r   r   r   5   r   r   r   c                 C   s$   t | �t�ttttt�d d��� S r�   )	r   r�   r�   r�   r�   r�   r�   r   r�   r�   r   r   r   r   7   r   r   c                 C   s   t | �t���tt�d �S �Nr�   )�dr�   r�   r�   r�   r   r�   r   r   r   r   9   r   r   c                 C   s   t | �t���tt�d �S r�   )�er�   r�   r�   r�   r   r�   r   r   r   r   ;   r   )r   r�   r�   r�   r�   r�   c                 C   s   t t| �t���� S �N��g�xr�   r�   r�   r�   r   r   r   r   =   r   c                 C   s   t t| �t���� S r�   r�   r�   r   r   r   r   @   r   c                 C   s   t t| �t�tt��� S r�   )r   r�   r�   r�   r�   �t�hexr�   r   r   r   r   B   r   z-haF  Usage : python3 HashCrack.py [Options] <method> <hash>
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
	sha1r   zError with hash sizez!Filenam for password list or 0 : �0�r� z[-] Password not foundzsave.txtz :
	Password : z
	Arguments : � c                 C   s   g | ]}|�qS r   r   )�.0r   r   r   r   �
<listcomp>|   s     r�   z

zThis script take : z
 secondes.zHit enter to exit...)AZhashlibr   r   r   r   r   r�   r   r�   r   r   r   r�   �base64r   �h�sysr	   �i�	itertoolsr
   r   r   r�   �string�l�mr   r   r   r   �p�q�ascii_letters�digitsr�   r�   r�   r�   r�   �wr�   r   �print�z�lenr�   �open�Fr�   �decode�exit�indexr�   �int�joinr   �C�input�D�f�	readlines�E�close�writer   r   r   r   �<module>   s                           
  
  
  
  
  
  
  
  
  

  
 � 














$ & 
 

  
  

    
 

 , 