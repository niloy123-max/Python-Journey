print('Let\'s check the strength of password')
print('**TalTech University Online Library Site**')
step_1 = input('Enter Log in or Register: ').strip().title()
Access = False
if step_1 == 'Register':
    Username = input('Enter your username: ')
    while True:
        Password = input('Enter a new password (Please use at lease 1 uppercase letter, 1 lowercase letter, 1 digit, 1 special character and total 8 characters): ')
        has_upper = any(c.isupper() for c in Password)
        has_lower = any(c.islower() for c in Password)
        has_digit = any(c.isdigit() for c in Password)
        special_chars = "!@#$%^&*\/()"
        has_special = any(c in special_chars for c in Password)
        if len(Password) >= 8 and has_upper and has_lower and has_digit and has_special:
            Access = True
            print("Registration Successful!")
            break
        else: 
            print('Error!! Try again with the command!!')
elif step_1 == 'Log In':
    Username = 'Niloy'
    Password = 'niloy'
    attempts = 0
    while attempts < 3:
        User = input('Enter your username: ')
        Pass = input('Enter your password: ')
        if Username == User and Password == Pass: 
            print('Log in successful.')
            Access = True
            break
        else: 
            attempts += 1
            remaining = 3 - attempts
            if remaining > 0: 
                print(f'Wrong password or username. try again. Remaining attempts = {remaining}')
            else: 
                print('Your account is locked!')
if Access == True: 
    print('Welcome to the Online Library portal of TalTech University')
    Submit = False
    while True:
        try: 
            List_of_books = ['To Kill a Mockingbird by Harper Lee 1984 by George Orwell', 'The Great Gatsby by F. Scott Fitzgerald', 'Pride and Prejudice by Jane Austen', 'Jane Eyre by Charlotte Brontë', 'Wuthering Heights by Emily Brontë', 'Great Expectations by Charles Dickens', 'Moby-Dick by Herman Melville', 'The Catcher in the Rye by J.D. Salinger', 'Frankenstein by Mary Shelley', 'The Lord of the Rings by J.R.R. Tolkien', 'Animal Farm by George Orwell', 'Brave New World by Aldous Huxley', 'Alice\'s Adventures in Wonderland by Lewis Carroll', 'The Picture of Dorian Gray by Oscar Wilde', 'Little Women by Louisa May Alcott', 'Middlemarch by George Eliot', 'Ulysses by James Joyce', 'The Grapes of Wrath by John Steinbeck', 'Catch-22 by Joseph Heller', 'Treasure Island by Robert Louis Stevenson', 'Gulliver\'s Travels by Jonathan Swift', 'David Copperfield by Charles Dickens', 'The Hobbit by J.R.R. Tolkien', 'Fahrenheit 451 by Ray Bradbury', 'Lord of the Flies by William Golding', 'A Tale of Two Cities by Charles Dickens', 'Sense and Sensibility by Jane Austen', 'Dracula by Bram Stoker', 'Robinson Crusoe by Daniel Defoe']
            print(f'Right now we have {len(List_of_books)} books in our library')
            print('List of books : To Kill a Mockingbird by Harper Lee 1984 by George Orwell, The Great Gatsby by F. Scott Fitzgerald, Pride and Prejudice by Jane Austen, Jane Eyre by Charlotte Brontë, Wuthering Heights by Emily Brontë, Great Expectations by Charles Dickens, Moby-Dick by Herman Melville, The Catcher in the Rye by J.D. Salinger, Frankenstein by Mary Shelley, The Lord of the Rings by J.R.R. Tolkien, Animal Farm by George Orwell, Brave New World by Aldous Huxley, Alice\'s Adventures in Wonderland by Lewis Carroll, The Picture of Dorian Gray by Oscar Wilde, Little Women by Louisa May Alcott, Middlemarch by George Eliot, Ulysses by James Joyce, The Grapes of Wrath by John Steinbeck, Catch-22 by Joseph Heller, Treasure Island by Robert Louis Stevenson, Gulliver\'s Travels by Jonathan Swift, David Copperfield by Charles Dickens, The Hobbit by J.R.R. Tolkien, Fahrenheit 451 by Ray Bradbury, Lord of the Flies by William Golding, A Tale of Two Cities by Charles Dickens, Sense and Sensibility by Jane Austen, Dracula by Bram Stoker, and Robinson Crusoe by Daniel Defoe.')
            Choose = str(input('Enter your preferred book\'s name(as per the list): '))
            Submit = True
            break
        except: 
            print('Wrong input')
    if Submit == True: 
        print('\n1 = Read books online, 2= Order books to borrow')
        while True:
            try: 
                purpose = int(input('Enter your purpose. Type 1 or 2: '))
                Next_step = True
                break
            except: 
                print('Wrong input. Try again')
        if purpose == 1: 
            id = False
            while True:
                try: 
                    print('Confirm your identity')
                    identity = input('Enter your Student ID number: ')
                    if len(identity) < 8:
                        id = True
                        if id == True: 
                            print(f'Welcome to the 1st page of {Choose} book')
                            Done = 'Done'
                            do = input(f'Enter {Done} to exit this page: ')
                            break
                except: 
                    print('Wrong input')
        elif purpose == 2: 
                    name = input('Enter your full name: ')
                    Session = input('Enter your session: ')
                    Id = input('Enter your Student ID number: ')
                    Address = input('Enter your address: ')
                    Return = input('Input the days after you\'ll return the books: ')
                    print('Your application is submitted! You\'ll get an update within next working days')
                    print('You have to come to the library office within 7 working days after getting confirmation! Thank you. Have a great day!')
else: 
    print('Try again')