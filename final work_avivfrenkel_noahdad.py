def Actions_menu():
    """
    שאלה 1:
    This function selects the appropriate service from the menu based on the user's input.
    """
    menu=int(input("Please tap the requested menu from 1-8"))
    match menu:
        case 1:
            print("Create account")
        case 2:
            print("Deposit money")
        case 3:
            print("Withdraw money")
        case 4:
            print("Check balance in account")
        case 5:
            print("Close account")
        case 6:
            print("Display all accounts holder list")
        case 7:
            print("Total balance in the bank")
        case 8:
            print("Quit")
        case other:
            print("Not found")

"""
        שאלה 2:
account_create: This function creates a bank account by inputting customer details.
"""
customers_database = {}  #The customer database is empty and each time a new customer is added

def calculate_age(birth_date):
    """
 This function takes a birth date in the 'DD/MM/YYYY' format and returns the current age of the person.
    """
    day, month, year = map(int, birth_date.split('/'))
    age = 2024 - year
    if month > 4 or (month == 4 and day > 6):
        age -= 1

    return age
def is_id_exists(customers_database, id_number):
    """
 This function checks if an ID already exists in the system.
    """
    for customer_details in customers_database.values():
        if customer_details['ID'] == id_number:
            return True
    return False


import random

def account_create(customers_database):
    """
     This function allows the user to create a new bank account.
    """
    created = False
    while not created:
        Email = input("Please register the email, and it must be noted that it is correct: ")
        if '@' not in Email or '.' not in Email or Email.count('@') != 1 or Email.startswith('@') or Email.endswith(
                '@') or Email.startswith('.') or Email.endswith('.'):
            print("Invalid email format. Please enter a valid email.")
            continue

        Name = input("Please enter the name: ")
        if not Name:
            print("Name cannot be empty. Please enter your name.")
            continue

        Last_Name = input("Please enter a last name: ")
        if not Last_Name:
            print("Last name cannot be empty. Please enter your last name.")
            continue

        ID = int(input("Please insert an ID card including a luxury card: "))

        if is_id_exists(customers_database, ID):
            print("ID already exists in the system. Please enter a different ID.")
            continue

        Date_of_birth = input("Please enter a date of birth (DD/MM/YYYY): ")

        try:
            day, month, year = map(int, Date_of_birth.split('/'))
        except ValueError:
            print("Invalid date format. Please enter the date in the format DD/MM/YYYY")
            continue


        if year > 2008 or (year == 2008 and month > 3):
            print("Sorry, you must be at least 16 years old to open a bank account.")
            continue

        account_number = random.randint(1000, 9999)


        customers_database[account_number] = {
            'Name': Name.capitalize(),
            'Last Name': Last_Name.capitalize(),
            'Date of Birth': Date_of_birth,
            'Email': Email,
            'ID': ID,
            'Balance': 0
        }

        created = True
        print("Bank account successfully created.")
        print("Customer details:")
        print(f"Name: {Name}")
        print(f"Last Name: {Last_Name}")
        print(f"Date of Birth: {Date_of_birth}")
        print(f"Email: {Email}")
        print(f"Account Number: {account_number}")

    return customers_database
"""
סעיף 3
 This function deposits money into the customer's bank account.
"""
def money_deposit(customers_database):
    account_number = int(input("Please write down the account number: "))
    deposit_amount = float(input("Please enter the deposit amount: "))

    if account_number in customers_database:
        customers_database[account_number]['Balance'] += deposit_amount
        print("Deposit successful!")
        print("Updated Balance:", customers_database[account_number]['Balance'])
    else:
        print("Account not found in the customers database.")
"""
סעיף 4
This function authenticates the customer's details.
"""
def user_authenticate(customers_database, account_number):
    if account_number in customers_database:
        return True
    else:
        return False

