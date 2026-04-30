#!/usr/bin/python3
"""User class
"""


class User():
    """User class
    """

    def __init__(self):
        self.__password = None

    @property
    def password(self):
        """Password getter
        """
        return self.__password

    @password.setter
    def password(self, pwd):
        """Password setter
        """
        self.__password = pwd

    def is_valid_password(self, pwd):
        """Valid password
        """
        return self.__password == pwd


if __name__ == "__main__":
    print("Test User")

    user_1 = User()
    user_1.password = "myPassword"
    if user_1.is_valid_password("myPassword") is False:
        print("is_valid_password should return True if it's the right password")
