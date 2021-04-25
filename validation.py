# Account Validation


def account_number_validation(account_number):
    # Check if account_number is not empty
    # If account_number is 10 digits
    # If account_number is an integer
    if account_number:

        try:
            int(account_number)

            if len(str(account_number)) == 10:
                return True

        except ValueError:
            return False
        except TypeError:
            return False

    return False


def selected_operation_input_validation(input, selected_operation=None):
    if selected_operation == int(input):
        try:
            return True
        except ValueError:
            print("Incorrect Input")
            return False


def validate_registration_input(last_name, first_name):
    # Check if it's a list
    # Check each item in the list and be sure they are the current data type
    if last_name == str(input) and first_name == str(input):
        try:
            return True
        except ValueError:
            print("Name must contains alphabet not numbers")
            return False


def password_validation(password):
    if password:
        try:
            len(float(password)) >= 7
            return True
        except ValueError:
            print("Password must be greater than 7")
            return False
        except TypeError:
            return False
    else:
        print("Password is a require field")
        return False

# def account_generation_failure():
#     try:
#         account_number = generate_account_number()
#
#     except ValueError:
#         print('Account generation failed ')
#         init()
