import pandas as pd

df = pd.read_csv(r'C:\Users\Santos Kumar Soren\Downloads\Compressed\201408_trip_data\201408_trip_data.csv')

print(df['Trip ID'].size)

df1 = df['Zip Code'].unique()
print(df1.size)

df2 = df['Start Terminal'].value_counts().sort_values(ascending=False)
print(df2)
print('Top 10 from top:')
print(df2.head(10))
print('Top 10 from bottom')
print(df2.tail(10))