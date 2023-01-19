from csv import reader
from hashlib import sha256
hash_pas= {}
for pas in range(1,10000):
    hashing_numbers = sha256(b'%i'% pas).hexdigest()
    hash_pas[hashing_numbers] = pas
with open(r"name file") as f:
    pas_singer = reader(f)
    for row in pas_singer:
        for key in row[1:]:
            print(row,':',hash_pas[key])
