import pandas as pd
# importing data into data frame
df = pd.read_csv('C:\\Users\SHRI\Desktop\data1.csv')
df['total_statements'] =[13,13,12,13,2,2,3,9,7,8,16,2,6,3,2,11,6,5,4,2,7]
df['total_reasons'] = [21,16,11,12,2,7,3,9,7,8,19,4,8,3,2,8,7,5,5,2,7]
grouped_df = df.groupby(['Team Name']).mean([['total_statements', 'total_reasons']])
df1 = grouped_df.sort_values(by=['total_statements', ], ascending=[False])
df1 = df1.drop('S No', axis=1)
df1=df1.drop('User ID',axis=1)
df1.sort_values(by=["total_statements","total_reasons"],ascending=False,inplace=True) # sorted the value in decending order
print(df1)
df1.to_excel('D:/internship/input2_sorted.xlsx',index=True)