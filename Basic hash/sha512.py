import hashlib

def hashit(toHash, size):
    sha512_hash = hashlib.sha512()              #sha 512 object
    sha512_hash.update(str(toHash).encode())    #encoded
    hashedHex = sha512_hash.hexdigest()         #in hex
    hashedDeca = int(hashedHex, 16)             #back to decimal
    hashedDeca = hashedDeca % int(size)
    print(f'string {toHash} with sha512 is {hashedDeca}')