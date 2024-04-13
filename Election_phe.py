from phe import paillier
from Blockchain import BlockChain
import os


class Election:

    def __init__(self):
        self.global_blockChain = BlockChain("G")
        self.pk, self.pv = paillier.generate_paillier_keypair()

    def get_global_blockChain(self):
        return self.global_blockChain

    def add_localBlockChain(self):
        bc = BlockChain("L")
        bc.add_block(self.pk.encrypt(0))
        self.get_global_blockChain().add_block(bc)

        return bc

    def vote(self, local_bc, vot: int):
        encrypted_vote = self.pk.encrypt(vot)
        local_bc.add_block(encrypted_vote)

    def get_pv(self):
        return self.pv


def main():

    Elc = Election()
    lbc1 = Elc.add_localBlockChain()
    lbc2 = Elc.add_localBlockChain()
    lbc3 = Elc.add_localBlockChain()
    lbc4 = Elc.add_localBlockChain()
    lbc5 = Elc.add_localBlockChain()
    pv = Elc.get_pv()
    number_of_bc = Elc.get_bc_number()
    while True:
        bc = lbc1
        inp = input(
            "Enter CityCode and your vote\t\t\tEnter 0 for exit\n")
        if inp == "0":
            break
        try:
            city_code, vot = map(int, inp.split())
            if vot != 1 & vot != -1:
                raise Exception()
            if city_code == 2:
                bc = lbc2
            elif city_code == 3:
                bc = lbc3
            elif city_code == 4:
                bc = lbc4
            elif city_code == 5:
                bc = lbc5

            os.system('cls')
            Elc.vote(bc, vot)
        except:
            print("faild")
    os.system('cls')
    result = Elc.get_global_blockChain().calculation()
    r = pv.decrypt(result)
    winner = ''
    if r < 0:
        winner = 'B'
    elif r > 0:
        winner = 'A'
    else:
        winner = 'draw'
    print(f"Result  = {r}\nWinner is {winner}")


if __name__ == "__main__":
    main()
