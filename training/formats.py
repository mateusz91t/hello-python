import pandas as pd
import time


source = 'files_sources/dane.csv'

start = time.time()
df = pd.read_csv(source)
print(f'load csv time:\t\t{time.time() - start}')

start = time.time()
df.to_csv('files_sources/dane.csv')
print(f'save csv time:\t\t{time.time() - start}')

start = time.time()
df.to_feather('files_sources/dane.feather')
print(f'save feather time:\t{time.time() - start}')

start = time.time()
df = pd.read_feather('files_sources/dane.feather')
print(f'load feather time:\t{time.time() - start}')

start = time.time()
df.to_parquet('files_sources/dane.parquet')
print(f'save parquet time:\t{time.time() - start}')

start = time.time()
df = pd.read_parquet('files_sources/dane.parquet')
print(f'load parquet time:\t{time.time() - start}')
