#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import wx
import wx.lib.scrolledpanel as scrolled
import MySQLdb as mdb
con = mdb.connect('localhost', 'admin', 'admin', 'eds')

with con:
    cur=con.cursor()
class HeadNewPanel(wx.Panel):

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent,size=(w,100),pos=(0,0))

class NewPanel(wx.Panel):

    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent,size=(w,h-100),pos=(0,100))
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


        l1 = wx.StaticText(self.homepnl, -1, "Customer ID : ",pos=(510,240))
        self.t1 = wx.TextCtrl(self.homepnl,style= wx.TE_PROCESS_ENTER,pos=(610,230),size=(200,40))
        l1 = wx.StaticText(self.homepnl, -1, "Password    : ",pos=(510,290))
        self.t2 = wx.TextCtrl(self.homepnl,style = wx.TE_PASSWORD|wx.TE_PROCESS_ENTER,pos=(610,280),size=(200,40))
        self.t1.Bind(wx.EVT_TEXT_ENTER,self.Login)
        self.t2.Bind(wx.EVT_TEXT_ENTER,self.Login)
        self.errormsg = wx.StaticText(self.homepnl, -1, " ",pos=(610,340))
        loginButton = wx.Button(self.homepnl, label='Log In', pos=(715, 370))
        loginButton.Bind(wx.EVT_BUTTON, self.Login)
        NacButton = wx.Button(self.homepnl, label='Not a Consumer', pos=(515, 370))
        NacButton.Bind(wx.EVT_BUTTON, self.EmpLoginForm)
        newConButton = wx.Button(self.homepnl, label='Apply New Connection', pos=(1000,20),size=(200,40))
        newConButton.Bind(wx.EVT_BUTTON,self.newConnection)   #220
        #w,h=wx.GetDisplaySize()
        self.SetSize((w,h))
        self.SetMaxSize((w,h))
        self.SetMinSize((w,h))
        self.SetTitle('Power Distribution System')
        self.Centre()

    def newConnection(self,e):
        self.homepnl.Hide()
        self.previousTitle=self.GetTitle()
        self.SetTitle("Application for New Connection")
        self.ncpnl=NewPanel(self)
        self.ncpnl.SetBackgroundColour((232,232,232))
        ebButton = wx.Button(self.ncpnl, label='Back', pos=(1000, 10))
        self.p1=self.ncpnl
        self.p2=self.homepnl
        ebButton.Bind(wx.EVT_BUTTON, self.back)

        l1=wx.StaticText(self.ncpnl, -1, "State/UT :",pos=(w/2-200,50),size=(500,500))
        l2=wx.StaticText(self.ncpnl, -1, "Distribution Company :",pos=(w/2-200,100),size=(500,500))
        l3=wx.StaticText(self.ncpnl, -1, "Division :",pos=(w/2-200,150),size=(500,500))
        l4=wx.StaticText(self.ncpnl, -1, "Sub Division :",pos=(w/2-200,200),size=(500,500))
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
        self.cbState=wx.ComboBox(self.ncpnl,pos=(w/2,50),choices=stateList)
        self.cbState.Bind(wx.EVT_COMBOBOX, self.ncDcSelect)



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
        self.cbDc=wx.ComboBox(self.ncpnl,pos=(w/2,100),choices=dcList)
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
        self.cbDc=wx.ComboBox(self.ncpnl,pos=(w/2,150),choices=divList)
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
        self.cbDc=wx.ComboBox(self.ncpnl,pos=(w/2,200),choices=sdivList)
        self.cbDc.Bind(wx.EVT_COMBOBOX, self.nn)

    def nn(self,e):
        self.Subdiv=e.GetString()
        print self.Subdiv
        submitForm=wx.Button(self.ncpnl, label='Submit', pos=(w/2, 300))
        submitForm.Bind(wx.EVT_BUTTON,self.NewconForm)

    def eb(self,e):
    	self.homepnl.Hide()
    	self.previousTitle=self.GetTitle()
    	self.SetTitle("Electricity Board")
        self.upnl= upperNewPanel(self)
        self.lpnl=lowerNewPanel(self)
        #self.lpnl.SetBackgroundColour("blue")
        ebButton = wx.Button(self.upnl, label='Back', pos=(1000, 10))
        self.p1=self.upnl
        self.p2=self.homepnl
        print "firoz  1"
    	ebButton.Bind(wx.EVT_BUTTON, self.back_tc_pc_dc_eb)
        #l1 = wx.StaticText(self.ebpnl, -1,"hello",pos=(10,10))

        #[select all] buttom
        ebAll = wx.Button(self.upnl, label='Show all', pos=(10, 50))
        ebAll.Bind(wx.EVT_BUTTON, self.ebAll)
        wx.StaticText(self.upnl, -1,"State/UT:",pos=(500,60))
        self.t1 = wx.TextCtrl(self.upnl,style= wx.TE_PROCESS_ENTER,pos=(570,50),size=(200,40))
        self.t1.Bind(wx.EVT_TEXT_ENTER,self.ebStateSearch)
        if(self.t1.GetValue()==""):
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
        self.lpnl.Show()



    def ebAll(self,e):
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
    def ebStateSearch(self,e):
        if(self.t1.GetValue()):
            self.lpnl.Hide()

            self.lpnl=lowerNewPanel(self)

            #lpnl.SetBackgroundColour("grey")
            print "hello"
            self.lpnl.Show()
            print self.t1.GetValue()
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM electricityboard where state=%s",(self.t1.GetValue(),))
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
        if(self.t1.GetValue()==""):
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

    def tcStateSearch(self,e):
        if(self.t1.GetValue()):
            self.lpnl.Hide()
            self.lpnl=lowerNewPanel(self)
            self.lpnl.Show()

            #self.currentpnl.SetBackgroundColour("pink")
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM transmissioncompany where state=%s",(self.t1.GetValue(),))
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

    def pcStateSearch(self,e):
        if(self.t1.GetValue()):
            self.lpnl.Hide()
            self.lpnl=lowerNewPanel(self)
            self.lpnl.Show()

            #self.currentpnl.SetBackgroundColour("pink")
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM powercompany where state=%s",(self.t1.GetValue(),))
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

    def dcStateSearch(self,e):
        if(self.t1.GetValue()):
            self.lpnl.Hide()
            self.lpnl=lowerNewPanel(self)
            self.lpnl.Show()

            #self.currentpnl.SetBackgroundColour("pink")
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM distributioncompany where state=%s",(self.t1.GetValue(),))
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

    def back(self,e):
    	self.p1.Hide()
    	self.p2.Show()
    	self.SetTitle(self.previousTitle)


    def back_tc_pc_dc_eb(self,e):
    	self.p1.Hide()
    	self.p2.Show()
        self.lpnl.Hide()
    	self.SetTitle(self.previousTitle)


    def pc(self,e):
        self.homepnl.Hide()
        self.previousTitle=self.GetTitle()
    	self.SetTitle("Power Company")
        self.upnl=NewPanel(self)
        self.lpnl=lowerNewPanel(self)
        BackButton = wx.Button(self.upnl, label='Back', pos=(1000, 10),size=(100,40))
        ShowAllButton = wx.Button(self.upnl, label='Show All', pos=(10, 50),size=(100,40))

    	self.p1=self.upnl
    	self.p2=self.homepnl
    	BackButton.Bind(wx.EVT_BUTTON,self.back_tc_pc_dc_eb)
        ShowAllButton.Bind(wx.EVT_BUTTON,self.pcAll)
        self.t1 = wx.TextCtrl(self.upnl,style= wx.TE_PROCESS_ENTER,pos=(500,20),size=(200,40))
        self.t1.Bind(wx.EVT_TEXT_ENTER,self.pcStateSearch)
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
        self.previousTitle=self.GetTitle()
    	self.SetTitle("Distribution Company")
        self.dcpnl=NewPanel(self)
        self.lpnl=lowerNewPanel(self)
        BackButton = wx.Button(self.dcpnl, label='Back', pos=(1000, 10),size=(100,40))
        ShowAllButton = wx.Button(self.dcpnl, label='Show All', pos=(10, 50),size=(100,40))

        self.p1=self.dcpnl
    	self.p2=self.homepnl
    	BackButton.Bind(wx.EVT_BUTTON,self.back_tc_pc_dc_eb)
        ShowAllButton.Bind(wx.EVT_BUTTON,self.dcAll)
        self.t1 = wx.TextCtrl(self.dcpnl,style= wx.TE_PROCESS_ENTER,pos=(500,20),size=(200,40))
        self.t1.Bind(wx.EVT_TEXT_ENTER,self.dcStateSearch)
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
        self.previousTitle=self.GetTitle()
    	self.SetTitle("Transmission Company")
        self.tcpnl=NewPanel(self)
        self.lpnl=lowerNewPanel(self)
        BackButton = wx.Button(self.tcpnl, label='Back', pos=(1000, 10),size=(100,40))
        ShowAllButton = wx.Button(self.tcpnl, label='Show All', pos=(10, 50),size=(100,40))
        self.p1=self.tcpnl
    	self.p2=self.homepnl
    	BackButton.Bind(wx.EVT_BUTTON,self.back_tc_pc_dc_eb)
        ShowAllButton.Bind(wx.EVT_BUTTON,self.tcAll)
        self.t1 = wx.TextCtrl(self.tcpnl,style= wx.TE_PROCESS_ENTER,pos=(500,20),size=(200,40))
        self.t1.Bind(wx.EVT_TEXT_ENTER,self.tcStateSearch)
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

    def NewconForm(self,e):
        self.ncpnl.Hide()
        self.formpnl=NewPanel(self)
        #self.formpnl.SetBackgroundColour("green")
        l0 = wx.StaticText(self.formpnl, -1, " New Connection Form  ",pos=(450,10),size=(500,500),style=wx.ALIGN_CENTER)
        l0.SetFont(wx.Font(15, wx.MODERN, wx.NORMAL, wx.BOLD))

        l1 = wx.StaticText(self.formpnl, -1, " Name of Applicant    :   ",pos=(100,100))
        self.t11 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,100),size=(200,30))
        l2 = wx.StaticText(self.formpnl, -1, " Father's Name        :   ",pos=(100,150))
        self.t12 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,150),size=(200,30))
        l3 = wx.StaticText(self.formpnl, -1, " Installation Address :   ",pos=(100,200))
        self.t13 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,200),size=(200,30))
        l5 = wx.StaticText(self.formpnl, -1, " Mobile No.           :   ",pos=(100,250))
        self.t14 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,250),size=(200,30))
        l6 = wx.StaticText(self.formpnl, -1, " Email                :   ",pos=(100,300))
        self.t15 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,300),size=(200,30))
        l7 = wx.StaticText(self.formpnl, -1, " Purpose of Supply    :   ",pos=(100,350))
        self.t16 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,350),size=(200,30))
        l8 = wx.StaticText(self.formpnl, -1, " City    :   ",              pos=(100,400))
        self.t17 = wx.TextCtrl(self.formpnl,style= wx.TE_PROCESS_ENTER,    pos=(350,400),size=(200,30))

        SubmitButton = wx.Button(self.formpnl, label='Submit', pos=(500, 450),size=(100,40))
        SubmitButton.Bind(wx.EVT_BUTTON,self.Submit)

        backButton = wx.Button(self.formpnl, label='Cancel', pos=(1000, 10))
        self.p1=self.formpnl
        self.p2=self.homepnl
        backButton.Bind(wx.EVT_BUTTON, self.Cancel)

    def Submit(self,e):
        if(self.t11.GetValue() and self.t12.GetValue() and self.t13.GetValue() and self.t14.GetValue() and self.t15.GetValue() and self.t16.GetValue() ):
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("select boardname from consumer where state=%s",(self.state,))
            rows=cur.fetchall()
            cur = con.cursor()
            cur.execute("insert into newconnection values (%s,%s,%s,%s,%s,%s,%s,%s)",(self.t11.GetValue(),self.t14.GetValue(),rows[0]['boardname'],self.state,self.Subdiv,self.Div,self.t17.GetValue(),self.t15.GetValue(),))
            con.commit()
            self.p1=self.formpnl
            self.p2=self.homepnl
            wx.MessageBox(message='Succesfuly Submitted',caption='Info',style=wx.OK | wx.ICON_INFORMATION)
            self.back(self)
        else:
            msg=wx.StaticText(self.formpnl, -1, "Any field can not be empty !!",pos=(w/2,300),size=(300,300))
            msg.SetForegroundColour((255,0,0))
    def Cancel(self,e):
        dial=wx.MessageBox(message='Do you want to cancel it?',caption='Cancel',style=wx.YES_NO | wx.ICON_INFORMATION)
        self.p1=self.formpnl
        self.p2=self.homepnl
        if (dial==2):
            self.back(self)
    def UserProfile(self,e):
    	self.custpnl.Hide()
        self.previousTitle=self.GetTitle()
    	self.SetTitle("Profile")
        self.uppnl=NewPanel(self)
        cur.execute("select cid,cname,phone,email,address from consumer where cid=%s",(self.t1.GetValue(),))
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
    	self.p1=self.uppnl
    	self.p2=self.custpnl
    	BackButton.Bind(wx.EVT_BUTTON,self.back)
    	#self.uppnl.SetBackgroundColour("blue")
    	self.uppnl.Show()

    def EmpProfile(self,e):
    	self.emppnl.Hide()
        self.previousTitle=self.GetTitle()
    	self.SetTitle("Profile")
        self.epnl=NewPanel(self)
        cur.execute("select * from employee where eid=%s",(self.t1.GetValue(),))
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
    	self.p1=self.epnl
    	self.p2=self.emppnl
    	BackButton.Bind(wx.EVT_BUTTON,self.back)
    	#self.uppnl.SetBackgroundColour("blue")
    	#self.uppnl.Show()


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
                cur.execute("select designation from employee where eid=%s",(self.t1.GetValue(),))
                eboard=cur.fetchall()
                if(eboard[0][0]=='designation6'):
                    self.XXEmployee(self)
            else:
                self.errormsg.SetForegroundColour((255,0,0))
                self.errormsg.SetLabel("Wrong Employee ID or Password!!")
        else:
            self.errormsg.SetForegroundColour((255,0,0))
            self.errormsg.SetLabel("Wrong Employee ID or Password!!")

    def XXEmployee(self,e):
        self.emplpnl.Hide()
        self.previousTitle=self.GetTitle()
        self.SetTitle("Employee")





        """self.panel =NewPanel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.listbox = wx.ListBox(self.panel)
        hbox.Add(self.listbox, wx.ID_ANY, wx.EXPAND | wx.ALL, 80)

        self.btnPanel = wx.Panel(self.panel)
        vbox = wx.BoxSizer(wx.VERTICAL)

        LogoutButton = wx.Button(self.btnPanel, wx.ID_ANY, 'Logout', size=(90, 40))
        LogoutButton.Bind(wx.EVT_BUTTON,self.EmpLogout)
        cur.execute("select ename from employee where eid=%s",(self.t1.GetValue(),))
        rows=cur.fetchall()
        ProfileButton = wx.Button(self.btnPanel, label='Hi '+rows[0][0])
        ProfileButton.Bind(wx.EVT_BUTTON,self.EmpProfile)


        delBtn = wx.Button(self.btnPanel, wx.ID_ANY, 'Delete', size=(90, 40))
        clrBtn = wx.Button(self.btnPanel, wx.ID_ANY, 'Clear', size=(90, 40))

        #self.Bind(wx.EVT_BUTTON, self.NewItem, id=newBtn.GetId())

        #self.Bind(wx.EVT_BUTTON, self.NewItem, id=newBtn.GetId())
        #self.Bind(wx.EVT_BUTTON, self.OnRename, id=renBtn.GetId())
        #self.Bind(wx.EVT_BUTTON, self.OnDelete, id=delBtn.GetId())
        #self.Bind(wx.EVT_BUTTON, self.OnClear, id=clrBtn.GetId())
        #self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnRename)

        #vbox.Add((-1, 20))
        vbox.Add(LogoutButton)
        vbox.Add(ProfileButton, 0, wx.TOP, 5)
        vbox.Add(delBtn, 0, wx.TOP, 5)
        vbox.Add(clrBtn, 0, wx.TOP, 5)

        self.btnPanel.SetSizer(vbox)
        hbox.Add(self.btnPanel, 0.4, wx.EXPAND | wx.RIGHT, 20)
        self.panel.SetSizer(hbox)

        #self.SetTitle('wx.ListBox')
        #self.Centre()

    def NewItem(self, event):

        text = wx.GetTextFromUser('Enter a new item', 'Insert dialog')
        if text != '':
            self.listbox.Append(text)"""




        self.emppnl=NewPanel(self)

        LogoutButton = wx.Button(self.emppnl, label='Logout', pos=(1270, 0),size=(80,30))
        LogoutButton.Bind(wx.EVT_BUTTON,self.EmpLogout)
        cur.execute("select ename from employee where eid=%s",(self.t1.GetValue(),))
        rows=cur.fetchall()
        ProfileButton = wx.Button(self.emppnl, label='Hi '+rows[0][0], pos=(1120, 0))
        ProfileButton.Bind(wx.EVT_BUTTON,self.EmpProfile)

        cur.execute("select * from newconnection where boardname in ( select boardname from employee where eid=%s )",(self.t1.GetValue(),))
        ncrows=cur.fetchall()
        print ncrows
        desc = cur.description
        wx.StaticText(self.emppnl, -1,'Applicant Name',     pos=(10,100),size=(500,500))
        wx.StaticText(self.emppnl, -1,'Phone no',          pos=(150,100),size=(500,500))
        wx.StaticText(self.emppnl, -1,'Boardname',         pos=(250,100),size=(500,500))
        wx.StaticText(self.emppnl, -1,'State',             pos=(600,100),size=(500,500))
        wx.StaticText(self.emppnl, -1,'Subdivision',       pos=(700,100),size=(500,500))
        wx.StaticText(self.emppnl, -1,'Division',          pos=(800,100),size=(500,500))
        wx.StaticText(self.emppnl, -1,'City',              pos=(900,100),size=(500,500))
        wx.StaticText(self.emppnl, -1,'Email id',          pos=(1000,100),size=(500,500))
        i=160
        j=1
        for r in ncrows:
            wx.StaticText(self.emppnl, -1,r[0],pos=(10,i),size=(500,500))
            wx.StaticText(self.emppnl, -1,str(r[1]),pos=(150,i),size=(500,500))
            wx.StaticText(self.emppnl, -1,r[2],pos=(250,i),size=(500,500))
            wx.StaticText(self.emppnl, -1,r[3],pos=(600,i),size=(500,500))
            wx.StaticText(self.emppnl, -1,r[4],pos=(700,i),size=(500,500))
            wx.StaticText(self.emppnl, -1,r[5],pos=(800,i),size=(500,500))
            wx.StaticText(self.emppnl, -1,r[6],pos=(900,i),size=(500,500))
            wx.StaticText(self.emppnl, -1,r[7],pos=(1000,i),size=(500,500))

            self.apButton = wx.Button(self.emppnl,id=j, label='Aprove', pos=(1160, i),size=(80,25))
            self.apButton.SetBackgroundColour(wx.Colour(115,230,0))
            self.apButton.Bind(wx.EVT_BUTTON,self.ncAprove,id=self.apButton.GetId())

            rejButton = wx.Button(self.emppnl,id=j, label='Reject', pos=(1270, i),size=(80,25))
            rejButton.SetBackgroundColour(wx.Colour(255, 71, 26))
            #rejButton.Bind(wx.EVT_BUTTON,self.ncAprove,id=apButton.GetId())
            #RejectButton.Bind(wx.EVT_BUTTON,self.ncDisaprove)
            i=i+40
            j=j+1
        #print AproveButton

    def ncAprove(self,e):
        print self.apButton.GetId()
        #cur.execute("select ")


    def Customer(self,e):
        self.homepnl.Hide()
        self.previousTitle=self.GetTitle()
    	self.SetTitle("User")
        self.custpnl=NewPanel(self)

        LogoutButton = wx.Button(self.custpnl, label='Logout', pos=(1270, 0),size=(80,30))
        cur.execute("select cname from consumer where cid=%s",(self.t1.GetValue(),))
        rows=cur.fetchall()
        ProfileButton = wx.Button(self.custpnl, label='Hi '+rows[0][0], pos=(1120, 0))
    	LogoutButton.Bind(wx.EVT_BUTTON,self.CustLogout)
        ProfileButton.Bind(wx.EVT_BUTTON,self.UserProfile)

        no_of_meter=cur.execute("select * from consumer where cid=%s",(self.t1.GetValue(),))
        rows_cust=cur.fetchall()
        for i in range(0,no_of_meter):
            cur.execute("select * from billinginfo where meterno=%s",(rows_cust[i][8],))
            rows_cust_bill=cur.fetchall()
            l0 = wx.StaticText(self.custpnl, -1, str(rows_cust[i][3]),pos=(200,0+i*400),size=(1000,1000),style=wx.ALIGN_CENTER)
            l0.SetFont(wx.Font(23, wx.MODERN, wx.NORMAL, wx.BOLD))
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

    def CustLogout(self,e):
        self.t1.Clear()
        self.t2.Clear()
        self.errormsg.SetLabel(" ")
        self.p1=self.custpnl
    	self.p2=self.homepnl
        self.back(self)

    def EmpLogout(self,e):
        self.t1.Clear()
        self.t2.Clear()
        self.errormsg.SetLabel(" ")
        #self.panel.Hide()
        self.p1=self.emppnl
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
