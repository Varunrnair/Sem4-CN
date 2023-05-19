def byte_stuffing(data, flag):
    stuffed_data = b""
    escape_character = b'$'
    for i in data:
        if i == flag[0]:
            stuffed_data += escape_character + bytes([i])
        elif i == escape_character[0]:
            stuffed_data += escape_character + escape_character
        else:
            stuffed_data += bytes([i])
    return stuffed_data


def byte_destuffing(stuffed_data, flag):
    destuffed_data = b""
    escape_character = b'$'
    i = 0
    while i < len(stuffed_data):
        if stuffed_data[i:i+1] == escape_character:
            i += 1
        destuffed_data += stuffed_data[i:i+1]
        i += 1
    return destuffed_data

data = input("Enter the string: ").encode()
flag = input("Enter the flag element: ").encode()

stuffed_data = byte_stuffing(data, flag)
print("Stuffed data:", stuffed_data)

destuffed_data = byte_destuffing(stuffed_data, flag)
print("Destuffed data:", destuffed_data)




