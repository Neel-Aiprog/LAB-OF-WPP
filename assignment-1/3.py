length=int(input("pls enter your length in feet\t"))
ch=int(input("enter your appropriate choice\t"))
ans=[]
inch=5*length
yard=length/3
milm=length*304.8
cenm=length*30.48
mile=length*0.000189394
kilom=length*0.0003048
metre=length*0.3048
ans.append(inch)
ans.append(yard)
ans.append(cenm)
ans.append(milm)
ans.append(kilom)
ans.append(metre)
print(ans[ch-1])
