# program to brute-force a caesar cipher

# asking for message
plainText = input('Message to be decrypted: ')

# symbol set for the encryption
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# empty string to fill with encrypted symbols
translated = ''

# converting to uppercase to fit in with LETTERS
plainText = plainText.upper()

#need to loop ciphering for each of 26 keys
for i in range(26):
    for symbol in plainText:
        # encrypt the symbol if found in LETTERS and append to translated
        if symbol in LETTERS:
            numVal = LETTERS.find(symbol)
            numVal = (numVal + i) % 26
            translated = translated + LETTERS[numVal]
        # otherwise just append the symbol without alteration
        else:
            translated = translated + symbol
    print('Using key ' + str(i) + ' ' + translated)
    translated = ''

# print the encrypted string obtained     
#print(translated)

