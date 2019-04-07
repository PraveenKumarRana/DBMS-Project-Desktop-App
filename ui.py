#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from functools import partial
import wx
import string
from random import*
import wx.lib.scrolledpanel as scrolled
import MySQLdb as mdb
con = mdb.connect('localhost', 'admin', 'admin', 'eds')

with con:
    cur=con.cursor()
class HeadNewPanel(wx.Panel):

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent,size=(w,100),pos=(0,0))
        l1=wx.StaticText(self, -1,"Power Distribution System",pos=(430,30),size=(300,30),style = wx.ALIGN_CENTER)
        l1.SetFont(wx.Font(30,wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD))
class NewPanel(wx.Panel):

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent,size=(w,h-100),pos=(0,100))
        self.Bind(wx.EVT_PAINT, self.OnPaintN)
    def OnPaintN(self,e) :
        dc = wx.PaintDC(self)
        dc.SetBrush(wx.Brush(wx.Colour(255,255,255)))
        dc.DrawRectangle(10, 10, 1346, 500)

class upperNewPanel(wx.Panel):

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent,size=(w,165),pos=(0,100))
class lowerNewPanel(wx.Panel):

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent,size=(w,h-265),pos=(0,220))

class MainWindow(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent=None,style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.SetIcon(wx.Icon("display1.ico"))
        global w,h
        w,h=wx.GetDisplaySize()
        self.InitUI()


    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnClose, fileItem)

        self.headpnl=HeadNewPanel(self)
        self.headpnl.SetBackgroundColour("blue")

        self.homepnl = NewPanel(self)
        pcButton = wx.Button(self.homepnl, label='Power Company', pos=(40, 150),size=(200,40))
        dcButton = wx.Button(self.homepnl, label='Distribution Company', pos=(40, 200),size=(200,40))
        tcButton = wx.Button(self.homepnl, label='Transmission Company', pos=(40, 250),size=(200,40))
        ebButton = wx.Button(self.homepnl, label='Electricity Board', pos=(40, 300),size=(200,40))


        pcButton.Bind(wx.EVT_BUTTON, self.pc)
        dcButton.Bind(wx.EVT_BUTTON, self.dc)
        tcButton.Bind(wx.EVT_BUTTON, self.tc)
        ebButton.Bind(wx.EVT_BUTTON, self.eb)

        l0 = wx.StaticText(self.homepnl, -1, "Customer Login ",pos=(600,170),size=(500,500))
        l0.SetFont(wx.Font(16,wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        errormsg = wx.StaticText(self.homepnl, -1, " ",pos=(610,340))
        l1 = wx.StaticText(self.homepnl, -1, "Customer ID : ",pos=(510,240))
        t1 = wx.TextCtrl(self.homepnl,style= wx.TE_PROCESS_ENTER,pos=(610,230),size=(200,40))
        l1 = wx.StaticText(self.homepnl, -1, "Password    : ",pos=(510,290))
        t2 = wx.TextCtrl(self.homepnl,style = wx.TE_PASSWORD|wx.TE_PROCESS_ENTER,pos=(610,280),size=(200,40))
        t1.Bind(wx.EVT_TEXT_ENTER,partial(self.Login,t1=t1,t2=t2,errormsg=errormsg))
        t2.Bind(wx.EVT_TEXT_ENTER,partial(self.Login,t1=t1,t2=t2,errormsg=errormsg))

        loginButton = wx.Button(self.homepnl, label='Log In', pos=(715, 370))
        loginButton.Bind(wx.EVT_BUTTON, partial(self.Login,t1=t1,t2=t2,errormsg=errormsg))
        NacButton = wx.Button(self.homepnl, label='Not a Consumer', pos=(515, 370))
        NacButton.Bind(wx.EVT_BUTTON, partial(self.EmpLoginForm,pt1=t1,pt2=t2,perrormsg=errormsg))
        newConButton = wx.Button(self.homepnl, label='Apply New Connection', pos=(1000,20),size=(200,40))
        newConButton.Bind(wx.EVT_BUTTON,self.newConnection)
        statBtn = wx.Button(self.homepnl, label='Know Your Conn. status', pos=(1000,80),size=(200,40))
        statBtn.Bind(wx.EVT_BUTTON,self.ncStat)
        #w,h=wx.GetDisplaySize()
        self.SetSize((w,h))
        self.SetMaxSize((w,h))
        self.SetMinSize((w,h))
        self.SetTitle('Power Distribution System')
        self.Centre()
        self.homepnl.Bind(wx.EVT_PAINT, partial(self.OnPaint,op=self.homepnl))
        #self.Centre()
        #self.Show(True)


    def OnPaint(self,e,op):
        dc = wx.PaintDC(op)
        dc.SetBrush(wx.Brush(wx.Colour(255,255,255)))
        dc.DrawRectangle(10, 10, 1346, 500)
        dc.SetBrush(wx.Brush(wx.Colour(220,217,217)))
        dc.DrawRectangle(450, 160, 480, 290)

    def ncStat(self,e):
        self.homepnl.Hide()
        self.previousTitle=self.GetTitle()
        self.SetTitle("Application Status form New Connection")
        self.ncstatpnl=NewPanel(self)
        l1=wx.StaticText(self.ncstatpnl, -1, "Provide your ref_id :",pos=(400,300),size=(500,500))
        self.t222 = wx.TextCtrl(self.ncstatpnl,style= wx.TE_PROCESS_ENTER,pos=(600,300),size=(200,40))
        knowstatButton = wx.Button(self.ncstatpnl, label='submit', pos=(650, 370))
        knowstatButton.Bind(wx.EVT_BUTTON, self.ncstatsubmit)
        backButton = wx.Button(self.ncstatpnl, label='Back', pos=(1000, 10))
        backButton.Bind(wx.EVT_BUTTON, partial(self.back,p1=self.ncstatpnl,p2=self.homepnl,title="Power Distribution System"))

    def ncstatsubmit(self,e):
        if(self.t222.GetValue()):
            cur.execute("select status from ncstatus where refid=%s",(self.t222.GetValue(),))
            rows=cur.fetchall()
            print len(rows)
            if(len(rows)!=0):
                self.ncstatpnl.Hide()
                self.previousTitle=self.GetTitle()
                self.SetTitle("Status for New Connection")
                self.statpnl=NewPanel(self)
                backButton = wx.Button(self.statpnl, label='Back', pos=(1000, 10))
                backButton.Bind(wx.EVT_BUTTON, partial(self.back,p1=self.statpnl,p2=self.ncstatpnl,title="Application Status form New Connection"))
                l1=wx.StaticText(self.statpnl, -1,'Status  : ',              pos=(980,350),size=(500,500))
                l1.SetFont(wx.Font(15,wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
                l2=wx.StaticText(self.statpnl, -1, rows[0][0] ,  pos=(1100,350),size=(500,500))
                l2.SetFont(wx.Font(15,wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

                l3=wx.StaticText(self.statpnl, -1,'Reference no. : ',              pos=(900,150),size=(500,500))
                l3.SetFont(wx.Font(15,wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
                l4=wx.StaticText(self.statpnl, -1, self.t222.GetValue() ,  pos=(1100,150),size=(500,500))
                l4.SetFont(wx.Font(15,wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
                if rows[0][0]=='Aproved' :
                    msg='Hi Your Application has been succesfuly Aproved !!'
                    wx.MessageBox(message=msg,caption='Info',style=wx.OK | wx.ICON_INFORMATION)

                    wx.StaticText(self.statpnl, -1,'Applicant Name :',          pos=(100,100),size=(500,500))
                    wx.StaticText(self.statpnl, -1,'Consumer id    :',          pos=(100,130),size=(500,500))
                    wx.StaticText(self.statpnl, -1,'Phone no       :',          pos=(100,160),size=(500,500))
                    wx.StaticText(self.statpnl, -1,'Boardname      :',          pos=(100,190),size=(500,500))
                    wx.StaticText(self.statpnl, -1,'State          :',          pos=(100,220),size=(500,500))
                    wx.StaticText(self.statpnl, -1,'Subdivision    :',          pos=(100,250),size=(500,500))
                    wx.StaticText(self.statpnl, -1,'Division       :',          pos=(100,280),size=(500,500))
                    wx.StaticText(self.statpnl, -1,'City           :',          pos=(100,310),size=(500,500))
                    wx.StaticText(self.statpnl, -1,'Meter no.      :',          pos=(100,340),size=(500,500))
                    wx.StaticText(self.statpnl, -1,'Email id       :',          pos=(100,370),size=(500,500))
                    wx.StaticText(self.statpnl, -1,'Insta.. add    :',          pos=(100,400),size=(500,500))

                    cur.execute("select * from consumer c,ncstatus n where c.cid=n.cid and refid=%s",(self.t222.GetValue(),))
                    d=cur.fetchall()
                    self.t222.Clear()
                    wx.StaticText(self.statpnl, -1, d[0][1]  ,  pos=(260,100),size=(500,500))
                    wx.StaticText(self.statpnl, -1, str(d[0][0]) ,  pos=(260,130),size=(500,500))
                    wx.StaticText(self.statpnl, -1, str(d[0][2])  ,  pos=(260,160),size=(500,500))
                    wx.StaticText(self.statpnl, -1, d[0][3] ,  pos=(260,190),size=(500,500))
                    wx.StaticText(self.statpnl, -1, d[0][4] ,  pos=(260,220),size=(500,500))
                    wx.StaticText(self.statpnl, -1, d[0][5] ,  pos=(260,250),size=(500,500))
                    wx.StaticText(self.statpnl, -1, d[0][6]  ,  pos=(260,280),size=(500,500))
                    wx.StaticText(self.statpnl, -1, d[0][7] ,  pos=(260,310),size=(500,500))
                    wx.StaticText(self.statpnl, -1, str(d[0][8]) ,  pos=(260,340),size=(500,500))
                    wx.StaticText(self.statpnl, -1, d[0][10] ,  pos=(260,370),size=(500,500))
                    wx.StaticText(self.statpnl, -1, d[0][11] ,  pos=(260,400),size=(500,500))

                    l2.SetForegroundColour((0,255,0))
                else:
                    if rows[0][0]=='pending' :
                        wx.StaticText(self.statpnl, -1,'Applicant Name :',          pos=(100,100),size=(500,500))
                        wx.StaticText(self.statpnl, -1,'Phone no       :',          pos=(100,130),size=(500,500))
                        wx.StaticText(self.statpnl, -1,'Boardname      :',          pos=(100,160),size=(500,500))
                        wx.StaticText(self.statpnl, -1,'State          :',          pos=(100,190),size=(500,500))
                        wx.StaticText(self.statpnl, -1,'Subdivision    :',          pos=(100,220),size=(500,500))
                        wx.StaticText(self.statpnl, -1,'Division       :',          pos=(100,250),size=(500,500))
                        wx.StaticText(self.statpnl, -1,'City           :',          pos=(100,280),size=(500,500))
                        wx.StaticText(self.statpnl, -1,'Email id       :',          pos=(100,310),size=(500,500))
                        wx.StaticText(self.statpnl, -1,'Insta.. add    :',          pos=(100,340),size=(500,500))
                        cur.execute("select * from newconnection where refid=%s",(self.t222.GetValue(),))
                        dt=cur.fetchall()
                        print dt
                        wx.StaticText(self.statpnl, -1, dt[0][0]  ,      pos=(260,100),size=(500,500))
                        wx.StaticText(self.statpnl, -1, str(dt[0][1]) ,  pos=(260,130),size=(500,500))
                        wx.StaticText(self.statpnl, -1, dt[0][2]  ,      pos=(260,160),size=(500,500))
                        wx.StaticText(self.statpnl, -1, dt[0][3] ,       pos=(260,190),size=(500,500))
                        wx.StaticText(self.statpnl, -1, dt[0][4] ,       pos=(260,220),size=(500,500))
                        wx.StaticText(self.statpnl, -1, dt[0][5] ,       pos=(260,250),size=(500,500))
                        wx.StaticText(self.statpnl, -1, dt[0][6]  ,      pos=(260,280),size=(500,500))
                        wx.StaticText(self.statpnl, -1, dt[0][7] ,       pos=(260,310),size=(500,500))
                        wx.StaticText(self.statpnl, -1, dt[0][8] ,       pos=(260,340),size=(500,500))
                        msg='Hi Your Application is Pending \n \n and is under verification process'
                        l2.SetForegroundColour((0,0,255))
                    else:
                        msg='Hi Your Application has been rejected'
                        l2.SetForegroundColour((255,0,0))
                    wx.MessageBox(message=msg,caption='Info',style=wx.OK | wx.ICON_INFORMATION)

                    self.t222.Clear()
            else:
                msg=wx.StaticText(self.ncstatpnl, -1, "Invalid reference id !!",pos=(600,250),size=(300,300))
                msg.SetForegroundColour((255,0,0))

        else:
            msg=wx.StaticText(self.ncstatpnl, -1, "Enter your reference id!!",pos=(600,250),size=(300,300))
            msg.SetForegroundColour((255,0,0))

    def newConnection(self,e):
        self.homepnl.Hide()

        self.SetTitle("Application for New Connection")
        self.ncpnl=NewPanel(self)
        #self.ncpnl.SetBackgroundColour((232,232,232))
        ebButton = wx.Button(self.ncpnl, label='Back', pos=(1000, 10))
        ebButton.Bind(wx.EVT_BUTTON, partial(self.back,p1=self.ncpnl,p2=self.homepnl,title="Power Distribution System"))

        l1=wx.StaticText(self.ncpnl, -1, "State/UT :",pos=(w/2-200,180),size=(500,500))
        l2=wx.StaticText(self.ncpnl, -1, "Distribution Company :",pos=(w/2-200,230),size=(500,500))
        l3=wx.StaticText(self.ncpnl, -1, "Division :",pos=(w/2-200,280),size=(500,500))
        l4=wx.StaticText(self.ncpnl, -1, "Sub Division :",pos=(w/2-200,330),size=(500,500))
        l1.SetFont(wx.Font(12,wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        l2.SetFont(wx.Font(12,wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        l3.SetFont(wx.Font(12,wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        l4.SetFont(wx.Font(12,wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("select state from distributioncompany")
        rows=cur.fetchall()
        #desc = cur.description()
        stateList=list()
        for row in rows:
            stateList.append(row["state"])
        print stateList
        self.cbState=wx.ComboBox(self.ncpnl,pos=(w/2,180),choices=stateList)
        self.cbState.Bind(wx.EVT_COMBOBOX, self.ncDcSelect)
        #self.ncpnl.Bind(wx.EVT_PAINT, partial(self.OnPaint,op=self.ncpnl))



    def ncDcSelect(self,e):
        self.state=e.GetString()
        print self.state
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("select dname from distributioncompany where state = %s",(self.state,))
        rows=cur.fetchall()
        dcList=list()
        for row in rows:
            dcList.append(row["dname"])
        print dcList
        self.cbDc=wx.ComboBox(self.ncpnl,pos=(w/2,230),choices=dcList)
        self.cbDc.Bind(wx.EVT_COMBOBOX, self.ncDivSelect)

    def ncDivSelect(self,e):
        self.Dc=e.GetString()
        print self.Dc
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("select divname from division as d1,distributioncompany as d2 where d1.did=d2.did and d2.dname=%s and d2.state=%s ",(self.Dc,self.state))
        rows=cur.fetchall()
        divList=list()
        for row in rows:
            divList.append(row["divname"])
        print divList
        self.cbDc=wx.ComboBox(self.ncpnl,pos=(w/2,280),choices=divList)
        self.cbDc.Bind(wx.EVT_COMBOBOX, self.ncSubdivSelect)
    def ncSubdivSelect(self,e):
        self.Div=e.GetString()
        print self.Div
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("select sdivname from subdivision as d1,division as d2 where d1.divid=d2.divid and d1.state=%s and d2.divname=%s",(self.state,self.Div))
        rows=cur.fetchall()
        sdivList=list()
        for row in rows:
            sdivList.append(row["sdivname"])
        print sdivList
        self.cbDc=wx.ComboBox(self.ncpnl,pos=(w/2,330),choices=sdivList)
        self.cbDc.Bind(wx.EVT_COMBOBOX, self.submit_form1)

    def submit_form1(self,e):
        self.Subdiv=e.GetString()
        print self.Subdiv
        submitForm=wx.Button(self.ncpnl, label='Submit', pos=(w/2-100, 380))
        submitForm.Bind(wx.EVT_BUTTON,self.NewconForm)

    def eb(self,e):
    	self.homepnl.Hide()

    	self.SetTitle("Electricity Board")
        self.upnl= upperNewPanel(self)
        self.lpnl=lowerNewPanel(self)
        #self.lpnl.SetBackgroundColour("blue")
        ebButton = wx.Button(self.upnl, label='Back', pos=(1000, 10))
    	ebButton.Bind(wx.EVT_BUTTON, partial(self.back_tc_pc_dc_eb,p1=self.upnl,p2=self.homepnl,title="Power Distribution System"))
        #l1 = wx.StaticText(self.ebpnl, -1,"hello",pos=(10,10))

        self.ebNameSearch=wx.SearchCtrl(self.upnl,pos=(120,50),size=(200,40))
        self.ebNameSearch.SetDescriptiveText("Search by B.name")
        self.ebNameSearch.Bind(wx.EVT_TEXT,self.ebNameS)


        ebAll = wx.Button(self.upnl, label='Show all', pos=(10, 50),size=(100,40))
        ebAll.Bind(wx.EVT_BUTTON, self.ebAll)
        wx.StaticText(self.upnl, -1,"State/UT:",pos=(500,60))
        t1 = wx.SearchCtrl(self.upnl,pos=(570,50),size=(200,40))
        t1.SetDescriptiveText("Search by State/UT")
        self.ebStateSB=t1
        t1.Bind(wx.EVT_TEXT,partial(self.ebStateSearch,t1=t1))
        if(t1.GetValue()==""):
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM electricityboard ")
            rows = cur.fetchall()
            desc = cur.description

            wx.StaticText(self.upnl, -1,"Board Name",pos=(70,100))
            wx.StaticText(self.upnl, -1,"No. of Consumer",pos=(270,100))
            wx.StaticText(self.upnl, -1,"State/UT",pos=(470,100))
            wx.StaticText(self.upnl, -1,"Power Consumed",pos=(600,100))

            #print "%s %s %s %s %s" % (desc[0][0], desc[1][0],desc[2][0],desc[3][0],desc[4][0])
            i=20
            for row in rows:
                #txt = row[desc[0][0]], row[desc[1][0]], row[desc[2][0]],row[desc[3][0]],row[desc[4][0]]
                wx.StaticText(self.lpnl, -1,row[desc[0][0]],pos=(80,i))
                wx.StaticText(self.lpnl, -1,str(row[desc[1][0]]),pos=(270,i))
                wx.StaticText(self.lpnl, -1,row[desc[2][0]],pos=(470,i))
                wx.StaticText(self.lpnl, -1,str(row[desc[4][0]]),pos=(600,i))

                i=i+30
        #self.lpnl.Show()


    def ebNameS(self,e):
        if(self.ebStateSB.IsEmpty()==0):
            self.ebStateSB.Clear()        #searching by boardname(dynamically)
        self.lpnl.Hide()
        name=e.GetString()
        self.lpnl=lowerNewPanel(self)
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("select * FROM electricityboard where boardname like '{}%'".format(name))
        rows=cur.fetchall()
        desc = cur.description
        if(len(rows)==0):
            msg=wx.StaticText(self.lpnl, -1,"Not available !!",pos=(300,30))
            msg.SetForegroundColour((255,0,0))
        i=20
        for row in rows:
            wx.StaticText(self.lpnl, -1,row[desc[0][0]],pos=(80,i))
            wx.StaticText(self.lpnl, -1,str(row[desc[1][0]]),pos=(270,i))
            wx.StaticText(self.lpnl, -1,row[desc[2][0]],pos=(470,i))
            wx.StaticText(self.lpnl, -1,str(row[desc[4][0]]),pos=(600,i))
            i=i+30


    def ebAll(self,e):
        if(self.ebNameSearch.IsEmpty()==0):
            self.ebNameSearch.Clear()
        if(self.ebStateSB.IsEmpty()==0):
            self.ebStateSB.Clear()

        self.lpnl.Hide()
        self.lpnl=lowerNewPanel(self)
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM electricityboard ")
        rows = cur.fetchall()
        desc = cur.description
        #print "%s %s %s %s %s" % (desc[0][0], desc[1][0],desc[2][0],desc[3][0],desc[4][0])
        i=20
        for row in rows:
            #txt = row[desc[0][0]], row[desc[1][0]], row[desc[2][0]],row[desc[3][0]],row[desc[4][0]]
            wx.StaticText(self.lpnl, -1,row[desc[0][0]],pos=(80,i))
            wx.StaticText(self.lpnl, -1,str(row[desc[1][0]]),pos=(270,i))
            wx.StaticText(self.lpnl, -1,row[desc[2][0]],pos=(470,i))
            wx.StaticText(self.lpnl, -1,str(row[desc[4][0]]),pos=(600,i))
            i=i+30
    def ebStateSearch(self,e,t1):
        if(self.ebNameSearch.IsEmpty()==0):
            self.ebNameSearch.Clear()
        if(t1.GetValue()):
            self.lpnl.Hide()

            self.lpnl=lowerNewPanel(self)

            #lpnl.SetBackgroundColour("grey")
            print "hello"
            self.lpnl.Show()
            print t1.GetValue()
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM electricityboard where state like '{}%'".format(t1.GetValue()))
            rows = cur.fetchall()
            desc = cur.description
            if(len(rows)==0):
                msg=wx.StaticText(self.lpnl, -1,"Not available !!",pos=(300,30))
                msg.SetForegroundColour((255,0,0))
            #wx.StaticText(lpnl, -1,"Board Name",pos=(70,100))
            #wx.StaticText(lpnl, -1,"No. of Consumer",pos=(270,100))
            #wx.StaticText(lpnl, -1,"State",pos=(470,100))
            #wx.StaticText(lpnl, -1,"Power Consumed",pos=(600,100))
            dc = wx.ClientDC(self)
            dc.DrawLine(50, 60, 190, 60)
            #print "%s %s %s %s %s" % (desc[0][0], desc[1][0],desc[2][0],desc[3][0],desc[4][0])
            i=20
            for row in rows:
                #txt = row[desc[0][0]], row[desc[1][0]], row[desc[2][0]],row[desc[3][0]],row[desc[4][0]]
                wx.StaticText(self.lpnl, -1,row[desc[0][0]],pos=(80,i))
                wx.StaticText(self.lpnl, -1,str(row[desc[1][0]]),pos=(270,i))
                wx.StaticText(self.lpnl, -1,row[desc[2][0]],pos=(470,i))
                wx.StaticText(self.lpnl, -1,str(row[desc[4][0]]),pos=(600,i))

                i=i+30
        if(t1.GetValue()==""):
            self.lpnl.Hide()
            self.lpnl=lowerNewPanel(self)
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM electricityboard ")
            rows = cur.fetchall()
            desc = cur.description
            #print "%s %s %s %s %s" % (desc[0][0], desc[1][0],desc[2][0],desc[3][0],desc[4][0])
            i=20
            for row in rows:
                #txt = row[desc[0][0]], row[desc[1][0]], row[desc[2][0]],row[desc[3][0]],row[desc[4][0]]
                wx.StaticText(self.lpnl, -1,row[desc[0][0]],pos=(80,i))
                wx.StaticText(self.lpnl, -1,str(row[desc[1][0]]),pos=(270,i))
                wx.StaticText(self.lpnl, -1,row[desc[2][0]],pos=(470,i))
                wx.StaticText(self.lpnl, -1,str(row[desc[4][0]]),pos=(600,i))

                i=i+30

    def tcStateSearch(self,e,t1):
        if(t1.GetValue()):
            self.lpnl.Hide()
            self.lpnl=lowerNewPanel(self)
            self.lpnl.Show()

            #self.currentpnl.SetBackgroundColour("pink")
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM transmissioncompany where state=%s",(t1.GetValue(),))
            rows = cur.fetchall()
            desc = cur.description
            i=20
            for row in rows:
                #txt = row[desc[0][0]], row[desc[1][0]], row[desc[2][0]],row[desc[3][0]],row[desc[4][0]]
                wx.StaticText(self.lpnl, -1,row[desc[1][0]],pos=(100,i))
                wx.StaticText(self.lpnl, -1,row[desc[4][0]],pos=(300,i))
                wx.StaticText(self.lpnl, -1,str(row[desc[3][0]]),pos=(500,i))
                wx.StaticText(self.lpnl, -1,str(row[desc[5][0]]),pos=(700,i))
                i=i+30

    def pcStateSearch(self,e,t1):
        if(t1.GetValue()):
            self.lpnl.Hide()
            self.lpnl=lowerNewPanel(self)
            self.lpnl.Show()

            #self.currentpnl.SetBackgroundColour("pink")
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM powercompany where state=%s",(t1.GetValue(),))
            rows = cur.fetchall()
            desc = cur.description
            i=20
            for row in rows:
                #txt = row[desc[0][0]], row[desc[1][0]], row[desc[2][0]],row[desc[3][0]],row[desc[4][0]]
                wx.StaticText(self.lpnl, -1,row[desc[1][0]],pos=(100,i))
                wx.StaticText(self.lpnl, -1,row[desc[4][0]],pos=(300,i))
                wx.StaticText(self.lpnl, -1,row[desc[2][0]],pos=(500,i))
                wx.StaticText(self.lpnl, -1,str(row[desc[3][0]]),pos=(700,i))
                i=i+30

    def dcStateSearch(self,e,t1):
        if(t1.GetValue()):
            self.lpnl.Hide()
            self.lpnl=lowerNewPanel(self)
            self.lpnl.Show()

            #self.currentpnl.SetBackgroundColour("pink")
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM distributioncompany where state=%s",(t1.GetValue(),))
            rows = cur.fetchall()
            desc = cur.description
            i=20
            for row in rows:
                #txt = row[desc[0][0]], row[desc[1][0]], row[desc[2][0]],row[desc[3][0]],row[desc[4][0]]
                wx.StaticText(self.lpnl, -1,row[desc[1][0]],pos=(100,i))
                wx.StaticText(self.lpnl, -1,row[desc[3][0]],pos=(300,i))
                wx.StaticText(self.lpnl, -1,str(row[desc[2][0]]),pos=(500,i))
                i=i+30

    def tcAll(self,e):
        self.lpnl.Hide()
        self.tcpnl.Hide()
        self.tc(self)


    def pcAll(self,e):
        self.lpnl.Hide()
        self.upnl.Hide()
        self.pc(self)

    def dcAll(self,e):
        self.lpnl.Hide()
        self.dcpnl.Hide()
        self.dc(self)






        #self.ebpnl.Show()

    def back(self,e,p1,p2,title):
    	p1.Hide()
    	p2.Show()
    	self.SetTitle(title)


    def back_tc_pc_dc_eb(self,e,p1,p2,title):
    	p1.Hide()
    	p2.Show()
        self.lpnl.Hide()
    	self.SetTitle(title)


    def pc(self,e):
        self.homepnl.Hide()

    	self.SetTitle("Power Company")
        self.upnl=NewPanel(self)
        self.lpnl=lowerNewPanel(self)
        BackButton = wx.Button(self.upnl, label='Back', pos=(1000, 10),size=(100,40))
        ShowAllButton = wx.Button(self.upnl, label='Show All', pos=(10, 50),size=(100,40))

    	BackButton.Bind(wx.EVT_BUTTON,partial(self.back_tc_pc_dc_eb,p1=self.upnl,p2=self.homepnl,title="Power Distribution System"))
        ShowAllButton.Bind(wx.EVT_BUTTON,self.pcAll)
        t1 = wx.TextCtrl(self.upnl,style= wx.TE_PROCESS_ENTER,pos=(500,20),size=(200,40))
        t1.Bind(wx.EVT_TEXT_ENTER,partial(self.pcStateSearch,t1=t1))
        wx.StaticText(self.upnl, -1,"Name",pos=(100,100))
        wx.StaticText(self.upnl, -1,"State",pos=(300,100))
        wx.StaticText(self.upnl, -1,"Type",pos=(500,100))
        wx.StaticText(self.upnl, -1,"Total power",pos=(700,100))
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM powercompany ")
        rows = cur.fetchall()
        desc = cur.description

        i=20
        for row in rows:
            #txt = row[desc[0][0]], row[desc[1][0]], row[desc[2][0]],row[desc[3][0]],row[desc[4][0]]
            wx.StaticText(self.lpnl, -1,row[desc[1][0]],pos=(100,i))
            wx.StaticText(self.lpnl, -1,row[desc[4][0]],pos=(300,i))
            wx.StaticText(self.lpnl, -1,row[desc[2][0]],pos=(500,i))
            wx.StaticText(self.lpnl, -1,str(row[desc[3][0]]),pos=(700,i))
            i=i+30

    	self.upnl.Show()


    def dc(self,e):
        self.homepnl.Hide()

    	self.SetTitle("Distribution Company")
        self.dcpnl=NewPanel(self)
        self.lpnl=lowerNewPanel(self)
        BackButton = wx.Button(self.dcpnl, label='Back', pos=(1000, 10),size=(100,40))
        ShowAllButton = wx.Button(self.dcpnl, label='Show All', pos=(10, 50),size=(100,40))

    	BackButton.Bind(wx.EVT_BUTTON,partial(self.back_tc_pc_dc_eb,p1=self.dcpnl,p2=self.homepnl,title="Power Distribution System"))
        ShowAllButton.Bind(wx.EVT_BUTTON,self.dcAll)
        t1 = wx.TextCtrl(self.dcpnl,style= wx.TE_PROCESS_ENTER,pos=(500,20),size=(200,40))
        t1.Bind(wx.EVT_TEXT_ENTER,partial(self.dcStateSearch,t1=t1))
        wx.StaticText(self.dcpnl, -1,"Name",pos=(100,100))
        wx.StaticText(self.dcpnl, -1,"State",pos=(300,100))
        wx.StaticText(self.dcpnl, -1,"Tenure(in years)",pos=(500,100))
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM distributioncompany ")
        rows = cur.fetchall()
        desc = cur.description

        i=20
        for row in rows:
            #txt = row[desc[0][0]], row[desc[1][0]], row[desc[2][0]],row[desc[3][0]],row[desc[4][0]]
            wx.StaticText(self.lpnl, -1,row[desc[1][0]],pos=(100,i))
            wx.StaticText(self.lpnl, -1,row[desc[3][0]],pos=(300,i))
            wx.StaticText(self.lpnl, -1,str(row[desc[2][0]]),pos=(500,i))
            i=i+30
    	self.dcpnl.Show()


    def tc(self,e):
        self.homepnl.Hide()

    	self.SetTitle("Transmission Company")
        self.tcpnl=NewPanel(self)
        self.lpnl=lowerNewPanel(self)
        BackButton = wx.Button(self.tcpnl, label='Back', pos=(1000, 10),size=(100,40))
        ShowAllButton = wx.Button(self.tcpnl, label='Show All', pos=(10, 50),size=(100,40))

    	BackButton.Bind(wx.EVT_BUTTON,partial(self.back_tc_pc_dc_eb,p1=self.tcpnl,p2=self.homepnl,title="Power Distribution System"))
        ShowAllButton.Bind(wx.EVT_BUTTON,self.tcAll)
        t1 = wx.TextCtrl(self.tcpnl,style= wx.TE_PROCESS_ENTER,pos=(500,20),size=(200,40))
        t1.Bind(wx.EVT_TEXT_ENTER,partial(self.tcStateSearch,t1=t1))
        wx.StaticText(self.tcpnl, -1,"Name",pos=(100,100))
        wx.StaticText(self.tcpnl, -1,"State",pos=(300,100))
        wx.StaticText(self.tcpnl, -1,"Capacity",pos=(500,100))
        wx.StaticText(self.tcpnl, -1,"Tenure(in years)",pos=(700,100))
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM transmissioncompany ")
        rows = cur.fetchall()
        desc = cur.description
        # print rows[0][desc[1][0]]
        # print rows[0][desc[3][0]]
        # print rows[0][desc[4][0]]
        i=20
        for row in rows:
            #txt = row[desc[0][0]], row[desc[1][0]], row[desc[2][0]],row[desc[3][0]],row[desc[4][0]]
            wx.StaticText(self.lpnl, -1,row[desc[1][0]],pos=(100,i))
            wx.StaticText(self.lpnl, -1,row[desc[4][0]],pos=(300,i))
            wx.StaticText(self.lpnl, -1,str(row[desc[3][0]]),pos=(500,i))
            wx.StaticText(self.lpnl, -1,str(row[desc[5][0]]),pos=(700,i))
            i=i+30
        self.tcpnl.Show()

    def EmpLoginForm(self,e,pt1,pt2,perrormsg):
        self.homepnl.Hide()

    	self.SetTitle("Employee Login")
        self.emplpnl=NewPanel(self)
        errormsg = wx.StaticText(self.emplpnl, -1, " ",pos=(610,140))
        l0 = wx.StaticText(self.emplpnl, -1, "Employee Login ",pos=(600,170),size=(500,500))
        l0.SetFont(wx.Font(16,wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        l1 = wx.StaticText(self.emplpnl, -1, "Employee ID : ",pos=(510,240))
        t1 = wx.TextCtrl(self.emplpnl,style= wx.TE_PROCESS_ENTER,pos=(610,230),size=(200,40))
        l1 = wx.StaticText(self.emplpnl, -1, "Password    : ",pos=(510,290))
        t2 = wx.TextCtrl(self.emplpnl,style = wx.TE_PASSWORD|wx.TE_PROCESS_ENTER,pos=(610,280),size=(200,40))
        t1.Bind(wx.EVT_TEXT_ENTER,partial(self.EmpLogin,t1=t1,t2=t2,errormsg=errormsg))
        t2.Bind(wx.EVT_TEXT_ENTER,partial(self.EmpLogin,t1=t1,t2=t2,errormsg=errormsg))
        loginButton = wx.Button(self.emplpnl, label='Log In', pos=(715, 370))
        loginButton.Bind(wx.EVT_BUTTON, partial(self.EmpLogin,t1=t1,t2=t2,errormsg=errormsg))


        BackButton = wx.Button(self.emplpnl, label='Back', pos=(60, 420),size=(100,40))

    	BackButton.Bind(wx.EVT_BUTTON,partial(self.ElfToMainBack,t1=pt1,t2=pt2,errormsg=perrormsg))
    	self.emplpnl.Show()
        self.emplpnl.Bind(wx.EVT_PAINT, partial(self.OnPaint,op=self.emplpnl))


    def NewconForm(self,e):
        self.ncpnl.Hide()
        self.formpnl=NewPanel(self)
        #self.formpnl.SetBackgroundColour("green")
        l0 = wx.StaticText(self.formpnl, -1, " New Connection Form  ",pos=(450,10),size=(500,500),style=wx.ALIGN_CENTER)
        l0.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.BOLD))

        l1 = wx.StaticText(self.formpnl, -1, " Name of Applicant    :   ",pos=(100,100))
        t11 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,100),size=(200,30))
        l2 = wx.StaticText(self.formpnl, -1, " Father's Name        :   ",pos=(100,150))
        t12 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,150),size=(200,30))
        l3 = wx.StaticText(self.formpnl, -1, " Installation Address :   ",pos=(100,200))
        t13 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,200),size=(200,30))
        l5 = wx.StaticText(self.formpnl, -1, " Mobile No.           :   ",pos=(100,250))
        t14 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,250),size=(200,30))
        l6 = wx.StaticText(self.formpnl, -1, " Email                :   ",pos=(100,300))
        t15 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,300),size=(200,30))
        l7 = wx.StaticText(self.formpnl, -1, " Purpose of Supply    :   ",pos=(100,350))
        #t16 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,350),size=(200,30))
        divList=list()
        divList.append("Domestic")
        divList.append("Commercial")
        divList.append("Industrial")

        self.ps=wx.ComboBox(self.formpnl,pos=(350,350),choices=divList)
        self.ps.Bind(wx.EVT_COMBOBOX, self.posu)
        l8 = wx.StaticText(self.formpnl, -1, " City    :   ",              pos=(100,400))
        t17 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,400),size=(200,30))

        idButton = wx.Button(self.formpnl, label='chose file', pos=(700, 450),size=(100,40))
        idButton.Bind(wx.EVT_BUTTON,self.upload)

        SubmitButton = wx.Button(self.formpnl, label='Submit', pos=(500, 450),size=(100,40))
        SubmitButton.Bind(wx.EVT_BUTTON,partial(self.Submit,t11=t11,t12=t12,t13=t13,t14=t14,t15=t15,t17=t17))

        backButton = wx.Button(self.formpnl, label='Cancel', pos=(1000, 10))
        self.p1=self.formpnl
        self.p2=self.homepnl
        backButton.Bind(wx.EVT_BUTTON, self.Cancel)

    def upload(self,e):
        frame = wx.Frame(None, -1, 'win.py')
        frame.SetDimensions(0,0,200,50)
        dialog=wx.FileDialog(frame, "Open", "", "", "Python files (*.py)|*.py",  wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dialog.ShowModal() == wx.ID_OK:
            print dialog.GetPath()
        

    def posu(self,e):
        self.t16=e.GetString()

    def Submit(self,e,t11,t12,t13,t14,t15,t17):
        if(t11.GetValue() and t12.GetValue() and t13.GetValue() and t14.GetValue() and t15.GetValue() and self.t16 ):
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("select boardname from consumer where state=%s",(self.state,))
            rows=cur.fetchall()
            cur = con.cursor()
            characters = string.ascii_letters + string.digits
            self.reference_id="".join(choice(characters) for x in range(randint(8,10)))

            cur.execute("select max(cid) from consumer")
            c=cur.fetchall()
            cid=c[0][0]

            cur.execute("select max(cid) from newconnection")
            cc=cur.fetchall()
            cidd=cc[0][0]

            if cid>=cidd:
            	ciid=cid+1
            else:
            	ciid=cidd+1

            cur.execute("insert into newconnection values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(t11.GetValue(),t14.GetValue(),rows[0]['boardname'],self.state,self.Subdiv,self.Div,t17.GetValue(),t15.GetValue(),t13.GetValue(),self.reference_id,ciid,))


            status="pending"
            cur.execute("insert into ncstatus values (%s,%s,%s)",(ciid,self.reference_id,status,))
            con.commit()

            #self.p1=self.formpnl
            #self.p2=self.homepnl
            msg='\n Succesfuly Submitted !! Your reference no. is ' + self.reference_id
            wx.MessageBox(message=msg,caption='Info',style=wx.OK | wx.ICON_INFORMATION)
            self.back(self,p1=self.formpnl,p2=self.homepnl,title="Power Distribution System")

        else:
            msg=wx.StaticText(self.formpnl, -1, "Any field can not be empty !!",pos=(w/2,300),size=(300,300))
            msg.SetForegroundColour((255,0,0))

    def Cancel(self,e):
        dial=wx.MessageBox(message='Do you want to cancel it?',caption='Cancel',style=wx.YES_NO | wx.ICON_INFORMATION)
        #self.p1=self.formpnl
        #self.p2=self.homepnl
        if (dial==2):
            #self.back(self)
            self.back_tc_pc_dc_eb(self,p1=self.formpnl,p2=self.homepnl,title="Power Distribution System")
    def UserProfile(self,e,t1):
    	self.custpnl.Hide()

    	self.SetTitle("Profile")
        self.uppnl=NewPanel(self)
        cur.execute("select cid,cname,phone,email,address from consumer where cid=%s",(t1.GetValue(),))
        rows=cur.fetchall()
        l1=wx.StaticText(self.uppnl, -1, rows[0][1]+"'s Profile",pos=(220,10),size=(1000,1000),style=wx.ALIGN_CENTER)
        l1.SetFont(wx.Font(18, wx.MODERN, wx.NORMAL, wx.BOLD))
        l2 = wx.StaticText(self.uppnl, -1, "Consumer ID :   "+str(rows[0][0]),pos=(50,50),size=(1000,1000))
        l3 = wx.StaticText(self.uppnl, -1, "Name        :   "+rows[0][1],     pos=(50,100),size=(1000,1000))
        l4 = wx.StaticText(self.uppnl, -1, "Phone Number:   "+str(rows[0][2]),pos=(50,150),size=(1000,1000))
        l5 = wx.StaticText(self.uppnl, -1, "Email ID    :   "+rows[0][3],     pos=(50,200),size=(1000,1000))
        l6 = wx.StaticText(self.uppnl, -1, "Address     :   "+rows[0][4],     pos=(50,250),size=(1000,1000))
        l2.SetFont(wx.Font(13, wx.MODERN, wx.NORMAL, wx.NORMAL))
        l3.SetFont(wx.Font(13, wx.MODERN, wx.NORMAL, wx.NORMAL))
        l4.SetFont(wx.Font(13, wx.MODERN, wx.NORMAL, wx.NORMAL))
        l5.SetFont(wx.Font(13, wx.MODERN, wx.NORMAL, wx.NORMAL))
        l6.SetFont(wx.Font(13, wx.MODERN, wx.NORMAL, wx.NORMAL))
        BackButton = wx.Button(self.uppnl, label='Back', pos=(60, 420),size=(100,40))
    	#self.p1=self.uppnl
    	#self.p2=self.custpnl
    	BackButton.Bind(wx.EVT_BUTTON,partial(self.back,p1=self.uppnl,p2=self.custpnl,title="User"))
    	#self.uppnl.SetBackgroundColour("blue")
    	self.uppnl.Show()

    def EmpProfile(self,e,t1,t2):
    	self.emppnl.Hide()

    	self.SetTitle("Profile")
        self.epnl=NewPanel(self)
        cur.execute("select * from employee where eid=%s",(t1.GetValue(),))
        rows=cur.fetchall()
        l1=wx.StaticText(self.epnl, -1, rows[0][1]+"'s Profile",pos=(210,20),size=(1000,1000),style=wx.ALIGN_CENTER)
        l1.SetFont(wx.Font(18, wx.MODERN, wx.NORMAL, wx.BOLD))
        l2 = wx.StaticText(self.epnl, -1, "Employee ID       :   "+str(rows[0][0]),      pos=(50,50),size=(1000,1000))
        l3 = wx.StaticText(self.epnl, -1, "Name              :   "+rows[0][1],           pos=(50,100),size=(1000,1000))
        l4 = wx.StaticText(self.epnl, -1, "Departmet         :   "+rows[0][4],           pos=(50,150),size=(1000,1000))
        l5 = wx.StaticText(self.epnl, -1, "Designation       :   "+rows[0][7],           pos=(50,200),size=(1000,1000))
        l6 = wx.StaticText(self.epnl, -1, "Elect. board name :   "+rows[0][6],           pos=(50,250),size=(1000,1000))
        l7 = wx.StaticText(self.epnl, -1, "Date of Jioning   :   "+str(rows[0][2]),      pos=(50,300),size=(1000,1000))
        l8 = wx.StaticText(self.epnl, -1, "Phone no.         :   "+str(rows[0][8]),       pos=(50,350),size=(1000,1000))
        l9 = wx.StaticText(self.epnl, -1, "Date of birth     :   "+str(rows[0][3]),      pos=(50,400),size=(1000,1000))
        l2.SetFont(wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL))
        l3.SetFont(wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL))
        l4.SetFont(wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL))
        l5.SetFont(wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL))
        l6.SetFont(wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL))
        l7.SetFont(wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL))
        l8.SetFont(wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL))
        l9.SetFont(wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL))

        BackButton = wx.Button(self.epnl, label='Back', pos=(1200, 420),size=(100,40))

    	BackButton.Bind(wx.EVT_BUTTON,partial(self.back,p1=self.epnl,p2=self.emppnl,title="Employee"))
    	#self.uppnl.SetBackgroundColour("blue")
    	#self.uppnl.Show()


    def Login(self,e,t1,t2,errormsg):
        if(t1.GetValue()):
            cur.execute("select password from consumer where cid=%s",(t1.GetValue(),))
            rows = cur.fetchall()
            if(len(rows)!=0 and t2.GetValue()==rows[0][0]):
                self.Customer(self,t1=t1,t2=t2,errormsg=errormsg)
            else:
                errormsg.Hide()
                errormsg.Show()
                errormsg.SetForegroundColour((255,0,0))
                errormsg.SetLabel("Wrong Customer ID or Password!!")
        else:
            errormsg.Hide()
            errormsg.Show()
            errormsg.SetForegroundColour((255,0,0))
            errormsg.SetLabel("Wrong Customer ID or Password!!")


    def EmpLogin(self,e,t1,t2,errormsg):
        if(t1.GetValue()):
            cur.execute("select password from employee where eid=%s",(t1.GetValue(),))
            rows = cur.fetchall()
            if(len(rows)!=0 and t2.GetValue()==rows[0][0]):
                cur.execute("select designation from employee where eid=%s",(t1.GetValue(),))
                eboard=cur.fetchall()
                if(eboard[0][0]=='designation6'):
                    self.XXEmployee(self,t1=t1,t2=t2,errormsg=errormsg)
                if(eboard[0][0]=='designation3'):
                    self.designation3(self,t1=t1,t2=t2,errormsg=errormsg)

            else:
                errormsg.SetForegroundColour((255,0,0))
                errormsg.SetLabel("Wrong Employee ID or Password!!")
        else:
            errormsg.SetForegroundColour((255,0,0))
            errormsg.SetLabel("Wrong Employee ID or Password!!")

    def designation3(self,e,t1,t2,errormsg):
        self.emplpnl.Hide()
        self.emppnl=NewPanel(self)

        self.SetTitle("Employee")

        LogoutButton = wx.Button(self.emppnl, label='Logout', pos=(1270, 0),size=(80,30))
        LogoutButton.Bind(wx.EVT_BUTTON,partial(self.EmpLogout,t1=t1,t2=t2,errormsg=errormsg))
        cur.execute("select ename from employee where eid=%s",(t1.GetValue(),))
        rows=cur.fetchall()
        ProfileButton = wx.Button(self.emppnl, label='Hi '+rows[0][0], pos=(1120, 0))
        ProfileButton.Bind(wx.EVT_BUTTON,partial(self.EmpProfile,t1=t1,t2=t2))

        l1=wx.StaticText(self.emppnl, -1,"Distribution Company",pos=(80,30),size=(300,30))
        l1.SetFont(wx.Font(12,wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        l1Add=wx.Button(self.emppnl, label='ADD', pos=(70,80),size=(100,40))
        l1Add.Bind(wx.EVT_BUTTON,self.addDc)
        l1Update=wx.Button(self.emppnl, label='UPDATE', pos=(200,80),size=(100,40))
        l1Delete=wx.Button(self.emppnl, label='DELETE', pos=(330,80),size=(100,40))
        l1Delete.Bind(wx.EVT_BUTTON,self.DelDc)

        l1=wx.StaticText(self.emppnl, -1,"Transmission Company",pos=(80,150),size=(300,30))
        l1.SetFont(wx.Font(12,wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        l2Add=wx.Button(self.emppnl, label='ADD', pos=(70,200),size=(100,40))
        l2Add.Bind(wx.EVT_BUTTON,self.addTc)
        l2Update=wx.Button(self.emppnl, label='UPDATE', pos=(200,200),size=(100,40))
        l2Delete=wx.Button(self.emppnl, label='DELETE', pos=(330,200),size=(100,40))

        l3=wx.StaticText(self.emppnl, -1,"Power Company",pos=(80,270),size=(300,30))
        l3.SetFont(wx.Font(12,wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        l3Add=wx.Button(self.emppnl, label='ADD', pos=(70,320),size=(100,40))
        l3Add.Bind(wx.EVT_BUTTON,self.addPc)
        l3Update=wx.Button(self.emppnl, label='UPDATE', pos=(200,320),size=(100,40))
        l3Delete=wx.Button(self.emppnl, label='DELETE', pos=(330,320),size=(100,40))
    def DelDc(self,e):
        self.emppnl.Hide()
        self.delpnl=NewPanel(self)

        l0 = wx.StaticText(self.delpnl, -1, " Deleting Distriution Company  ",pos=(450,10),size=(500,500),style=wx.ALIGN_CENTER)
        l0.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.BOLD))

        cur=con.cursor(mdb.cursors.DictCursor)
        cur.execute("select * from distributioncompany")
        self.rows=cur.fetchall()
        wx.StaticText(self.delpnl, -1, "Id",pos=(150,50))
        wx.StaticText(self.delpnl, -1, "Name",pos=(300,50))
        wx.StaticText(self.delpnl, -1, "Tenure",pos=(580,50))
        wx.StaticText(self.delpnl, -1, "State",pos=(650,50))
        wx.StaticText(self.delpnl, -1, "T.C. Id",pos=(830,50))
        #self.delpnl.SetupScrolling()
        i=80
        j=0
        for row in self.rows:
            wx.StaticText(self.delpnl, -1,str(row['did']),pos=(150,i))
            wx.StaticText(self.delpnl, -1,row['dname'],pos=(200,i))
            wx.StaticText(self.delpnl, -1,str(row['tenure']),pos=(600,i))
            wx.StaticText(self.delpnl, -1,row['state'],pos=(660,i))
            wx.StaticText(self.delpnl, -1,str(row['tid']),pos=(830,i))
            delButton = wx.Button(self.delpnl, label='DELETE', pos=(880, i),size=(100,20))
            delButton.Bind(wx.EVT_BUTTON,self.delBut,delButton)
            delButton.id=j
            j=j+1
            i=i+30
        backButton = wx.Button(self.delpnl, label='Back', pos=(1000, 10),size = (100,40))

        backButton.Bind(wx.EVT_BUTTON, partial(self.back,p1=self.delpnl,p2=self.emppnl,title="Emplooyee"))

    def delBut(self,e):
        id=e.GetEventObject().id
        deldid=self.rows[id]['did']
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("delete from distributioncompany where did =%s",(deldid,))
        con.commit()
        self.delpnl.Hide()
        self.DelDc(self)

    def addDc(self,e):
        self.emppnl.Hide()
        self.formpnl=NewPanel(self)

        l0 = wx.StaticText(self.formpnl, -1, " Adding New Distriution Company  ",pos=(450,10),size=(500,500),style=wx.ALIGN_CENTER)
        l0.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.BOLD))

        l1 = wx.StaticText(self.formpnl, -1, " Name of D.C. :   ",pos=(100,100))
        t11 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,100),size=(200,30))
        l2 = wx.StaticText(self.formpnl, -1, " Tenure       :   ",pos=(100,150))
        t12 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,150),size=(200,30))
        l3 = wx.StaticText(self.formpnl, -1, " State        :   ",pos=(100,200))
        t13 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,200),size=(200,30))
        l4 = wx.StaticText(self.formpnl, -1, " T.C. Id      :   ",pos=(100,250))
        t14 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,250),size=(200,30))
        SubmitButton = wx.Button(self.formpnl, label='Submit', pos=(500, 450),size=(100,40))
        SubmitButton.Bind(wx.EVT_BUTTON,self.addDcSubmit)

        backButton = wx.Button(self.formpnl, label='Cancel', pos=(630, 450),size = (100,40))
        self.p1=self.formpnl
        self.p2=self.emppnl
        backButton.Bind(wx.EVT_BUTTON, self.addDcCancel)

    def addDcSubmit(self,e):
        if(t11.GetValue() and t12.GetValue() and t13.GetValue() and t14.GetValue()):
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("select did from distributioncompany ")
            rows=cur.fetchall()
            self.newid=rows[-1]['did'] + 1
            cur = con.cursor()
            cur.execute("insert into distributioncompany values (%s,%s,%s,%s,%s)",(self.newid,t11.GetValue(),t12.GetValue(),t13.GetValue(),t14.GetValue()))
            con.commit()

            #self.p1=self.formpnl
            #self.p2=self.emppnl
            wx.MessageBox(message='Succesfuly Submitted',caption='Info',style=wx.OK | wx.ICON_INFORMATION)
            #self.back(self)
            self.back(self,p1=self.formpnl,p2=self.emppnl,title="Employee")
        else:
            msg=wx.StaticText(self.formpnl, -1, "Any field can not be empty !!",pos=(w/2,300),size=(300,300))
            msg.SetForegroundColour((255,0,0))

    def addDcCancel(self,e):
        dial=wx.MessageBox(message='Do you want to cancel it?',caption='Cancel',style=wx.YES_NO | wx.ICON_INFORMATION)
        #self.p1=self.formpnl
        #self.p2=self.emppnl
        if (dial==2):
            #self.back(self)
            self.back(self,p1=self.formpnl,p2=self.emppnl,title="Employee")


    def addTc(self,e):
        self.emppnl.Hide()
        self.formpnl=NewPanel(self)

        l0 = wx.StaticText(self.formpnl, -1, " Adding New Transmission Company  ",pos=(450,10),size=(500,500),style=wx.ALIGN_CENTER)
        l0.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.BOLD))

        l1 = wx.StaticText(self.formpnl, -1, " Name of T.C. :   ",pos=(100,100))
        t11 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,100),size=(200,30))
        l2 = wx.StaticText(self.formpnl, -1, " Tenure       :   ",pos=(100,150))
        t12 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,150),size=(200,30))
        l3 = wx.StaticText(self.formpnl, -1, " State        :   ",pos=(100,200))
        t13 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,200),size=(200,30))
        l4 = wx.StaticText(self.formpnl, -1, " Capacity     :   ",pos=(100,250))
        t14 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,250),size=(200,30))
        l5 = wx.StaticText(self.formpnl, -1, " D.C. Id      :   ",pos=(100,300))
        t15 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,300),size=(200,30))
        l6 = wx.StaticText(self.formpnl, -1, " P.C. Id      :   ",pos=(100,350))
        t16 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,350),size=(200,30))

        SubmitButton = wx.Button(self.formpnl, label='Submit', pos=(500, 450),size=(100,40))
        SubmitButton.Bind(wx.EVT_BUTTON,self.addTcSubmit)

        backButton = wx.Button(self.formpnl, label='Cancel', pos=(630, 450),size = (100,40))
        self.p1=self.formpnl
        self.p2=self.emppnl
        backButton.Bind(wx.EVT_BUTTON, self.addTcCancel)

    def addTcSubmit(self,e):
        if(t11.GetValue() and t12.GetValue() and t13.GetValue() and t14.GetValue()):
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("select tid from transmissioncompany ")
            rows=cur.fetchall()
            self.newid=rows[-1]['tid'] + 1
            cur = con.cursor()
            cur.execute("insert into transmissioncompany values (%s,%s,%s,%s,%s,%s,%s)",(self.newid,t11.GetValue(),t15.GetValue(),t14.GetValue(),t13.GetValue(),t12.GetValue(),t16.GetValue()))
            con.commit()
            #self.p1=self.formpnl
            #self.p2=self.emppnl
            wx.MessageBox(message='Succesfuly Submitted',caption='Info',style=wx.OK | wx.ICON_INFORMATION)
            #self.back(self)
            self.back(self,p1=self.formpnl,p2=self.emppnl,title="Employee")
        else:
            msg=wx.StaticText(self.formpnl, -1, "Any field can not be empty !!",pos=(w/2,300),size=(300,300))
            msg.SetForegroundColour((255,0,0))

    def addTcCancel(self,e):
        dial=wx.MessageBox(message='Do you want to cancel it?',caption='Cancel',style=wx.YES_NO | wx.ICON_INFORMATION)
        #self.p1=self.formpnl
        #self.p2=self.emppnl
        if (dial==2):
            #self.back(self)
            self.back(self,p1=self.formpnl,p2=self.emppnl,title="Employee")
    def addPc(self,e):
        self.emppnl.Hide()
        self.formpnl=NewPanel(self)

        l0 = wx.StaticText(self.formpnl, -1, " Adding New Power Company  ",pos=(450,10),size=(500,500),style=wx.ALIGN_CENTER)
        l0.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.BOLD))

        l1 = wx.StaticText(self.formpnl, -1, " Name of P.C.             :   ",pos=(100,100))
        t11 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,100),size=(200,30))
        l2 = wx.StaticText(self.formpnl, -1, " type                     :   ",pos=(100,150))
        typeList=('Pivate','Government')
        self.cbState=wx.ComboBox(self.formpnl,pos=(350,150),choices=typeList)
        self.cbState.Bind(wx.EVT_COMBOBOX, self.gstr)

        #print t12
        l3 = wx.StaticText(self.formpnl, -1, " Total Power Generation   :   ",pos=(100,200))
        t13 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,200),size=(200,30))
        l4 = wx.StaticText(self.formpnl, -1, " State                    :   ",pos=(100,250))
        t14 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,250),size=(200,30))
        SubmitButton = wx.Button(self.formpnl, label='Submit', pos=(500, 450),size=(100,40))
        SubmitButton.Bind(wx.EVT_BUTTON,self.addPcSubmit)

        backButton = wx.Button(self.formpnl, label='Cancel', pos=(630, 450),size = (100,40))
        self.p1=self.formpnl
        self.p2=self.emppnl
        backButton.Bind(wx.EVT_BUTTON, self.addPcCancel)
    def gstr(self,e):
        t12=e.GetString()

    def addPcSubmit(self,e):
        if(t11.GetValue() and len(t12) and t13.GetValue() and t14.GetValue()):
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("select pid from powercompany ")
            rows=cur.fetchall()
            self.newid=rows[-1]['pid'] + 1
            cur = con.cursor()
            cur.execute("insert into powercompany values (%s,%s,%s,%s,%s)",(self.newid,t11.GetValue(),t12,t13.GetValue(),t14.GetValue()))
            con.commit()

            #self.p1=self.formpnl
            #self.p2=self.emppnl
            wx.MessageBox(message='Succesfuly Submitted',caption='Info',style=wx.OK | wx.ICON_INFORMATION)
            #self.back(self)
            self.back(self,p1=self.formpnl,p2=self.emppnl,title="Employee")
        else:
            msg=wx.StaticText(self.formpnl, -1, "Any field can not be empty !!",pos=(w/2,300),size=(300,300))
            msg.SetForegroundColour((255,0,0))

    def addPcCancel(self,e):
        dial=wx.MessageBox(message='Do you want to cancel it?',caption='Cancel',style=wx.YES_NO | wx.ICON_INFORMATION)
        #self.p1=self.formpnl
        #self.p2=self.emppnl
        if (dial==2):
            #self.back(self)
            self.back(self,p1=self.formpnl,p2=self.emppnl,title="Employee")

    def XXEmployee(self,e,t1,t2,errormsg):
        self.emplpnl.Hide()

        self.SetTitle("Employee")
        self.emppnl=NewPanel(self)

        LogoutButton = wx.Button(self.emppnl, label='Logout', pos=(1270, 20),size=(80,30))
        LogoutButton.Bind(wx.EVT_BUTTON,partial(self.EmpLogout,t1=t1,t2=t2,errormsg=errormsg))
        cur.execute("select ename from employee where eid=%s",(t1.GetValue(),))
        rows=cur.fetchall()
        ProfileButton = wx.Button(self.emppnl, label='Hi '+rows[0][0], pos=(1120, 20))
        ProfileButton.Bind(wx.EVT_BUTTON,partial(self.EmpProfile,t1=t1,t2=t2))

        cur.execute("select * from newconnection where boardname in ( select boardname from employee where eid=%s )",(t1.GetValue(),))
        self.ncrows=cur.fetchall()
        print self.ncrows
        desc = cur.description
        h1=wx.StaticText(self.emppnl, -1,'Applicant Name',    pos=(15,100),size=(130,20))
        h2=wx.StaticText(self.emppnl, -1,'Phone no',          pos=(150,100),size=(95,20))
        h3=wx.StaticText(self.emppnl, -1,'Boardname',         pos=(250,100),size=(345,20))
        h4=wx.StaticText(self.emppnl, -1,'State',             pos=(600,100),size=(125,20))
        h5=wx.StaticText(self.emppnl, -1,'Subdivision',       pos=(730,100),size=(115,20))
        h6=wx.StaticText(self.emppnl, -1,'Division',          pos=(850,100),size=(95,20))
        h7=wx.StaticText(self.emppnl, -1,'City',              pos=(950,100),size=(85,20))
        h8=wx.StaticText(self.emppnl, -1,'Email id',          pos=(1040,100),size=(145,20))
        h9=wx.StaticText(self.emppnl, -1,'Insta.. add',       pos=(1190,100),size=(165,20))
        h1.SetBackgroundColour('dark gray')
        h2.SetBackgroundColour('dark gray')
        h3.SetBackgroundColour('dark gray')
        h4.SetBackgroundColour('dark gray')
        h5.SetBackgroundColour('dark gray')
        h6.SetBackgroundColour('dark gray')
        h7.SetBackgroundColour('dark gray')
        h8.SetBackgroundColour('dark gray')
        h9.SetBackgroundColour('dark gray')
        i=160
        j=0
        k=0
        for r in self.ncrows:
            wx.StaticText(self.emppnl, -1,r[0],pos=(15,i),size=(500,500))
            wx.StaticText(self.emppnl, -1,str(r[1]),pos=(150,i),size=(500,500))
            wx.StaticText(self.emppnl, -1,r[2],pos=(250,i),size=(500,500))
            wx.StaticText(self.emppnl, -1,r[3],pos=(600,i),size=(500,500))
            wx.StaticText(self.emppnl, -1,r[4],pos=(730,i),size=(500,500))
            wx.StaticText(self.emppnl, -1,r[5],pos=(850,i),size=(500,500))
            wx.StaticText(self.emppnl, -1,r[6],pos=(950,i),size=(500,500))
            wx.StaticText(self.emppnl, -1,r[7],pos=(1040,i),size=(500,500))
            wx.StaticText(self.emppnl, -1,r[8],pos=(1190,i),size=(500,500))

            apButton = wx.Button(self.emppnl, label='Aprove', pos=(1090, i+40),size=(80,25))
            apButton.id=j
            apButton.SetBackgroundColour(wx.Colour(115,230,0))
            apButton.Bind(wx.EVT_BUTTON,partial(self.ncAprove,t1=t1,t2=t2,errormsg=errormsg),apButton)
            j=j+1
            rejButton = wx.Button(self.emppnl, label='Reject', pos=(1220, i+40),size=(80,25))
            rejButton.id=j
            rejButton.SetBackgroundColour(wx.Colour(255, 71, 26))
            rejButton.Bind(wx.EVT_BUTTON,partial(self.ncReject,t1=t1,t2=t2,errormsg=errormsg),rejButton)
            i=i+80
            j=j+1
            k=k+1


    def ncAprove(self,e,t1,t2,errormsg):
        print e.GetEventObject().id
        j=0
        k=0
        for i in range(0,len(self.ncrows)):
            if e.GetEventObject().id==2*j :
                cur=con.cursor()
                cur.execute("select max(meterno) from consumer")
                m=cur.fetchall()
                meterno=m[0][0]+1
                cur=con.cursor()
                cur.execute("insert into consumer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.ncrows[k][10],self.ncrows[k][0],self.ncrows[k][1],self.ncrows[k][2],self.ncrows[k][3],self.ncrows[k][4],self.ncrows[k][5],self.ncrows[k][6], meterno,'firoz123',self.ncrows[k][7],self.ncrows[k][8],))
                status="Aproved"
                cur.execute("update ncstatus set status=%s where cid=%s",(status,self.ncrows[k][10]))

                con.commit()
                cur=con.cursor()
                cur.execute("delete from newconnection where cname=%s",(self.ncrows[k][0],))
                con.commit()
                self.emppnl.Hide()
                self.XXEmployee(self,t1=t1,t2=t2,errormsg=errormsg)
                break
            j=j+1
            k=k+1

    def ncReject(self,e,t1,t2,errormsg):
        print e.GetEventObject().id
        j=0
        k=0
        for i in range(0,len(self.ncrows)):
            if e.GetEventObject().id== (2*j+1) :
                cur=con.cursor()
                status="Rejected"
                cur.execute("update ncstatus set status=%s where cid=%s",(status,self.ncrows[k][10]))
                cur.execute("delete from newconnection where cname=%s",(self.ncrows[k][0],))
                con.commit()
                self.emppnl.Hide()
                self.XXEmployee(self,t1=t1,t2=t2,errormsg=errormsg)
                break
            j=j+1
            k=k+1

    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(6))

    def Customer(self,e,t1,t2,errormsg):
        self.homepnl.Hide()

    	self.SetTitle("User")
        self.custpnl=NewPanel(self)

        LogoutButton = wx.Button(self.custpnl, label='Logout', pos=(1270, 20),size=(80,30))
        cur.execute("select cname from consumer where cid=%s",(t1.GetValue(),))
        rows=cur.fetchall()
        ProfileButton = wx.Button(self.custpnl, label='Hi '+rows[0][0], pos=(1120, 20))
    	LogoutButton.Bind(wx.EVT_BUTTON,partial(self.CustLogout,t1=t1,t2=t2,errormsg=errormsg))
        ProfileButton.Bind(wx.EVT_BUTTON,partial(self.UserProfile,t1=t1))

        no_of_meter=cur.execute("select * from consumer where cid=%s",(t1.GetValue(),))
        rows_cust=cur.fetchall()
        for i in range(0,no_of_meter):
            cur.execute("select * from billinginfo where meterno=%s",(rows_cust[i][8],))
            rows_cust_bill=cur.fetchall()
            l0 = wx.StaticText(self.custpnl, -1, str(rows_cust[i][3]),pos=(200,20+i*400),size=(1000,1000),style=wx.ALIGN_CENTER)
            l0.SetFont(wx.Font(20, wx.MODERN, wx.NORMAL, wx.BOLD))
            l1 = wx.StaticText(self.custpnl, -1, "Customer Id :     "+str(rows_cust[i][0]),pos=(100,100+i*400),size=(1000,1000))
            l2 = wx.StaticText(self.custpnl, -1, "Name        :     "+rows_cust[i][1],pos=(100,160+i*400),size=(1000,1000))
            l3 = wx.StaticText(self.custpnl, -1, "Address     :     "+rows_cust[i][11],pos=(100,220+i*400),size=(1000,1000))
            l4 = wx.StaticText(self.custpnl, -1, "Division    :     "+rows_cust[i][6],pos=(100,280+i*400),size=(1000,1000))
            l5 = wx.StaticText(self.custpnl, -1, "SubDivision :     "+rows_cust[i][5],pos=(100,340+i*400),size=(1000,1000))
            l6 = wx.StaticText(self.custpnl, -1, "Meter No.   :     "+str(rows_cust[i][8]),pos=(100,400+i*400),size=(1000,1000))

            l7 = wx.StaticText(self.custpnl, -1, "Bill No.         :     "+str(rows_cust_bill[0][0]),pos=(700,100+i*400),size=(1000,1000))
            l8 = wx.StaticText(self.custpnl, -1, "IssueDate        :     "+str(rows_cust_bill[0][2]),pos=(700,160+i*400),size=(1000,1000))
            l9 = wx.StaticText(self.custpnl, -1, "Previous Reading :     "+str(rows_cust_bill[0][3]),pos=(700,220+i*400),size=(1000,1000))
            l10 = wx.StaticText(self.custpnl, -1, "Current Reading :     "+str(rows_cust_bill[0][5]),pos=(700,280+i*400),size=(1000,1000))
            l11 = wx.StaticText(self.custpnl, -1, "Unit Consumed   :     "+str(rows_cust_bill[0][5]-rows_cust_bill[0][3]),pos=(700,340+i*400),size=(1000,1000))

            l1.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL))
            l2.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL))
            l3.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL))
            l4.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL))
            l5.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL))
            l6.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL))
            l7.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL))
            l8.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL))
            l9.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL))
            l10.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL))
            l11.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL))


    	self.custpnl.Show()

    def CustLogout(self,e,t1,t2,errormsg):
        t1.Clear()
        t2.Clear()
        errormsg.SetLabel(" ")
        #self.p1=self.custpnl
    	#self.p2=self.homepnl
        #self.back(self)
        self.back(self,p1=self.custpnl,p2=self.homepnl,title="Power Distribution System")

    def EmpLogout(self,e,t1,t2,errormsg):
        t1.Clear()
        t2.Clear()
        errormsg.SetLabel(" ")
        #self.panel.Hide()
        #self.p1=self.emppnl
    	#self.p2=self.homepnl
        #self.back(self)
        self.back(self,p1=self.emppnl,p2=self.emplpnl,title="Employee Login")

    def ElfToMainBack(self,e,t1,t2,errormsg):
        t1.Clear()
        t2.Clear()
        errormsg.SetLabel(" ")
        self.back(self,p1=self.emplpnl,p2=self.homepnl,title="Power Distribution System")

    def OnClose(self,e):
        self.Close(True)


def main():

    app = wx.App()
    ex = MainWindow(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
