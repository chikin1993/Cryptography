# ask for mode and proceed only with valid answers
mode1 = 'encrypt'
mode2 = 'decrypt'

mode = input('choice of mode? ')
while mode != mode1 and mode2:
    print('you are still in the loop')
    mode = input('choice of mode? ')
    

    
