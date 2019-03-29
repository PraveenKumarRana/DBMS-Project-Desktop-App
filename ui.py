#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import MySQLdb as mdb
con = mdb.connect('localhost', 'root', 'mohd', 'eds')
import wx
w=0
h=0
with con:
    cur=con.cursor()
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

        l1 = wx.StaticText(self.homepnl, -1, "Customer ID : ",pos=(510,40))
        self.t1 = wx.TextCtrl(self.homepnl,style= wx.TE_PROCESS_ENTER,pos=(610,30),size=(200,40))
        l1 = wx.StaticText(self.homepnl, -1, "Password    : ",pos=(510,90))
        self.t2 = wx.TextCtrl(self.homepnl,style = wx.TE_PASSWORD|wx.TE_PROCESS_ENTER,pos=(610,80),size=(200,40))
        self.t1.Bind(wx.EVT_TEXT_ENTER,self.Login)
        self.t2.Bind(wx.EVT_TEXT_ENTER,self.Login)
        self.errormsg = wx.StaticText(self.homepnl, -1, " ",pos=(610,140))
        loginButton = wx.Button(self.homepnl, label='Log In', pos=(715, 170))
        loginButton.Bind(wx.EVT_BUTTON, self.Login)
        NacButton = wx.Button(self.homepnl, label='Not a Consumer', pos=(515, 170))
        NacButton.Bind(wx.EVT_BUTTON, self.EmpLoginForm)
        w,h=wx.GetDisplaySize()
        self.SetSize((w,h))
        self.SetMaxSize((w,h))
        self.SetMinSize((w,h))
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

    def EmpLoginForm(self,e):
        self.homepnl.Hide()
        self.previousTitle=self.GetTitle()
    	self.SetTitle("Employee Login")
        self.emplpnl=NewPanel(self)
        l1 = wx.StaticText(self.emplpnl, -1, "  Employee ID : ",pos=(510,40))
        self.t1 = wx.TextCtrl(self.emplpnl,style= wx.TE_PROCESS_ENTER,pos=(610,30),size=(200,40))
        l1 = wx.StaticText(self.emplpnl, -1, "Password    : ",pos=(510,90))
        self.t2 = wx.TextCtrl(self.emplpnl,style = wx.TE_PASSWORD|wx.TE_PROCESS_ENTER,pos=(610,80),size=(200,40))
        self.t1.Bind(wx.EVT_TEXT_ENTER,self.EmpLogin)
        self.t2.Bind(wx.EVT_TEXT_ENTER,self.EmpLogin)
        self.errormsg = wx.StaticText(self.emplpnl, -1, " ",pos=(610,140))
        loginButton = wx.Button(self.emplpnl, label='Log In', pos=(715, 170))
        loginButton.Bind(wx.EVT_BUTTON, self.EmpLogin)


        BackButton = wx.Button(self.emplpnl, label='Back', pos=(60, 420),size=(100,40))
    	self.p1=self.emplpnl
    	self.p2=self.homepnl
    	BackButton.Bind(wx.EVT_BUTTON,self.back)
    	self.emplpnl.Show()

    def UserProfile(self,e):
    	self.custpnl.Hide()
        self.previousTitle=self.GetTitle()
    	self.SetTitle("Profile")
        self.uppnl=NewPanel(self)
        cur.execute("select cid,cname,phone from consumer where cid=%s",(self.t1.GetValue(),))
        rows=cur.fetchall()
        phone=str(rows[0][2])
        custid=str(rows[0][0])
        l1=wx.StaticText(self.uppnl, -1, rows[0][1]+"'s Profile",pos=(310,70),size=(1000,1000),style=wx.ALIGN_CENTER)
        l1.SetFont(wx.Font(18, wx.MODERN, wx.NORMAL, wx.BOLD))
        l2 = wx.StaticText(self.uppnl, -1, "Consumer ID :   "+custid,pos=(610,170),size=(1000,1000))
        l3 = wx.StaticText(self.uppnl, -1, "Name        :   "+rows[0][1],pos=(610,270),size=(1000,1000))
        l4 = wx.StaticText(self.uppnl, -1, "Phone Number:   "+phone,pos=(610,370),size=(1000,1000))
        l5 = wx.StaticText(self.uppnl, -1, "Email ID    :   ",pos=(610,470),size=(1000,1000))
        l6 = wx.StaticText(self.uppnl, -1, "Address     :   ",pos=(610,570),size=(1000,1000))
        l2.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL))
        l3.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL))
        l4.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL))
        l5.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL))
        l6.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL))
        BackButton = wx.Button(self.uppnl, label='Back', pos=(60, 420),size=(100,40))
    	self.p1=self.uppnl
    	self.p2=self.custpnl
    	BackButton.Bind(wx.EVT_BUTTON,self.back)
    	#self.uppnl.SetBackgroundColour("blue")
    	self.uppnl.Show()

    def Login(self,e):
        if(self.t1.GetValue()):
            cur.execute("select password from consumer where cid=%s",(self.t1.GetValue(),))
            rows = cur.fetchall()
            if(len(rows)!=0 and self.t2.GetValue()==rows[0][0]):
                self.Customer(self)
            else:
                self.errormsg.SetForegroundColour((255,0,0))
                self.errormsg.SetLabel("Wrong Customer ID or Password!!")
        else:
            self.errormsg.SetForegroundColour((255,0,0))
            self.errormsg.SetLabel("Wrong Customer ID or Password!!")

    def EmpLogin(self,e):
        if(self.t1.GetValue()):
            cur.execute("select password from employee where eid=%s",(self.t1.GetValue(),))
            rows = cur.fetchall()
            if(len(rows)!=0 and self.t2.GetValue()==rows[0][0]):
                self.Customer(self)
            else:
                self.errormsg.SetForegroundColour((255,0,0))
                self.errormsg.SetLabel("Wrong Employee ID or Password!!")
        else:
            self.errormsg.SetForegroundColour((255,0,0))
            self.errormsg.SetLabel("Wrong Employee ID or Password!!")

    def Customer(self,e):
        self.homepnl.Hide()
        self.previousTitle=self.GetTitle()
    	self.SetTitle("User")
        self.custpnl=NewPanel(self)
        LogoutButton = wx.Button(self.custpnl, label='Logout', pos=(1270, 0),size=(80,30))
        cur.execute("select cname from consumer where cid=%s",(self.t1.GetValue(),))
        rows=cur.fetchall()
        ProfileButton = wx.Button(self.custpnl, label='Hi '+rows[0][0], pos=(1120, 0))
    	LogoutButton.Bind(wx.EVT_BUTTON,self.Logout)
        ProfileButton.Bind(wx.EVT_BUTTON,self.UserProfile)
        l1 = wx.StaticText(self.custpnl, -1, "Name",pos=(310,40))
        l1 = wx.StaticText(self.custpnl, -1, "Customer ID",pos=(310,70))
    	self.custpnl.Show()

    def Logout(self,e):
        self.t1.Clear()
        self.t2.Clear()
        self.errormsg.SetLabel(" ")
        self.p1=self.custpnl
    	self.p2=self.homepnl
        self.back(self)

    def OnClose(self,e):
        self.Close(True)


def main():

    app = wx.App()
    ex = MainWindow(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
