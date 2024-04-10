from phe import paillier

pk, pv = paillier.generate_paillier_keypair()

f = pk.encrypt(4)
t = pk.encrypt(2)
s = f+t
print(s)
print(pv.decrypt(s))
