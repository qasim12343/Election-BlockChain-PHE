import hashlib


class Block:
    def __init__(self, data, previous_hash, previous_block, next_block):
        self.data = data
        self.previous_hash = previous_hash
        self.previous_block = previous_block
        self.next_block = next_block
        self.hash = self.calc_hash()

    def calc_hash(self):
        to_hash = str(self.data) + self.previous_hash
        return hashlib.sha256(to_hash.encode()).hexdigest()

    def get_data(self):
        return self.data

    def get_hash(self):
        return self.hash


class BlockChain:
    def create_genesis_block(self):
        return Block(0, "0", None, None)

    def __init__(self):
        self.head = self.create_genesis_block()
        self.tail = self.head

    def add_block(self, data):
        new_block = Block(data, self.tail.get_hash(), self.tail, None)
        self.tail.next_block = new_block
        self.tail = new_block

    def calculation(self):
        current = self.head
        result = 0
        while current:
            result = current.get_data()+result
            current = current.next_block
        return result

    def assert_correct(self):
        current = self.head
        while current.next_block:
            next_block = current.next_block
            if current.calc_hash() != next_block.previous_hash:
                return False
            current = next_block
        return True


def main():
    blockchain = BlockChain()
    blockchain.add_block(1)
    blockchain.add_block(-1)
    blockchain.add_block(-1)
    blockchain.add_block(5)

    print(blockchain.calculation())
    # print(blockchain.assert_correct())

    # # corrupt a block
    # blockchain.head.next_block.data = "Corrupted Block"
    # print(blockchain.assert_correct())


if __name__ == "__main__":
    main()
