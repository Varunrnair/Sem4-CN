def bit_stuffing(data):
    stuffed_data = ""
    count = 0
    for i in data:
        if i == '1':
            count += 1
            if count == 5:
                stuffed_data += i + '0'
                count = 0
            else:
                stuffed_data += i
        else:
            count = 0
            stuffed_data += i
    return stuffed_data

def bit_destuffing(stuffed_data):
    destuffed_data = ""
    count = 0
    for i in stuffed_data:
        if i == '1':
            if count == 5:
                count = 0
            else:
                destuffed_data += i
            count += 1
        else:
            if count == 5:
                count = 0
            else:
                destuffed_data += i
            count += 1
    return destuffed_data

data = (input("Enter the string : "))
stuffed_data = bit_stuffing(data)
print(stuffed_data)

destuffed_data = bit_destuffing(stuffed_data)
print("Destuffed data:", destuffed_data)