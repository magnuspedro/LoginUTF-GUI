#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import wx
import sys
import os
from utfproxy import LoginUTF
from encryption import Encryption
from File import File
from auto import Auto

#logging.captureWarnings(True)
#requests.packages.urllib3.disable_warnings()

setExit = False

class GUILogin(wx.Frame):
    """docstring for GUILogin."""
    def __init__(self, parent, title):
        super(GUILogin, self).__init__(parent, title=title,size=(200, 200))
        self.InitUI()
        self.Centre()
        self.Show()
        VRA = Auto()
        global setExit
        if(VRA.AutoLogin()):
            setExit=True


    def InitUI(self):

        panel = wx.Panel(self)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        st1 = wx.StaticText(panel, label='Matricula')
        hbox1.Add(st1, flag=wx.ALL|wx.CENTER, border=8)

        self.ra = wx.TextCtrl(panel)
        hbox1.Add(self.ra, flag=wx.ALL,proportion=1)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        st2 = wx.StaticText(panel, label='Senha      ')
        hbox2.Add(st2, flag=wx.ALL|wx.CENTER, border=8)

        self.password = wx.TextCtrl(panel,style=wx.TE_PASSWORD)
        hbox2.Add(self.password, flag=wx.ALL, proportion=1)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)


        search = wx.Button(panel,label='Login')
        hbox3.Add(search, flag=wx.ALIGN_CENTER, border=8)

        vbox.Add(hbox1, flag=wx.ALL, border=10)
        vbox.Add(hbox2, flag=wx.ALL, border=10)
        vbox.Add(hbox3, flag=wx.ALL|wx.CENTER, border=10)


        vbox.Add((-1, 10))


        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.GetText, search)


    def GetText(self,evt):
        text = ""
        ra = self.ra.GetValue()
        password = self.password.GetValue()

        Encrypt = Encryption()
        Crf = File()

        Crf.Save(Encrypt.Encrypt(ra),Encrypt.Encrypt(password))
        Login = LoginUTF(ra,password)
        if Login.Login():
            SM = wx.MessageBox("Login Successful", "Login",
                            wx.OK);
            SM.ShowModal()
        else:
            FM = wx.MessageBox("Login Unsuccessful", "Login",
                            wx.OK);
            FM.ShowModal()


if __name__ == '__main__':

    app = wx.App()
    GUILogin(None, title='Login UTFPR')
    if(setExit == False):
        app.MainLoop()
