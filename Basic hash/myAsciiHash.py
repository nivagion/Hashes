def hashit(toHash, size):
    suma = 0
    for char in toHash:
        suma += ord(char) * 13 #ASCII value of each char * 13
    suma %= int(size)
    print(f'string {toHash} with my ascii hash is {suma}')