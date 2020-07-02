"""
A simple login program

Created by Ken Valverde

"""

from util import register_functions


class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    # Functions will go here

    def print_user(self):
        print("\nWelcome", self.name)
        print("Account details:")
        print("Username: {}\nPassword: {}".format(self.username, self.password))


if __name__ == '__main__':
    user = User(
        register_functions.get_name(),
        register_functions.get_username(),
        register_functions.get_password(),
    )

    user.print_user()