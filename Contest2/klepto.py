nk, nd = map(int, input().split())

keyword = input()
decrypt = input()

cipher = keyword[::-1]

fromend = 1
while len(cipher) < nd:
    cipher+=str(chr((ord(decrypt[len(decrypt)-fromend])-ord(cipher[fromend-1]))%26 + 97))
    fromend+=1

print(cipher[::-1])