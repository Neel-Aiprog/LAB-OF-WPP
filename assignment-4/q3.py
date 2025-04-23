s=input()
text=list(s.lower())
alpha=[]
for i in range(97,123):
    alpha.append(chr(i))
for i in text:
    if(i==" "):
        text.remove(i)
text.sort()
alpha.sort()
a=len(set(text))
b=len(set(alpha))
if(a==b):
    print("pangram")
else:
    print("not pangram")