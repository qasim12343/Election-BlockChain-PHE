from phe import paillier
import Blockchain


class Election:

    def __init__(self):
        self.global_blockChain = Blockchain()

    def get_global_blockChain(self):
        return self.global_blockChain

    def add_localBlockChain(self):
        pass


# Election()
# localblockChain1 = Blockchain()
pk, pv = paillier.generate_paillier_keypair()
t = pk.encrypt(2)
print(t)
f = pk.encrypt(4)
print(pv.decrypt(t+f))
