print('Let\'s try a new loop')
real_username = 'Niloy'
real_password = 'Niloy'
tries = 0
while tries < 6: 
    E_1 = input('Enter your Username: ')
    E_2 = input('Enter your Passwrod: ')
    if real_username == E_1 and real_password == E_2: 
        print('Log in Successful')
        break
    else: 
        tries += 1 
        lasts = 6 - tries
        if tries > 0: 
            print(f'Wrong Password. Remaining Attempts {lasts}')
        else: 
            print(f'Your account is locked. Ramaining attempts {lasts}')