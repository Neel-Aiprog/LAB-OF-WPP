def decode_ways(s, index=0, path="", result=None):
    if result is None:
        result = []
    if index == len(s):
        result.append(path)
        return
    
    num1 = int(s[index])
    if 1 <= num1 <= 9:
        decode_ways(s, index + 1, path + chr(num1 + 64), result)
    
    if index + 1 < len(s):
        num2 = int(s[index:index+2])
        if 10 <= num2 <= 26:
            decode_ways(s, index + 2, path + chr(num2 + 64), result)
    
    return result

encoded_message = "11106"
decoded_messages = decode_ways(encoded_message)
print("Possible Decoded Messages:")
for message in decoded_messages:
    print(message)
