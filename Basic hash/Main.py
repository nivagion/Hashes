import myAsciiHash as myAH
import sha256 as s256
import sha512 as s512


toHash = input('Enter a string to hash: ')
hashSize = input('Enter a number of elements in hash: ')
whatMethod = input('input single char;  l-my ascii hash,  s-SHA 256,  p-SHA 512: ')

if whatMethod == 'l':
    myAH.hashit(toHash, hashSize)
elif whatMethod == 's':
    s256.hashit(toHash, hashSize)
elif whatMethod == 'p':
    s512.hashit(toHash, hashSize)
