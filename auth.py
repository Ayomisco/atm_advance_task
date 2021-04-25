# register
# - first name,lastname, Password, email
# - generating user account

# login
# - (account number) and Password

import datetime
# Dictionary
# INITIALISING THE SYSTEM
import random
import time

import validation
import database
from getpass import getpass
# Naira code Start
naira = u"\u20A6"
# Naira Code Stop

# database = {
#     3846403507: ['AYO', 'SAM', 'fayomide324@gmail.com', 'SAM']
# }


def init():
    print("Welcome to Ayomisco Bank")

    is_valid_option_selected: bool = False

    while not is_valid_option_selected:

        have_account = int(input("Do you have account with us: \n 1. yes \n 2. No \n" + "====" * 12 + "\n"))
        if have_account == 1:
            is_valid_option_selected = True
            login()
        elif have_account == 2:
            is_valid_option_selected = True
            print(register())
        else:
            print("You have selected invalid option")


def login():
    print("***************** Login to your account *******************")

    account_number_from_user = input("What is your account number? \n")

    is_account_number_valid = validation.account_number_validation(account_number_from_user)

    if is_account_number_valid:

        password = getpass("Enter your password: \n")

        user = database.authenticated_user(account_number_from_user, password)

        if user:
            bank_operation(user)

        # for account_number, user_details in database.items():
        #     if account_number == int(account_number_from_user):
        #         if user_details[3] == password:
        #             bank_operation(user_details)

        print('Invalid account or password')
        login()
    else:
        print('Invalid account number! Check that your entries are more than 10 and are number')
        init()


def register():
    print('************ Register **************')

    email = input("What is your email address? \n")
    sleep()

    first_name = input("What is your first name \n")
    sleep()

    last_name = input("What is your Last Name \n")
    sleep()

    password = getpass("Create a new password \n")

    # FIRST NAME AND lAST NAME VALIDATION
    validation.validate_registration_input(last_name, first_name)

    validation.password_validation(password)

    # Account generation failure IN VALIDATION
    # validation.account_generation_failure()

    # try:
    account_number = generate_account_number()

    # except ValueError:
    #     print('Account generation failed ')
    #     init()

    # database[account_number] = [first_name, last_name, email, password, 0]
    is_user_created = database.create(account_number, first_name, last_name, email, password)

    # using database module to create new user record

    if is_user_created:
        print("Your Account Has been Created")
        sleep()
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        sleep()

        login()
    else:
        print("Something went wrong try again")
        register()


def bank_operation(user):
    sleep()

    print("Welcome %s %s" % (user[0], user[1]))
    print("======================================")
    # Date and Time
    now = datetime.datetime.now()
    print(now.strftime("%y-%m-%d %H:%M:%S"))
    sleep()

    selected_operation = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))
    validation.selected_operation_input_validation()
    # Time Sleep
    sleep()

    if selected_operation == 1:
        sleep()
        deposit_operation(balance=0)

    elif selected_operation == 2:
        sleep()
        withdrawal_operations()

    elif selected_operation == 3:
        sleep()
        logout()
    elif selected_operation == 4:
        sleep()
        exit()
    else:
        print("Invalid option selected")
        bank_operation(user)
        init()


def withdrawal_operations(user_details):
    cash_withdraw = int(input("Enter amount to withdraw:"))
    if cash_withdraw >= get_current_balance(user_details(4)):
        print('Insuficient fund')
        try:
            int(cash_withdraw)
            return True
        except ValueError:
            return False




        
        print("Withdrawal")
        # Get current balance
        # Get amount to withdraw
        # Check if current balance is > withdraw balance
        # deduct withdrawn amount from current balance
        # display current balance
    
        # Customer Deposit Ends here #


def deposit_operation(balance):
    cash_deposit = int(input("How much would you like to deposit? \n"))
    time.sleep(2)
    print("======================================")
    print("======================================")
    total = balance + cash_deposit
    print("your account balance is: \n %s" % naira, total)
    # Customer Deposit Ends here #
    print("Deposit Operations")
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance


def set_current_balance(user_details, balance):
    user_details[4] = balance


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


def get_current_balance(user_details):
    total = user_details(4)
    return total


# Time Delay Function
def sleep():
    print("===== " * 7)
    print("===== " * 7)
    time.sleep(2)


def logout():
    login()


# ACTUAL BANKING SYSTEM #
init()
