#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
'''
class OtherFrame(wx.Frame):
    """
    Class used for creating frames other than the main one
    """
 
    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        self.SetSize((800, 600))
        self.Show()
'''        
class PanelTwo(wx.Panel):
    
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent,size = (800,600),pos=(0,0))
        ebButton = wx.Button(self, label='Electricity Board', pos=(40, 180),size=(200,40))
    	l1 = wx.StaticText(self, -1, "CustomerID",pos=(310,40)) 

class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):

        self.panel1 = wx.Panel(self)
        pcButton = wx.Button(self.panel1, label='Power Company', pos=(40, 30),size=(200,40))
        dcButton = wx.Button(self.panel1, label='Distribution Company', pos=(40, 80),size=(200,40))
        tcButton = wx.Button(self.panel1, label='Transmission Company', pos=(40, 130),size=(200,40))
        ebButton = wx.Button(self.panel1, label='Electricity Board', pos=(40, 180),size=(200,40))
        pcButton.Bind(wx.EVT_BUTTON, self.OnClose)
        dcButton.Bind(wx.EVT_BUTTON, self.OnClose)
        tcButton.Bind(wx.EVT_BUTTON, self.OnClose)
        ebButton.Bind(wx.EVT_BUTTON, self.eb)
        
        l1 = wx.StaticText(self.panel1, -1, "CustomerID",pos=(310,40)) 
        self.t1 = wx.TextCtrl(self.panel1,pos=(400,30),size=(200,40))
        l1 = wx.StaticText(self.panel1, -1, "Password",pos=(310,90))
        self.t2 = wx.TextCtrl(self.panel1,style = wx.TE_PASSWORD,pos=(400,80),size=(200,40))
        loginButton = wx.Button(self.panel1, label='Login', pos=(515, 130))
        loginButton.Bind(wx.EVT_BUTTON, self.OnClose)
        
        
        self.SetSize((800, 600))
        self.SetTitle('Power Distribution System')
        self.Centre()

    def eb(self,e):
    	self.panel1.Hide()
    	self.SetTitle("Electricity Board")
        self.panel2= PanelTwo(self)
        #self.panel2.SetBackgroundColour("blue")
        self.panel2.Show()
        
        
        
    	
    def OnClose(self,e):

        self.Close(True)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()  

