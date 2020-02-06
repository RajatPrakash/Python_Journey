import pandas as pd

data = pd.read_csv('pokemon_data.csv')
print('Normal Data')
print(data)

# getting only the chunk of data at a Time
count = 1
for chunk_data in pd.read_csv('pokemon_data.csv', chunksize=5):
  print('Chunk data row', count)
  print(chunk_data)
  count = count+1

