import pandas as pd
# importing data into data frame
df = pd.read_csv('C:\\Users\SHRI\Desktop\data2.csv')
df=df.sort_values(by=['total_statements', 'total_reasons'], ascending=[False, False])
df= df.drop('S No', axis=1)
df.index=range(1,22)
df.index.name="Rank"
print(df)
# Display the sorted DataFrame

df.to_excel('D:/internship/input1_sorted.xlsx', index= False ) 