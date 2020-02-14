import pandas as pd

a=[{"USUBJID":'CT1/' + str(i).zfill(3)} for i in range(101,116)]
dataset = pd.DataFrame(a)

# dataset as Pandas.DataFrame #

import hashlib

def sha_it(s):
    return hashlib.sha256(s.encode()).hexdigest().upper()
        
def hashid(var, key, hashlen):
    der = sum([ord(j) * (i+1) for i,j in enumerate(key)])
    strt = der % (64 - hashlen)
    return (sha_it(key + var))[strt:][:hashlen]
        
dataset['DSUBJID'] = dataset['USUBJID'].apply(hashid,args=('C0mpl3t3Ly+r@nd0m=kEY', 8))

print(dataset.to_markdown())

print(dataset.describe())