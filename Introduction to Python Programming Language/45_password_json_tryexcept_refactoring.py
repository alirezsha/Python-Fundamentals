import json

def saved_password():
    """This function displays the saved password."""
    file_path = 'F:/Offline Courses/03 - Python/password.json'
    try:
        with open(file_path) as f:
            password = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return password

def new_password():
    """This function gets the password from the new user."""
    password = input('Enter the password: ')
    file_path = 'F:/Offline Courses/03 - Python/password.json'
    with open(file_path, 'w') as f:
        json.dump(password, f)
    return password

def password_identification():
    """This function identifies entered passwords."""
    password = saved_password()
    if password:
        print(f'Your password is: {password}')
    else:
        password = new_password()
        print(f'Password set by you: {password}')

password_identification()
