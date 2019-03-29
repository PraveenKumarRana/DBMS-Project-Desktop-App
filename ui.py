#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
import MySQLdb as mdb
con = mdb.connect('localhost', 'admin', 'admin', 'eds')
w=0
h=0
class NewPanel(wx.Panel):

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent,size=(w,h),pos=(0,0))


class MainWindow(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent=None,style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.SetIcon(wx.Icon("display1.ico"))
        self.InitUI()


    def InitUI(self):

        global w,h

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnClose, fileItem)

        self.homepnl = wx.Panel(self)
        pcButton = wx.Button(self.homepnl, label='Power Company', pos=(40, 30),size=(200,40))
        dcButton = wx.Button(self.homepnl, label='Distribution Company', pos=(40, 80),size=(200,40))
        tcButton = wx.Button(self.homepnl, label='Transmission Company', pos=(40, 130),size=(200,40))
        ebButton = wx.Button(self.homepnl, label='Electricity Board', pos=(40, 180),size=(200,40))
        pcButton.Bind(wx.EVT_BUTTON, self.pc)
        dcButton.Bind(wx.EVT_BUTTON, self.dc)
        tcButton.Bind(wx.EVT_BUTTON, self.tc)
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
        ebButton = wx.Button(self.ebpnl, label='Back', pos=(1000, 10))
        self.p1=self.ebpnl
        self.p2=self.homepnl
    	ebButton.Bind(wx.EVT_BUTTON, self.back)
        #l1 = wx.StaticText(self.ebpnl, -1,"hello",pos=(10,10))
        with con:
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM electricityboard limit 4")
            rows = cur.fetchall()
            desc = cur.description

        wx.StaticText(self.ebpnl, -1,"Board Name",pos=(70,50))
        wx.StaticText(self.ebpnl, -1,"No. of Consumer",pos=(270,50))
        wx.StaticText(self.ebpnl, -1,"State",pos=(470,50))
        wx.StaticText(self.ebpnl, -1,"Power Consumed",pos=(600,50))
        dc = wx.ClientDC(self)
        dc.DrawLine(50, 60, 190, 60)

        #print "%s %s %s %s %s" % (desc[0][0], desc[1][0],desc[2][0],desc[3][0],desc[4][0])
        i=100
        for row in rows:
            #txt = row[desc[0][0]], row[desc[1][0]], row[desc[2][0]],row[desc[3][0]],row[desc[4][0]]
            wx.StaticText(self.ebpnl, -1,row[desc[0][0]],pos=(80,i))
            wx.StaticText(self.ebpnl, -1,str(row[desc[1][0]]),pos=(270,i))
            wx.StaticText(self.ebpnl, -1,row[desc[2][0]],pos=(470,i))
            wx.StaticText(self.ebpnl, -1,str(row[desc[4][0]]),pos=(600,i))

            i=i+30










        self.ebpnl.Show()

    def back(self,e):
    	self.p1.Hide()
    	self.p2.Show()
    	self.SetTitle(self.previousTitle)

    def pc(self,e):
        self.homepnl.Hide()
        self.previousTitle=self.GetTitle()
    	self.SetTitle("Power Company")
        self.pcpnl=NewPanel(self)
        BackButton = wx.Button(self.pcpnl, label='Back', pos=(60, 420),size=(100,40))
    	self.p1=self.pcpnl
    	self.p2=self.homepnl
    	BackButton.Bind(wx.EVT_BUTTON,self.back)
    	self.pcpnl.Show()


    def dc(self,e):
        self.homepnl.Hide()
        self.previousTitle=self.GetTitle()
    	self.SetTitle("Distribution Company")
        self.dcpnl=NewPanel(self)
        BackButton = wx.Button(self.dcpnl, label='Back', pos=(60, 420),size=(100,40))
    	self.p1=self.dcpnl
    	self.p2=self.homepnl
    	BackButton.Bind(wx.EVT_BUTTON,self.back)
    	self.dcpnl.Show()

    def tc(self,e):
        self.homepnl.Hide()
        self.previousTitle=self.GetTitle()
    	self.SetTitle("Transmission Company")
        self.tcpnl=NewPanel(self)
        BackButton = wx.Button(self.tcpnl, label='Back', pos=(60, 420),size=(100,40))
    	self.p1=self.tcpnl
    	self.p2=self.homepnl
    	BackButton.Bind(wx.EVT_BUTTON,self.back)
    	self.tcpnl.Show()





    def OnClose(self,e):

        self.Close(True)


def main():

    app = wx.App()
    ex = MainWindow(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
