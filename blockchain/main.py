import hashlib
from block import Block
from chain import Chain

chain = Chain(20)

for i in range(5):
    chain.add_to_pool(str(i))
    chain.mine()

"""h = hashlib.sha256()
h.update('b'.encode('utf-8'))
hash = h.hexdigest()
int = int(h.hexdigest(), 16)
print(int < 2**(256))

i = 0
h = hashlib.sha256()
h.update(str(i).encode('utf-8'))
condition = int(h.hexdigest(), 16) > 2**(256-10)
print(condition)

while condition:
    i += 1
    h.update(str(i).encode('utf-8'))
print(int(h.hexdigest(), 16) < 2**(256-10))
print(h.hexdigest())
"""