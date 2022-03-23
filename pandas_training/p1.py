import pandas as pd


df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth"
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"]
    }
)

print(type(df))
print(df, '\n')
print(type(df['Age']))
print(df['Age'], '\n')

ages = pd.Series([22, 35, 58], name='Age')
print(type(ages))
print(ages)
print(df['Age'].min())
print(ages.sum() / ages.count())

print()
print(ages.std())
print(df.describe())
