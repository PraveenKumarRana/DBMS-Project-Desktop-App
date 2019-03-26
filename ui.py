#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import wx
w=0
h=0
class NewPanel(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self, parent,pos=(0,0), size=(w,h))

		

class MainWindow(wx.Frame):

    def __init__(self, *args, **kw):
        super(MainWindow, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
    	global w,h

        self.home_pnl = wx.Panel(self)
        Elec_board_Button = wx.Button(self.home_pnl, label='Electrycity Board', pos=(60, 60),size=(200,40))
        Pc_board_Button = wx.Button(self.home_pnl, label='Power Company', pos=(60, 120),size=(200,40))
        Tc_board_Button = wx.Button(self.home_pnl, label='Transmission Company', pos=(60, 180),size=(200,40))
        Dc_board_Button = wx.Button(self.home_pnl, label='Distribution Company', pos=(60, 240),size=(200,40))
        

        Elec_board_Button.Bind(wx.EVT_BUTTON, self.e_board)
        Pc_board_Button.Bind(wx.EVT_BUTTON, self.OnClose)
        Tc_board_Button.Bind(wx.EVT_BUTTON, self.OnClose)
        Dc_board_Button.Bind(wx.EVT_BUTTON, self.OnClose)
        
        w,h=wx.GetDisplaySize()
        self.size=(w,h)
        self.SetSize(self.size)
        self.SetMaxSize(self.size)
        self.SetMinSize(self.size)
        self.SetTitle('wx.Button')
        self.Centre()
        
        self.t1 = wx.TextCtrl(self.home_pnl,pos=(500,150),size=(190,35)) 
        self.t2 = wx.TextCtrl(self.home_pnl,style = wx.TE_PASSWORD,pos=(500,210),size=(190,35))
        MainWindow_Button = wx.Button(self.home_pnl, label='MainWindow', pos=(605, 270))
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
        l1 = wx.StaticText(self.home_pnl, -1, "User Id",pos=(400,157))
        hbox2 = wx.BoxSizer(wx.HORIZONTAL) 
        l2 = wx.StaticText(self.home_pnl, -1, "Password",pos=(400,217)) 
        
        


    def e_board(self, e):

    	self.home_pnl.Hide();
    	self.eb_pnl=NewPanel(self)
    	Back_Button = wx.Button(self.eb_pnl, label='Back', pos=(60, 420),size=(100,40))
    	self.p1=self.home_pnl
    	self.p2=self.eb_pnl
    	Back_Button.Bind(wx.EVT_BUTTON,self.eb_back)
    	self.eb_pnl.Show()
    	
    def eb_back(self,e):
    	self.p2.Hide()
    	self.p1.Show()
    	
    def OnClose(self,e1):
    	self.Close(True)


def main():

    app = wx.App()
    ex = MainWindow(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()  
