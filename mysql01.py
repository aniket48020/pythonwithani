CREATE TABLE app (VCODE varchar(30), VEHICLETYPE varchar(30), PERKM numeric(5));
insert into app values("VO1","VOLVO BUS",150);
insert into app values("VO2","AC DELUXE BUS",150);
insert into app values("VO1","ORDINARY BUS",150);
insert into app values("VO1","SUV",150);
insert into app values("VO1","CAR",150);
create TABLE travel(CNO numeric(3), CNAME varchar(30), TRAVELDATE date, KM numeric, VCODE varchar(30), NOP numeric(3));
insert into travel values(101,"K.Niwal",'2015-12-13',200,"V01",32);
insert into travel values(103,"Fredrick Sym",'2016-03-21',120,"V03",45);
insert into travel values(105,"Hitesh Jain",'2016-04-23',450,"V02",42);
insert into travel values(102,"Ravi Anish",'2016-01-13',80,"V02",40);
insert into travel values(107,"John Malina",'2015-02-10',65,"V04",2);
insert into travel values(104,"Sahanubhuti",'2016-01-28',90,"V05",4);
insert into travel values(106,"Ramesh Jaya",'2016-04-06',100,"V01",25);
SELECT CNO,CNAME,TRAVELDATE FROM travel order by CNO desc;
SELECT CNAME from travel where VCODE="V01" OR VCODE="V02";
SELECT CNAME,CNO FROM travel where TRAVELDATE between '2015-05-01' AND '2015-12-31';
SELECT CNO,CNAME,TRAVELDATE,KM,VCODE,NOP FROM travel  where KM>120 order by NOP asc;
SELECT COUNT(*),VCODE FROM travel GROUP BY VCODE HAVING COUNT(*)>1;
SELECT DISTINCT VCODE FROM travel;
SELECT A.VCODE,CNAME,VEHICLETYPE FROM travel A,app B WHERE A.VCODE=B.VCODE AND KM<90;
SELECT CNAME,KM*PERKM FROM travel A, app B WHERE A.VCODE=B.VCODE AND A.VCODE="V05";


