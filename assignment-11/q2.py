import pandas as pd

s=pd.Series(['X','Y','T','Aaba','Baca','CABA',None,'bird','horse','dog'])
s_lower=s.str.lower()
s_upper=s.str.upper()
l=s.str.len()
print(s_lower)
print(s_upper)