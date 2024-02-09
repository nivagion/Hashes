import hashlib

def hashit(toHash, size):
    sha256_hash = hashlib.sha256() #sha 256 object
    sha256_hash.update(str(toHash).encode()) #encoded
    hashedHex = sha256_hash.hexdigest() #in hex
    hashedDeca = int(hashedHex, 16) #back to decimal
    hashedDeca = hashedDeca % int(size)
    print(f'string {toHash} with sha256 is {hashedDeca}')