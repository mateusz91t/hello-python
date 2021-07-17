import multiprocessing
from functools import partial
import pandas as pd

preprocess = 

BUCKET_SIZE = 50000

def run_process(df, start):
    df = df[start:start+BUCKET_SIZE]
    print(start, "to ",start+BUCKET_SIZE)
    temp = df["question"].apply(preprocess)

chunks  = [x for x in range(0,df.shape[0], BUCKET_SIZE)]
pool = multiprocessing.Pool()
func = partial(run_process, df)
temp = pool.map(func,chunks)
pool.close()
pool.join()
