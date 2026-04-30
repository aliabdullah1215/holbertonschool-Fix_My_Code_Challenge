#!/usr/bin/python3

class User:
    def __init__(self):
        self.__password = None

    def set_password(self, pwd):
        if pwd is None:
            self.__password = None
        else:
            self.__password = pwd

    def is_valid_password(self, pwd):
        if self.__password is None:
            return False
        return self.__password == pwd
