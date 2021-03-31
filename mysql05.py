create table SCHOOL(CODE numeric(10),TEACHERNAME varchar(30),SUBJECT varchar(30),DOJ date, PERIODS numeric(10),EXPERIENCE numeric(10));
insert into SCHOOL values(1001,"Ravi Shankar","English",'2000/3/12',24,10);
insert into SCHOOL values(1009,"Priya Rai","Physics",'1998/09/03',26,12);
insert into SCHOOL values(1203,"Lisa Anand","English",'2000/04/09',27,5);
insert into SCHOOL values(1045,"Yashraj","Math",'2000/08/24',24,15);
insert into SCHOOL values(1123,"Ganan","Physics",'1999/07/16',28,3);
insert into SCHOOL values(1167,"Harish B","Chemistry",'1999/10/19',27,5);
insert into SCHOOL values(1215,"Umesh","Physics",'1998/05/11',22,16);
create table Admin(Code numeric(10),Gender varchar(20),Designation varchar(30));
insert into Admin values(1001,"Male","Vice Principal");
insert into Admin values(1009,"Female","Co-ordinator");
insert into Admin values(1203,"Female","Co-ordinator");
insert into Admin values(1045,"Male","HOD");
insert into Admin values(1123,"Male","Senior Teacher");
insert into Admin values(1167,"Male","Senior Teacher");
insert into Admin values(1215,"Male","HOD");
SELECT TEACHERNAME,PERIODS from SCHOOL where PERIODS>25;
Select * from SCHOOL order by EXPERIENCE desc;
select DISTINCT  Designation from Admin;

