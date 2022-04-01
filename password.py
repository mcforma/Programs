# password.py
# To check whether a given password is valid or not

'''
the password uses the following criteria:

The password should be at least 16 characters strong.
The password should contain at least one upper case letter.
The password should contain at least one lower case letter.
The password should have at least one digit.
The password should have not have any special character such as $, % or #. 
The password should not contain spaces. 
The algorithm should ask for a password and then verifies that it meets the stated criteria. If it does it should display message “Password Accepted”.

If it doesn't the program should display a message telling the user why?
'''


def main():
    pswd = input("Please enter a password that has at least 16 characters, one uppercase, one lowercase, one digit, no special characters, and no spaces: ")
    valid, message = check_password(pswd)

    if valid == True:
        print(message)
    else:
        error = "\nPassword not accepted because of the following condition(s):\n"
        error += message
        print(error)


def check_password(pwd):
    l_case_count = 0
    u_case_count = 0
    digit_count = 0
    spl_char_count = 0
    space_count = 0
    size = len(pwd)

    for char in pwd:
        if char.islower():
            l_case_count += 1
        elif char.isupper():
            u_case_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        else:                   # only availble character type left is special character, so that will be the else
            spl_char_count += 1


    if size >= 16 and l_case_count > 0 and u_case_count > 0 and digit_count > 0 and space_count == 0 and spl_char_count == 0:
        msg = "Password meets all conditions and Password accepted\n"
        return True, msg
    else:
        msg = ""
        if size < 16:
            msg += "Password string must have at least 16 characters.\n"
        if l_case_count == 0:
            msg += "Password string must have at least one lowercase character.\n"
        if u_case_count == 0:
            msg += "Password string must have at least one uppercase character.\n"
        if digit_count == 0:
            msg += "Password string must have at least one digit as character.\n"
        if space_count > 0:
            msg += "Password string cannot contain any spaces.\n"
        if spl_char_count > 0:
            msg += "Password string cannot contain any special characters.\n"

        return False, msg

main()