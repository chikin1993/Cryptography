# First cipher I wrote! :)

# asking for message
plainText = input('Message to be encrypted: ')
while True:
    try:
        key = int(input('Key to use: '))
    # looping until key is an integer
    except ValueError:
        print('Not a real key m8')
        continue
    else:
        break
    
# do key mod 26 to give relative shift
key = key % 26

# symbol set for the encryption
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# empty string to fill with encrypted symbols
translated = ''

# converting to uppercase to fit in with LETTERS
plainText = plainText.upper()

for symbol in plainText:
    # encrypt the symbol if found in LETTERS and append to translated
    if symbol in LETTERS:
        numVal = LETTERS.find(symbol)
        numVal = (numVal + key) % 26
        translated = translated + LETTERS[numVal]
    # otherwise just append the symbol without alteration
    else:
        translated = translated + symbol

# print the encrypted string obtained     
print(translated)
