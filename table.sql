use eds;

drop table employee;
create table employee(eid int primary key,ename varchar(50),doj date,dob date,dept varchar(50),age int,boardname varchar(50),designation varchar(50),phone int,password varchar(50));
drop table consumer;
create table consumer(cid int,cname varchar(50),phone int,boardname varchar(50),state varchar(50),subdiv varchar(50),divis varchar(50),city varchar(50),meterno int primary key,password varchar(50),email varchar(50),address varchar(50));
drop table distributioncompany;
create table distributioncompany(did int primary key,dname varchar(50),tenure int,state varchar(50),tid int);
	drop table powercompany;
create table powercompany(pid int primary key,pname varchar(50),type varchar(50),totalpower int,state varchar(50));
	drop table transmissioncompany;
create table transmissioncompany(tid int primary key,tname varchar(50),did int,tcapacity int,state varchar(50),tenure int);
	drop table circles;
create table circles(cname varchar(50),state varchar(50),managerid int,did int);
	drop table division;
create table division(divid int primary key,divname varchar(50),headname varchar(50),state varchar(50), did int);
	drop table subdivision;
create table subdivision(sdivid int primary key,divid int,headname varchar(50),state varchar(50),sdivname varchar(50));
	drop table electricityboard;
create table electricityboard(boardname varchar(50) primary key,noofconsumer int,state varchar(50),chairmanid int,powerconsumed int);
	drop table billinginfo;
create table billinginfo(billid int primary key,cid int,issuedate date,prevreading int,meterno int,curreading int,rate int,type varchar(50),unit int);

insert into employee values
	(7001,	'Amar kumar',		'2012-08-11',	'2000-11-06',	'dept',	18,	'boardname',	'designation',	844667,	'password'),
	(7002,	'firoz mohammad',	'2010-10-08',	'1999-12-06',	'dept',	19,	'boardname',	'designation',	129748,	'password'),
	(7003,	'saumya prakash',	'2013-12-03',	'1998-06-10',	'dept',	21,	'boardname',	'designation',	729733,	'password'),
	(7004,	'vaibhav singhal',	'2015-09-07',	'1999-03-23',	'dept',	20,	'boardname',	'designation',	264856,	'password'),
	(7005,	'Praveen Rana',		'2012-03-05',	'1998-12-12',	'dept',	20,	'boardname',	'designation',	197835,	'password');

insert into consumer values
	(8001,	'John',		254789,	'boardname1',	'Delhi',			'subdiv1',	'divis',	'delhi-NCR',	101,	'password',	'john@gmail.com',		'GT road noida'		),
	(8002,	'Andrew',	961315,	'boardname2',	'Assam',			'subdiv2',	'divis',	'dispur',	102,	'password',	'Andrew@gmail.com',		'Ak sahaylane dispur'	),
	(8003,	'Peterson',	487964,	'boardname3',	'Gujarat',			'subdiv3',	'divis',	'surat',	103,	'password',	'Peterson@gmail.com',		'ps road surat'		),
	(8004,	'David',	479368,	'boardname4',	'Andhra Pradesh',	'subdiv4',	'divis',	'hyderabad',	104,	'password',	'David@gmail.com',		'sn colony hyderabad'	),
	(8005,	'Michael',	169893,	'boardname5',	'Haryana',			'subdiv5',	'divis',	'chandigarh',	105,	'password',	'Michael@gmail.com',		'pk colony chandigarh'	);


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
	('cname1',	'Delhi',			201,	2001),
	('cname2',	'Gujarat',			202,	2002),
	('cname3',	'Assam',			203,	2003),
	('cname4',	'Andhra Pradesh',		204,	2004),
	('cname5',	'Haryana',			205,	2005);
insert into division values
	(5001,	'divname1',	'Akshay',	'Haryana', 2001),
	(5002,	'divname2',	'Ranjan',	'Assam',2002),
	(5003,	'divname3',	'Manish',	'Delhi',2003),
	(5004,	'divname4',	'Prateek',	'Andhra Pradesh',2003),
	(5005,	'divname5',	'Anurag',	'Gujarat',2001);

insert into subdivision values
	(6001,	5001,	'Akshay',	'Haryana',			'sdivname1'),
	(6002,	5003,	'Ranjan',	'Delhi',			'sdivname2'),
	(6003,	5003,	'Manish',	'Delhi',			'sdivname3'),
	(6004,	5003,	'Prateek',	'Delhi',	'sdivname4'),
	(6005,	5005,	'Anurag',	'Gujarat',			'sdivname5');
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
	(10005,	8005,	'2019-01-06',	120,	105,	200,	15,	'type',	4),
	(10006,8001,'2017-12-20',165,106,180,12,'type',2);
