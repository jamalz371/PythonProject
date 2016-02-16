import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random_generator = Random.new().read
key = RSA.generate(2048, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange 
print publickey
print("\n")
print key
encrypted = publickey.encrypt('encrypt this message', 32)
#message to encrypt is in the above line 'encrypt this message'

print 'encrypted message : \n', encrypted #ciphertext
f = open ('encryption.txt', 'w')
f.write(str(encrypted)) #write ciphertext to file
f.close()

#decrypted code below

f = open('encryption.txt', 'r')
message = f.read()

decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

print 'decrypted message : \n', decrypted

f = open ('encryption.txt', 'w')
f.write(str(message))
f.write(str(decrypted))
f.close()


