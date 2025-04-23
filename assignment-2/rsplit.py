string = "abcdabcd"
choice = input("Enter choice string: ")
max_split = int(input("Enter max split value: "))
string_2 = string[::-1]  
string_3 = string_2.split(sep=choice[::-1], maxsplit=max_split)
result = [string_4[::-1] for string_4 in string_3][::-1]
print(result)
