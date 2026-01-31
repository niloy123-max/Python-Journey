print('Let\'s Build A Professional Admission Portal')
print('Tallin University of Science and Technology')
real_user = 'Niloy'
real_pass = 'niloy'
Attempts = 0
while Attempts < 5: 
    username = input('Enter your account username: ')
    password = input('Enter your account password: ')
    if real_user == username and real_pass == password: 
        print('Congratulations. Log in Successful. Welcome to Taltech University Admission Portal')
        Name = input('Enter your full name: ')
        Address = input('Enter your address: ')
        father = input ('Enter your father\'s name: ')
        mother = input('Enter your mother\'s name: ')
        college = input ('Enter your last institution\'s name: ')
        Exam = input(f'Enter your {college}\'s exam name: ')
        Gpa = float(input(f'Enter your {Exam} GPA grade: '))
        math = float(input('Enter your mathmatics GPA grade: '))
        physics = float(input('Enter your physics GPA grade: '))
        Chemistry = float(input('Enter your chemistry GPA grade: '))
        if Gpa == math == physics == Chemistry == 5.00: 
            print('Congratulations. You are eligible to get a full funded scholarship in Taltech University')
            eligibility = True
        elif Gpa == math and max(physics, Chemistry) == 5.00: 
            print('Congratulations. You are eligible to get a partial scholarship in Taltech University')
            eligibility = True
        elif Gpa == 5.00 and min(math, physics, Chemistry) >= 4.5: 
            print('Exellent!! You are a top candidate in Taltech University')
            eligibility = True
        elif Gpa >= 4.5 and min(math, physics, Chemistry) >= 4.00:
            print('Good job. You are eligible to apply in Taltech University')
            eligibility = True
        elif Gpa >=4.00 and min(math, physics, Chemistry) >=3.00: 
            print('Thanks for your interest in Taltech Unversity. You are in our waiting list')
        else: 
            print('Sorry! You are not eligible to apply in Taltech University. Better luck next time.')
        subject = ['Computer Science', 'Machanical Engineering', 'Civil Engineering', 'Cyber Security']
        if eligibility == True: 
            print(f'We have {len(subject)} departments in our university')
            print(f'Subject Lists: {subject}')
            while True: 
                choice = input('Enter your preferred subject: ')
                if choice in subject: 
                    print('Congratulations. Your application is done. We will inform your application result through E-mail as soon as possible') 
                    break
                else: 
                    print('Sorry! Your perferred subject is not available in our university!')
                exit
    else: 
        Attempts += 1
        if Attempts < 5: 
            print(f'Wrong Username or Password. Remaining attempts:{5 - Attempts}')
        else: 
            print(' Your account is locked!!')
with open('Application File.txt', 'a') as file: 
    file.write(f'Name: {Name}, GPA: {Gpa}, Subject: {choice}\n')
    print('Data successfully saved')