import pandas as pd
from itertools import product

data = {
'date': ['2024-01-10', '2024-01-15', '2024-01-20', '2024-02-05', '2024-02-10',
'2024-02-15', '2024-02-20', '2024-03-01', '2024-03-10', '2024-03-15'],
'artist': ['Arijit Singh', 'Arijit Singh', 'Shreya Ghoshal', 'Arijit Singh', 'Shreya Ghoshal','Shreya Ghoshal', 'Arijit Singh', 'Armaan Malik', 'Shreya Ghoshal', 'Arijit Singh'],
'venue': ['Mumbai', 'Mumbai', 'Delhi', 'Delhi', 'Mumbai','Mumbai', 'Mumbai', 'Bangalore', 'Bangalore','Bangalore']
}
df=pd.DataFrame(data)
df['date']=pd.to_datetime(df['date']) 
df['year_month']=df['date'].dt.to_period('M')
counts=df.groupby(['year_month','artist','venue']).size().reset_index(name='count')
result=counts.pivot_table(index='year_month',columns=['artist','venue'],values='count').fillna(0)
result.columns=['_'.join(col).strip() for col in result.columns.values]

print(result)