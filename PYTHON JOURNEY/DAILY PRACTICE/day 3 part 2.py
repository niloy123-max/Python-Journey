print('Okay. now we will try some loop functions')
print('1st I will try it in a password system. Let\'s try!!')
real_user = 'Niloy'
real_pass = 'niloy'
while True: 
    username = input('Enter your Username: ')
    password = input('Enter your Password: ')
    if real_user == username and real_pass == password: 
        print('Log in Successful')
        break
    else: 
        print('Wrong Username or Passwor. Try Again later')
print('Mission Complete)')