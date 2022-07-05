import hashlib


# Node in the linked list
class Block:
    def __init__(self, data, previous_hash):
        self.hash = hashlib.sha256()
        self.previous_hash = previous_hash
        self.nonce = 0 # numb that is incremented to generate the has that suits our need
        self.data = data

    def mine(self, difficulty):
        self.hash.update(str(self).encode('utf-8'))
        while int(self.hash.hexdigest(), 16) > 2**(256 - difficulty):
            self.nonce += 1
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode('utf-8'))

    def __str__(self):
        return f"Previous Hash = {self.previous_hash.hexdigest()},\nData = {self.data}, \nNonce = {self.nonce}"