def money_withdraw(customers_database):
    account_number = int(input("Please enter your account number: "))
    withdrawal_amount = float(input("Please enter the withdrawal amount: "))

    if user_authenticate(customers_database, account_number):
        if -1000 <= customers_database[account_number]['Balance'] - withdrawal_amount:
            customers_database[account_number]['Balance'] -= withdrawal_amount
            print("Withdrawal successful!")
            print("Account Number:", account_number)
            print("ID:", customers_database[account_number]['ID'])
            print("Updated Balance:", customers_database[account_number]['Balance'])
        else:
            print("Withdrawal amount exceeds the limit. Cannot withdraw money from the account.")
    else:
        print("Failed to authenticate user. Unable to withdraw money from the account.")

"""
סעיף 5
This function withdraws money from the customer's bank account.
"""
def balance_check(customers_database):
    account_number = int(input("Please enter the account number: "))

    if account_number in customers_database:
        customer_details = customers_database[account_number]
        print("Account Number:", account_number)
        print("Name:", customer_details['Name'])
        print("Last Name:", customer_details['Last Name'])
        print("ID:", customer_details['ID'])
        print("Date of Birth:", customer_details['Date of Birth'])
        print("Email:", customer_details['Email'])
        print("Balance:", customer_details['Balance'])
    else:
        print("Account not found in the customers database.")

"""
סעיף 6
This function checks the balance of the customer's account.
"""
def account_close(customers_database):
    account_number = int(input("Please enter the account number you wish to close: "))

    if account_number in customers_database:
        if user_authenticate(customers_database, account_number):
            print("Your remaining balance is:", customers_database[account_number]['Balance'])
            print("Your account has been closed.")
            customers_database.pop(account_number)
        else:
            print("Cannot close bank account as user authentication failed.")
    else:
        print("Account not found in the customers database.")

"""
סעיף 7
This function closes a bank account.
"""
def accounts_all_display(customers_database):
    if not customers_database:
        print("No accounts found in the customers database.")
    else:
        print("Accounts Details:")
        for account_number, customer_details in customers_database.items():
            print(f"Account Number: {account_number}")
            print(f"Name: {customer_details['Name']}")
            print(f"Last Name: {customer_details['Last Name']}")
            print(f"Balance: {customer_details.get('Balance', 0)}")
"""
סעיף 8
This function displays a list of all accounts in the bank.
"""
def balance_bank_total(customers_database):
    total_balance = 0

    for customer_details in customers_database.values():
        if 'Balance' in customer_details:
            total_balance += customer_details['Balance']

    if total_balance == 0:
        print("No customers found in the bank.")
    else:
        print(f"Total balance in the bank: {total_balance}")
"""
סעיף 9
This function calculates the total balance of all accounts in the bank.
"""
def user_authenticate(customers_database, account_number):
    account_number_input = int(input("Please enter your account number: "))
    user_id = int(input("Please enter your ID: "))
    user_date_of_birth = input("Please enter your date of birth (DD/MM/YYYY): ")

    # Check if account number exists in the database
    if account_number_input in customers_database:
        # Check if user details match with the database
        if (customers_database[account_number_input]['ID'] == user_id) and \
                (customers_database[account_number_input]['Date of Birth'] == user_date_of_birth):
            return True
    return False

"""
חלק 10
The main function for managing bank accounts. It prompts the user for actions and executes the selected operation.
"""
def main():
    customers_database = {}

    while True:
        action = int(input("Please choose an action:\n"
                           "1. Open an account\n"
                           "2. Deposit money\n"
                           "3. Withdraw money\n"
                           "4. Check account balance\n"
                           "5. Close account\n"
                           "6. Display all accounts\n"
                           "7. Calculate bank balance\n"
                           "8. Quit\n"))

        if action == 1:
            account_create(customers_database)
        elif action == 2:
            money_deposit(customers_database)
        elif action == 3:
            money_withdraw(customers_database)
        elif action == 4:
            balance_check(customers_database)
        elif action == 5:
            account_close(customers_database)
        elif action == 6:
            accounts_all_display(customers_database)
        elif action == 7:
            balance_bank_total(customers_database)
        elif action == 8:
            print("Exiting the system")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()