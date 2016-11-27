#!/usr/bin/python2.7
import requests
import re

#logging.captureWarnings(True)
#requests.packages.urllib3.disable_warnings()

class LoginUTF(object):
    """docstring for LoginUTF."""

    urlLogin = "https://1.1.1.1/login.html"
    urlLogout = "https://1.1.1.1/logout.html"
    data = ""

    def __init__(self,ra,password):
        self.ra = ra
        self.password = password


    def Login(self):
        try:

            payload = {'buttonClicked':'4','err_flag':'0','err_msg':'','info_flag':0,'info_msg':'','redirect_url':'','username':self.ra,'password':self.password}
            headers = {'Referer': self.urlLogin}
            response = requests.post(self.urlLogin, data=payload, headers=headers, verify=False)

            self.data = response.text
            result = open("/tmp/result.html",'w')
            result.write(self.data)

        except Exception as e:
            raise

        finally:
            if re.search("Login Successful",self.data):
                #print ("\033[1;32mLogin Successful\033[0m")
                return True
            else:
                #print ("\033[1;31mLogin Fail ;-;\033[0m")
                return False


    def Logout(self):
        try:
            payload = {'userStatus':'1','err_flag':'0','err_msg':''}
            headers = {'Referer':self.urlLogout}
            response = requests.post(self.urlLogout, data=payload, headers=headers, verify=False)

            self.data = response.text

        except Exception as e:
            pass

        finally:

            if re.search("To complete the log off process and to prevent access to unauthorize",self.data):
                print ("\033[1;32mLogout Successful\033[0m")
                return True
            else:
                print ("\033[1;31mLogout Fail ;-;\033[0m")
                return False

    def getUrlLogin(self):
        return self.urlLogin

    def getUrlLogout(self):
        return self.urlLogout

    def getRA(self):
        return self.ra

    def setRA(sef,ra):
        ra = self.ra

    def setPassword(self,password):
        password = self.password

    def getPassword(self):
        return self.password
