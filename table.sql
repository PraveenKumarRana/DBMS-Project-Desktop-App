drop database eds;
create database eds;

use eds;


create table employee(eid int primary key,ename varchar(50),doj date,dob date,dept varchar(50),age int,boardname varchar(50),degignation varchar(50),phone int);
create table consumer(cid int primary key,cname varchar(50),phone int,boardname varchar(50),state varchar(50),subdiv varchar(50),divis varchar(50),city varchar(50),meterno int, password varchar(10));
create table distributioncompany(did int primary key,dname varchar(50),tenure int,state varchar(50),tid int);
create table powercompany(pid int primary key,pname varchar(50),type varchar(50),totalpower int,location varchar(50));
create table transmissioncompany(tid int primary key,tname varchar(50),did int,tcapacity int,state varchar(50),tenure int);
create table circle(cname varchar(50),state varchar(50),managerid int,did int);
create table division(divid int primary key,divname varchar(50),headname varchar(50),state varchar(50));
create table subdivision(sdivid int primary key,divid int,headname varchar(50),state varchar(50),sdivname varchar(50));
create table electricityboard(boardname varchar(50) primary key,noofconsumer int,state varchar(50),chairmanid int,powerconsumed int);
create table billinginfo(billid int primary key,cid int,issuedate date,prevreading int,meterno int,curreading int,rate int,type varchar(50),unit int);

insert into consumer values
  (1000,'qwerty',965965,'upbord','up','rajnikhand','lucknow','Luck',454,'Firoz'),
  (2000,'vaibhav',5446335,'jghbo','jb','fver','ranchi','advasi',548,'sp');
