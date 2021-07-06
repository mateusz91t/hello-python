import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1, 2, 3, np.nan, 6, 7, 8])
print(s)

#             od daty i/lub do daty, ile razy, częstotliwość
dates = pd.date_range('20210201', periods=6, freq='2D')
print(dates, '\n')

# jeśli nie ustawimy indeksu to auto będzie 01234...
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)
print(df.dtypes)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp('20210226'),
        "C": pd.Series(1, index=list(range(4)), dtype='float32'),
        "D": np.array([3] * 4, dtype='int32'),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo"
    }
)

print('\n# Vieving data')
# Vieving data
print(df2)
print(df2.dtypes)
print(df.head())  # pierwsze __x lub 5 w.
print(df.tail(2), '\n')  # ostatnie __x lub 5 w.

print(df.index)
print(df2.index, '\n')

print(df.to_numpy())  # do tablic 2d
print(df2.to_numpy(), '\n')

print(df.describe())  # średnie, mediany, odchylenie st. itp
print(df2.describe(), '\n')

print(df)
print(df.T)
print(df.sort_index(ascending=False))
print(df.sort_index(axis=1, ascending=False))  # sortowanie kolumn
print(df.sort_values(by='B'))  # sort wierszy po kolumnie

# Selection
print('\n' * 2, '# Selection')
print(df['A'])  # ta kolumna
print(df[0:3])  # 0-3 kolumny
print(df['20210203':'20210207'])  # od indeksu __x do indeksu y
# loc - grupa kol i wier
print(df.loc[dates[0]])  # pierwszy wiersz
print(df.loc[dates[:2]])  # wiersze [0, 2) jeśli indeks daty
print(df2.loc[0:2])
print(df.loc[:, 'B'])  # drugi arg loc'a to jakie kolumny
print(df.loc[:, ['A', 'B']])
print(df.loc[:, 'B':'D'])  # slice z kolumn
# at - 1 wartosc z kol/w
print(df.at[dates[0], 'B'])
# iloc - grupa kol i wiersz, ale po indeksach
print(df.iloc[3])  # 3-ci wiersz z każdej kol
print(df.iloc[3:5, 0:2])  # rows, cols
print(df.iloc[:, 0:2])  # , cols
# iat - 1 wartość z kol/w po indeksie
print(df.iat[0, 1])

# Boolean indexing
print('\n' * 2, '# Boolean indexing')
print(df[df['A'] > 0])
print(df[df > 0])

df3 = df.copy()
df3['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df3)
print(
    df3[
        df3['E'].isin(
            ['two', 'four']
        )
    ]
)

# Setting
print('\n' * 2, '# Setting')
s1 = pd.Series(
    list(range(1, 7)), index=pd.date_range('20210201', periods=6, freq='2D')
)
print(s1)
# dodaję kolumnę po indeksie tej samej daty
df['F'] = s1
print(df)
print(df.iat[0, 0])
df.iat[0, 0] = 1
print(df.at[dates[0], 'A'])
print(df)
print(len(df))
df.loc[:, 'D'] = np.array([5] * len(df))
print(df)
# where
df4 = df.copy()
print(df4)
df4[df4 > 2] = -df4
print(df4)
print(df4[df4['A'] > 1] * 10)

# Missing data
print('\n' * 2, '# Missing data')
df5 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df5.at['2021-02-03', 'F'] = np.NaN
df5.loc[dates[0]: dates[1], 'E'] = 1
print(df5)
print(df5.dropna(how='any'))
print(df5.fillna(value=5))
print(df5.isna())
print(df5.isnull())

# Operations
# Stats
print('\n' * 2, '# Stats')
print(df)
print(df.mean())
print(df.mean(1))
s2 = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates)
print(s2)
s2 = s2.shift(2)
print(s2)
print(df)
print(df.sub(s2, axis='index'))  # odejmowanie serii 1,3,5

# Aplly
print('\n' * 2, '# Apply')
print(df)
print(df.apply(np.cumsum))  # sumaryczne podsumowanie wierszy
print(df.apply(lambda x: x.max() - x.min()))

# Histogramming
s3 = pd.Series(np.random.randint(0, 7, size=10))
print(s3)
print(s3.value_counts())  # ile jakich wartości

# String Methods
s4 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.NaN, 'CABA', 'dog', 'cat'])
print(s4)
print(s4.str.lower())

# Merge
# Concat
df6 = pd.DataFrame(np.random.randn(10, 4))
print(df6)

pieces = [df6[:3]]
print()
print(pieces)
pieces.append(df6[3:7])
print()
print(pieces)
pieces.append(df6[7:])
print(pieces)
print()
print(pd.concat(pieces))

# Join
# cross
print('\n' * 2, 'cross')
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [3, 4]})
print(left)
print(right)
print(pd.merge(left, right, on='key'))

# inner
print('\n' * 2, 'inner')
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [3, 4]})
print(left)
print(right)
print(pd.merge(left, right, on='key'))

# Grouping
df7 = pd.DataFrame(
    {
        'A': ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        'B': ["one", "one", "two", "three", "two", "two", "one", "three"],
        'C': np.random.randn(8),
        'D': np.random.randn(8)
    }
)

print(df7)
print(df7.groupby('A').sum())
print()
print(df7.groupby(['A', 'B']).sum())
print(df7.groupby(['A', 'B']).groups)


# Reshaping
# Stack
print('\n' * 2, 'stack')
tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)
print(tuples)
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
print(index)
df8 = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
print(df8)

df9 = df8[:4]
print(df9)
stacked = df9.stack()
print(stacked)
print(stacked.unstack())
print(stacked.unstack(1))
print(stacked.unstack(0))

# Pivot tables


# Time series
print('\n' * 2, 'Time series')
rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
print(rng)
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts)
print(ts.tz_localize("UTC"))
print(ts.tz_localize("UTC").tz_convert("US/Eastern"))


# Plotting
print('\n' * 2, 'Plotting')
plt.close("all")
ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
print(ts)
print('\n', 'cumsum')
ts = ts.cumsum()
print(ts)
ts.plot()
plt.show()
plt.close('all')

df9 = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D']
)
print(df9)
df9 = df9.cumsum()
print(df9)
plt.figure()  # tworzy dodatkowe okno wykresu
df9.plot()
plt.legend(loc='best')
plt.show()


# csv
s = pd.read_csv('../files_sources/dane.csv', sep=';')
print(s)
