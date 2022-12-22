# Ceaser's Cypher
print("Do you want to 'encode' or 'decode'")
encoder = int(input("press '1' for encoding '2' for decoding: "))
message = input("Enter the message: ").upper()
shift = int(input("Enter the shift: "))
Alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
             "S", "T", "U", "V", "W", "X", "Y", "Z"]
charachters = [" ", ",", ".", "<", ">", "?", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=",
               "{", "}", "[", "]", ":", ";", "|", "/"]
indexes = []
shifted_indexes = []
encoded_message = ""
print(message)
for letter in message:
    if letter not in charachters:
        index = Alphabets.index(letter)
        indexes.append(index)
    elif letter in charachters:
        indexes.append(letter)
print(indexes)
if encoder == 1:
    # Encryption
    for j in range(0, len(indexes)):
        if indexes[j] in charachters:
            shifted_indexes.append(indexes[j])
        elif (indexes[j] + shift) > 25 and (indexes[j] not in charachters):
            y = (shift - (25 - indexes[j])) - 1
            shifted_indexes.append(y)
        elif (indexes[j] + shift) <= 25 and (indexes[j] not in charachters):
            shifted_indexes.append(indexes[j] + shift)
    #print(shifted_indexes)
if encoder == 2:
    # Decryption
    for j in range(0, len(indexes)):
        if indexes[j] in charachters:
            shifted_indexes.append(indexes[j])
        else:
            y = indexes[j] - shift
            shifted_indexes.append(y)
    #print(shifted_indexes)

for k in range(0, len(shifted_indexes)):
    if shifted_indexes[k] in charachters:
        encoded_message += shifted_indexes[k]
    elif shifted_indexes[k] not in charachters:
        encoded_message += Alphabets[shifted_indexes[k]]
print(encoded_message)
