import pandas as pd

chunksize = 10 ** 6
for chunk in pd.read_csv('fake.csv', chunksize= chunksize):
    print(chunk)
for chunk in pd.read_csv('true.csv', chunksize= chunksize):
    print(chunk)
