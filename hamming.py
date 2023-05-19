def encode_message(message):
    m = len(message)
    r = 1
    while 2 ** r < m + r + 1:
        r += 1
    encoded_message = [0] * (m + r)
    j = 0
    for i in range(1, m + r + 1):
        if i & (i - 1) != 0:
            encoded_message[i - 1] = int(message[j])
            j += 1
    for i in range(r):
        pos = 2 ** i
        parity = 0
        for j in range(1, m + r + 1):
            if j & pos == pos:
                parity ^= encoded_message[j - 1]
        encoded_message[pos - 1] = parity
    return encoded_message


def decode_message(encoded_message):
    r = 1
    while 2 ** r < len(encoded_message) + 1:
        r += 1
    error_position = 0
    for i in range(r):
        pos = 2 ** i
        parity = 0
        for j in range(1, len(encoded_message) + 1):
            if j & pos == pos:
                parity ^= encoded_message[j - 1]
        if parity != 0:
            error_position += pos
    if error_position != 0:
        encoded_message[error_position - 1] = 1 - encoded_message[error_position - 1]
    decoded_message = ""
    for i in range(1, len(encoded_message) + 1):
        if i & (i - 1) != 0:
            decoded_message += str(encoded_message[i - 1])
    return decoded_message

message=input("enter the message in 0's and 1's: ")
encoded_message = encode_message(message)
print("Encoded message:", encoded_message)

encoded_message[2] = 1 - encoded_message[2]
print("Modified encoded message:", encoded_message)

decoded_message = decode_message(encoded_message)
print("Decoded message:", decoded_message)
