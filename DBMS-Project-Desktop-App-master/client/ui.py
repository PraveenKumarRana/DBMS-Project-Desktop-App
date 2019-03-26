#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import wx

class Login(wx.Frame):

    def __init__(self, *args, **kw):
        super(Login, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)
        Elec_board_Button = wx.Button(pnl, label='Electrycity Board', pos=(60, 60),size=(200,40))
        Pc_board_Button = wx.Button(pnl, label='Power Company', pos=(60, 120),size=(200,40))
        Tc_board_Button = wx.Button(pnl, label='Transmission Company', pos=(60, 180),size=(200,40))
        Dc_board_Button = wx.Button(pnl, label='Distribution Company', pos=(60, 240),size=(200,40))
        

        Elec_board_Button.Bind(wx.EVT_BUTTON, self.OnClose)
        Pc_board_Button.Bind(wx.EVT_BUTTON, self.OnClose)
        Tc_board_Button.Bind(wx.EVT_BUTTON, self.OnClose)
        Dc_board_Button.Bind(wx.EVT_BUTTON, self.OnClose)

        self.SetSize((800, 500))
        self.SetTitle('wx.Button')
        self.Centre()
        
        self.t1 = wx.TextCtrl(pnl,pos=(500,150),size=(190,35)) 
        self.t2 = wx.TextCtrl(pnl,style = wx.TE_PASSWORD,pos=(500,210),size=(190,35))
        Login_Button = wx.Button(pnl, label='Login', pos=(605, 270))
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
        l1 = wx.StaticText(pnl, -1, "User Id",pos=(400,157))
        hbox2 = wx.BoxSizer(wx.HORIZONTAL) 
        l2 = wx.StaticText(pnl, -1, "Password",pos=(400,217)) 

    def OnClose(self, e):

        self.Close(True)


def main():

    app = wx.App()
    ex = Login(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()  
