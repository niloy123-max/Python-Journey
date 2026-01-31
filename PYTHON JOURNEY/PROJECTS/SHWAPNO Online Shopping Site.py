print('Let\'s make an online shopping site named "SHWAPNO"')
print('Welcome to SHWAPNO SUPPER SHOP')
do = input('Please log in to your account or register. Enter (log in) or (register): ')
if do == 'log in': 
    passwords = 'niloy'
    username = 'Niloy'
    attempts = 0
    while attempts < 3:
        user = input('Enter your username: ')
        password = input('Enter your password: ')
        if user == username and password == passwords: 
            print('Congratulations. Log in successful')
            log_in = True
            break
        else: 
            attempts += 1
            remaining = 3 - attempts 
            if remaining > 0: 
                print(f'Sorry! Wrong username or password. Remaining attempts: {remaining}')
            else: 
                print('Your account is locked. Try again later')
else: 
    print('Account Creation')
    mail = input('Enter your E-mail Adress: ')
    password = input('Create a new password: ')
    print('Account creation successful')
    log_in_mail = input('Enter your username: ')
    passwords = input('Enter your password: ')
    attempts = 0
    while attempts < 3:
        if mail == log_in_mail and password == passwords: 
            print('Congratulations. Log in successful')
            log_in = True
            break
        else: 
            attempts += 1
            remaining = 3 - attempts 
            if remaining > 0: 
                print(f'Sorry! Wrong username or password. Remaining attempts: {remaining}')
            else: 
                print('Your account is locked. Try again later')
if log_in == True:
    products = ['Miniket', 'Basmati', 'Masoor', 'Moong', 'Soybean Oil', 'CornFlour', 'Atta/Maida', 'Salt', 'Sugar', 'Eggs', 'Milk Liquid', 'Milk Powder', 'Butter', 'Cheese', 'Bread', 'Jam/Jelly', 'Oats', 'Cornflakes', 'Tea', 'Coffee', 'Biscuits', 'Chips', 'Juice', 'Soft Drinks', 'Soap', 'Shampoo', 'Toothpaste', 'Brush', 'Handwash', 'Sanitizer', 'Detergent', 'Dishwash','Lotion', 'Cream', 'Apple', 'Banana', 'Orange', 'Potato', 'Onion', 'Ginger', 'Chicken', 'Fish', 'Beef']
    print(f'Dear Customer! We have {len(products)} products available in our shop. You can order anything from the following list:')
    print(f'Products: {products}')
    product_price = {'Miniket' : 60, 'Basmati' : 120, 'Masoor' : 160, 'Moong' : 80, 'Soybean Oil 5 liter' : 800, 'CornFlour' : 60, 'Atta/Maida' : 60, 'Salt' : 40, 'Sugar' : 100, 'Eggs' : 40, 'Milk Liquid' : 60, 'Milk Powder' : 500, 'Butter' : 500, 'Cheese' : 200, 'Bread' : 60, 'Jam/Jelly' : 120, 'Oats' : 380, 'Cornflakes' : 80, 'Tea' : 20, 'Coffee' : 30, 'Biscuits' : 30, 'Chips' : 10, 'Juice' : 120, 'Soft Drinks' : 100, 'Soap' : 80, 'Shampoo' : 200, 'Toothpaste' : 250, 'Brush' : 60, 'Handwash' : 40, 'Sanitizer' : 50, 'Detergent' : 180, 'Dishwash' : 100,'Lotion' : 350, 'Cream' : 250, 'Apple' : 300, 'Banana' : 40, 'Orange' : 350, 'Potato' : 30, 'Onion' : 60, 'Ginger' : 260, 'Chicken' : 180, 'Fish' : 250, 'Beef' : 800}
    total_bill = 0
    Order_items = []
    while True: 
        choose = input('Enter your choosen products name(or type done): ').title()
        if choose == 'Done':
            break
        elif choose in product_price: 
            price = product_price[choose]
            total_bill += price 
            print(f'Dear customer, the price of {choose} = {price} BDT per unit and total bill = {total_bill} BDT')
        else: 
            print('Product not found')
if total_bill > 0: 
    print(f'Dear Customer! Your total bill is: {total_bill}')
    print('Enter your Name, Phone number and address to confirm your order')
    input('Name, Phone Number, Address\n')
    print('Order Successfull. You will get your products as soon as possible. Thank you. Have a great day!!')