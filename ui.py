#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx

class OtherFrame(wx.Frame):
    """
    Class used for creating frames other than the main one
    """

    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        self.SetSize((800, 600))
        self.Centre()
        pnl=ebPanel(self)




        self.Show()
class ebPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,pos,size)
        self.SetBackgroundColour("blue")
        self.Centre(self)
        #eb_back = wx.Button(self, label='Back')
        #eb_back.Bind(wx.EVT_BUTTON, self.OnClose1)
    def OnClose1(self,e):
        self.Close(True)

class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)
        pcButton = wx.Button(pnl, label='Power Company', pos=(40, 30),size=(200,40))
        dcButton = wx.Button(pnl, label='Distribution Company', pos=(40, 80),size=(200,40))
        tcButton = wx.Button(pnl, label='Transmission Company', pos=(40, 130),size=(200,40))
        ebButton = wx.Button(pnl, label='Electricity Board', pos=(40, 180),size=(200,40))
        pcButton.Bind(wx.EVT_BUTTON, self.OnClose)
        dcButton.Bind(wx.EVT_BUTTON, self.OnClose)
        tcButton.Bind(wx.EVT_BUTTON, self.OnClose)
        ebButton.Bind(wx.EVT_BUTTON, self.eb)

        l1 = wx.StaticText(pnl, -1, "CustomerID",pos=(310,40))
        self.t1 = wx.TextCtrl(pnl,pos=(400,30),size=(200,40))
        l1 = wx.StaticText(pnl, -1, "Password",pos=(310,90))
	self.t2 = wx.TextCtrl(pnl,style = wx.TE_PASSWORD,pos=(400,80),size=(200,40))
	loginButton = wx.Button(pnl, label='Login', pos=(515, 130))
	loginButton.Bind(wx.EVT_BUTTON, self.OnClose)


        self.SetSize((800, 600))
        self.SetTitle('wx.Button')
        self.Centre()

    def eb(self,e):
    	title = 'ELECTRICITY BOARD'
        #frame = OtherFrame(title=title)
        pnl=ebPanel(self,size=(100,100))








    def OnClose(self,e):

        self.Close(True)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
