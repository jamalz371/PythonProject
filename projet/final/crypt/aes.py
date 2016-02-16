from Crypto.Cipher import AES

# on va crypter
key = "my secret key 16"
iv = "my secret iv 16 "
obj = AES.new(key, AES.MODE_CBC, iv)
message = "la belle maison rouge"

bs = 16
padding_length = bs - (len(message) % bs)
# si le message na pas une taille proportionnelle a 16
if not (len(message)%16) == 0:
	message += padding_length * chr(padding_length)
	
ciphertext = obj.encrypt(message)

# ecrire dans fichier
f = open ('test_aes.txt', 'w')
f.write(str(ciphertext))
f.write("\n")
f.write(str(message))
#-------------------------

print("resultat crypte : \n")
print(ciphertext)

print("\n")

# maintenant on va decrypter
obj2 = AES.new(key, AES.MODE_CBC, iv)

message = message[:-padding_length]

plaintext = obj2.decrypt(ciphertext)

print("resultat clair : \n")
print(plaintext)

print("\n")



