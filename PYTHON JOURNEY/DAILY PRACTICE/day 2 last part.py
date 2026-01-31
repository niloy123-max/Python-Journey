enter = input('Enter password: ')
Real = 'Niloy@2477'
if enter == Real: 
    print('Log in successful. Welcome to your account')
else: 
    print('Wrong Password. Try Again!!!')
print('Let\'s try another one.')
Submit = input('Enter your last academic examination name: ')
Submit_2 = float(input(f'Enter your {Submit} result\'s GPA point: '))
if Submit_2 < float(4.5): 
    print('Sorry. You are not eligible to apply in Taltech University')
else: 
    print('Congratulations. You are all set to apply in Taltech University')
Remaining_line = int(500 - (81+15))
print(f'Remaining_lines = {Remaining_line}')