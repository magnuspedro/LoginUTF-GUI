#!/usr/bin/python2.7
import base64

class Encryption(object):
    """docstring for Encryption."""

    def Encrypt(self,encrypt):
        return base64.b64encode(encrypt)

    def Decrypt(self, decrypt):
        return base64.b64decode(decrypt)
