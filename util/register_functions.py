# Function to have user register
import time
import getpass


def get_name():
    print("Hello...")
    time.sleep(1)
    name = str(input("Enter name: "))
    return name


def get_username():
    username = str(input("Create username: "))
    return username


def get_password():
    while True:
        try:
            password = str(input("Enter a password: "))
            re_password = str(input("Re-enter password: "))
            if re_password != password:
                raise ValueError("\nUH OH! Passwords don't match.")
            else:  # passwords match
                break
        except ValueError as e:
            print(e)
            print("Try again\n")
    return password
