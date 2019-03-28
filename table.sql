drop database eds;
create database eds;

use eds;


create table employee(eid int primary key,ename varchar(50),doj date,dob date,dept varchar(50),age int,boardname varchar(50),designation varchar(50),phone int);
create table consumer(cid int primary key,cname varchar(50),phone int,boardname varchar(50),state varchar(50),subdiv varchar(50),divis varchar(50),city varchar(50),meterno int,password varchar(50));
create table distributioncompany(did int primary key,dname varchar(50),tenure int,state varchar(50),tid int);
create table powercompany(pid int primary key,pname varchar(50),type varchar(50),totalpower int,state varchar(50));
create table transmissioncompany(tid int primary key,tname varchar(50),did int,tcapacity int,state varchar(50),tenure int);
create table circles(cname varchar(50),state varchar(50),managerid int,did int);
create table division(divid int primary key,divname varchar(50),headname varchar(50),state varchar(50));
create table subdivision(sdivid int primary key,divid int,headname varchar(50),state varchar(50),sdivname varchar(50));
create table electricityboard(boardname varchar(50) primary key,noofconsumer int,state varchar(50),chairmanid int,powerconsumed int);
create table billinginfo(billid int primary key,cid int,issuedate date,prevreading int,meterno int,curreading int,rate int,type varchar(50),unit int);

insert into employee values
	(7001,	'Amar kumar',		'2012-08-11',	'2000-11-06',	'dept',	18,	'boardname',	'designation',	844667),
	(7002,	'firoz mohammad',	'2010-10-08',	'1999-12-06',	'dept',	19,	'boardname',	'designation',	129748),
	(7003,	'saumya prakash',	'2013-12-03',	'1998-06-10',	'dept',	21,	'boardname',	'designation',	729733),
	(7004,	'vaibhav singhal',	'2015-19-07',	'1999-03-23',	'dept',	20,	'boardname',	'designation',	264856),
	(7005,	'Praveen Rana',		'2012-03-05',	'1998-12-12',	'dept',	20,	'boardname',	'designation',	197835);
	
insert into consumer values
	(8001,	'John',		254789,	'boardname',	'Delhi',			'subdiv',	'divis',	'delhi-NCR',	101,	'password'),
	(8002,	'Andrew',	961315,	'boardname',	'Assam',			'subdiv',	'divis',	'dispur',		102,	'password'),
	(8003,	'Peterson',	487964,	'boardname',	'Gujarat',			'subdiv',	'divis',	'surat',		103,	'password'),
	(8004,	'David',	479368,	'boardname',	'Andhra Pradesh',	'subdiv',	'divis',	'hyderabad',	104,	'password'),
	(8005,	'Michael',	169893,	'boardname',	'Haryana',			'subdiv',	'divis',	'chandigarh',	105,	'password');
insert into distributioncompany values
	(2001,	'APEPDCL',	5,	'Andhra Pradesh',	4001),
	(2002,	'LAEDCL',	8,	'Assam',			4002),
	(2003,	'NDPL',		3,	'Delhi',			4003),
	(2004,	'MGVCL',	6,	'Gujarat',			4004),
	(2005,	'DHBVNL',	9,	'Haryana',			4005);
insert into powercompany values
	(3001,	'APGenco',	'type',	15789,	'Andhra Pradesh'),
	(3002,	'APGCL',	'type',	45632,	'Assam'),
	(3003,	'IPGCL',	'type',	89542,	'Delhi'),
	(3004,	'GSECL',	'type',	26654,	'Gujarat'),
	(3005,	'GPGCL',	'type',	47943,	'Haryana');
insert into transmissioncompany values
	(4001,	'APTransco',	2001,	500,	'Andhra Pradesh',	5),
	(4002,	'AEGCL SLDC',	2002,	700,	'Assam',			8),
	(4003,	'SLDC Delhi',	2003,	300,	'Delhi',			3),
	(4004,	'GETCO',		2004,	800,	'Gujarat',			6),
	(4005,	'HVPNL',		2005,	400,	'Haryana',			9);
insert into circles values
	('cname',	'Delhi',			201,	2001),
	('cname',	'Gujarat',			202,	2002),
	('cname',	'Assam',			203,	2003),
	('cname',	'Andhra Pradesh',	204,	2004),
	('cname',	'Haryana',			205,	2005);
insert into division values
	(5001,	'divname',	'Akshay',	'Delhi'),
	(5002,	'divname',	'Ranjan',	'Assam'),
	(5003,	'divname',	'Manish',	'Haryana'),
	(5004,	'divname',	'Prateek',	'Andhra Pradesh'),
	(5005,	'divname',	'Anurag',	'Gujarat');
insert into subdivision values
	(6001,	5001,	'Akshay',	'Delhi',			'sdivname'),
	(6002,	5002,	'Ranjan',	'Assam',			'sdivname'),
	(6003,	5003,	'Manish',	'Haryana',			'sdivname'),
	(6004,	5004,	'Prateek',	'Andhra Pradesh',	'sdivname'),
	(6005,	5005,	'Anurag',	'Gujarat',			'sdivname');
insert into electricityboard values
	('ASEC',	250000,	'Assam',		301,	2500),
	('DVB',		400000,	'Delhi',		302,	3200),	
	('GUVN',	610000,	'Gujarat',		303,	4000),
	('HPGC',	120000,	'Haryana',		304,	1600),
	('JSEB',	320000,	'Jharkhand',	305,	5600);
insert into billinginfo values
	(10001,	8001,	'2017-12-20',	165,	101,	180,	12,	'type',	2),
	(10002,	8002,	'2018-06-15',	200,	102,	250,	16,	'type',	6),
	(10003,	8003,	'2018-10-30',	240,	103,	260,	18,	'type',	5),
	(10004,	8004,	'2017-11-01',	350,	104,	370,	26,	'type',	9),
	(10005,	8005,	'2019-01-06',	120,	105,	200,	15,	'type',	4);
