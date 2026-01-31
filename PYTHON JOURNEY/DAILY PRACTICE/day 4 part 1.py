print('Let\'s try one more time')
Real_user = 'Niloy'
Real_pass = 'niloy'
attempts = 0
log_in = False
while attempts < 5: 
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if username == Real_user and Real_pass == password: 
        print('Log in successfull. Welcome to the Application Page')
        log_in = True
        break
    else: 
        attempts += 1
        if attempts < 5: 
            print(f'Wrong password. Remaining tries {5 - attempts}')
        else: 
            print('Your account is locked')
            exit
if log_in == True: 
    print('Application page')
    input('Enter your Father\'s name: ')
    input('Enter your Mother\'s name: ')
    GPA = float(input('Enter your HSC GPA grade: '))
    if GPA == 5.00: 
        print('Congratulations. You are a top candidate for Taltech University')
    elif GPA >= 4.5 and GPA < 5.00: 
        print('Congratulations. You are eligible to apply in Taltech Unversity.')
    elif GPA >= 4 and GPA < 4.5: 
        print('Thanks for your interest in Taltech University. You are in our waiting list')
    else: 
        print('Sorry!! You are not eligible to apply in Taltech University. Better luck next time!!')