#!/usr/bin/python2.7
import os

class File(object):
    """docstring for File."""


    def Save(self,ra,password):
        with open("info",'w') as file:
            file.write(ra+"\n")
            file.write(password)

    def Open(self):
        with open("info",'r') as file:
            ra = file.readline()
            password = file.readline()
            return ra,password

    def isFile(self):
        return os.path.isfile("info")
