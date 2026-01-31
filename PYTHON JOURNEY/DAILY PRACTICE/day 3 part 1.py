print('Welcome to the Taltech University admission page')
print('Please log in to your account or register')
Enter = input('Enter your Username: ')
Enter_2 = input('Enter your Password: ')
Real_user = 'Niloys'
Real_pass = 'niloy'
if Enter ==Real_user and Enter_2 == Real_pass:
    print('Log in successfull. Welcome to your account')
    print('ADMISSION FORM')
    Exam = input('Enter your last academic institute name: ')
    GPA = float(input(f'enter your {Exam} result\'s GPA point: '))
    if GPA > 4.9: 
        math = float(input('Enter your Mathematics GPA Grade: '))
        phy = float(input('Enter your Physics GPA Grade: '))
        if math > 4.9 or phy > 4.9: 
            print('Congratulations!! You are eligible for a scholarship in Taltech University')
        if math and phy >= 4.5: 
            print('Exellent!! You are a top candidate for Taltech University')
        elif math and phy >= 4.0: 
            print('Good Job. You are eligible to apply in Taltech University')
        else: print('Sorry!! Your GPA grade doesn\'t fulfill our requirements. Better luck next time!!')
    elif GPA >= 4.5: 
        M_2 = float(input('Enter your Mathematics GPA Grade: '))
        P_2 = float(input('Enter your Physics GPA Grade: '))
        if M_2 and P_2 >= 4.0 :
            print('Good Job. You are eligible to apply in Taltech University')
        else: 
            print('Sorry!! Your GPA grade doesn\'t fulfill our requirements. Better luck next time!!')
    elif GPA >= 4: 
        print('Thanks for your interest in Taltech Unversity. Your are in out waiting list.')
    else: 
        print('Sorry!! Your GPA grade doesn\'t fulfill our requirements. Better luck next time!!')
else: 
    print('Wrong Username or Password')