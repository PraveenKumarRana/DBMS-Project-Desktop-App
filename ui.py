#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
w=0
h=0
class NewPanel(wx.Panel):
    
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent,size=(w,h),pos=(0,0))
        

class MainWindow(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent=None,style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.InitUI()

    def InitUI(self):

        global w,h
        self.homepnl = wx.Panel(self)
        pcButton = wx.Button(self.homepnl, label='Power Company', pos=(40, 30),size=(200,40))
        dcButton = wx.Button(self.homepnl, label='Distribution Company', pos=(40, 80),size=(200,40))
        tcButton = wx.Button(self.homepnl, label='Transmission Company', pos=(40, 130),size=(200,40))
        ebButton = wx.Button(self.homepnl, label='Electricity Board', pos=(40, 180),size=(200,40))
        pcButton.Bind(wx.EVT_BUTTON, self.OnClose)
        dcButton.Bind(wx.EVT_BUTTON, self.OnClose)
        tcButton.Bind(wx.EVT_BUTTON, self.OnClose)
        ebButton.Bind(wx.EVT_BUTTON, self.eb)
        
        l1 = wx.StaticText(self.homepnl, -1, "CustomerID",pos=(310,40)) 
        self.t1 = wx.TextCtrl(self.homepnl,pos=(400,30),size=(200,40))
        l1 = wx.StaticText(self.homepnl, -1, "Password",pos=(310,90))
        self.t2 = wx.TextCtrl(self.homepnl,style = wx.TE_PASSWORD,pos=(400,80),size=(200,40))
        loginButton = wx.Button(self.homepnl, label='Login', pos=(515, 130))
        loginButton.Bind(wx.EVT_BUTTON, self.OnClose)
        w,h=wx.GetDisplaySize()
        self.SetSize((w,h))
        self.SetTitle('Power Distribution System')
        self.Centre()

    def eb(self,e):
    	self.homepnl.Hide()
    	self.previousTitle=self.GetTitle()
    	self.SetTitle("Electricity Board")
        self.ebpnl= NewPanel(self)
        ebButton = wx.Button(self.ebpnl, label='Back', pos=(10, 10))
        self.p1=self.ebpnl
        self.p2=self.homepnl
    	ebButton.Bind(wx.EVT_BUTTON, self.back)
    	#l1 = wx.StaticText(self, -1, "CustomerID",pos=(310,40)) 
        self.ebpnl.SetBackgroundColour("blue")
        self.ebpnl.Show()
        
    def back(self,e):
    	self.p1.Hide()
    	self.p2.Show()
    	self.SetTitle(self.previousTitle)
    	
        
        
        
    	
    def OnClose(self,e):

        self.Close(True)


def main():

    app = wx.App()
    ex = MainWindow(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()  

