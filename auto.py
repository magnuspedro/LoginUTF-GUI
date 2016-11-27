#!/usr/bin/python2.7
from File import File
from utfproxy import LoginUTF
from encryption import Encryption


class Auto(object):
    """docstring for Auto."""

    def AutoLogin(self):
        Crf = File()
        Encrypt = Encryption()

        if(Crf.isFile()):
            data = Crf.Open()
            ra = data[0]
            password = data[1]
            Login = LoginUTF(Encrypt.Decrypt(ra),Encrypt.Decrypt(password))
            return Login.Login()
        return False
