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

print(df, '\n')
print(df['Age'], '\n')

ages = pd.Series([22, 35, 58], name='Age')
print(ages)
print(df['Age'].min())
print(ages.sum() / ages.count())
print(ages.std)
print(df.describe())
