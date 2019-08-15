# transposition cipher

# asking user for message and key
plaintext = input('input plaintext: ')

#while key >= 0.5 * len(plaintext):
key = int(input('key to use: '))

# cipher only secure with a key < 0.5 * len(plaintext)
# comeback to this and add an if statement and ask again for key

# start of cipher as list of empty strings for the columns
ciphertext = [''] * key

# loop over each of the keys columns
for col in range(key):

    # setting the current pointer to start with first column
    pointer = col

    # add chars to cipher text column until end of message
    while pointer < len(plaintext):

        # add the character at pointer to the column and increase by key
        ciphertext[col] += plaintext[pointer]
        pointer += key

# join the columns together to form final ciphertext
ciphertext = ''.join(ciphertext)

# print resulting ciphertext
print(ciphertext)
