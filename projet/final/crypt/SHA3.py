import hashlib
import sha3

s = sha3.SHA3512()

nom = s.name
print 'nom : ', nom

taille = s.digest_size
print 'taille : ', taille

s.update('la belle voiture rouge')

resultat = s.hexdigest()

print 'resultat :', resultat

