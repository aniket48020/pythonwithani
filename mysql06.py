create table items(code numeric(5),Iname varchar(30),Qty numeric(5),price numeric(10),company varchar(20),Tcode varchar(5));
insert into items values(1001,"Digital pad 12i",121,11000,"Xenita","T01");
insert into items values(1006,"LED screen 40",70,38000,"santora","T02");
insert into items values(1004,"Car gps system",50,21500,"Geoknow","T01");
insert into items values(1003,"Digital camera 12x",160,8000,"Digiclick","T02");
insert into items values(1005,"Pen drive 32 Gb",600,1200,"Storehome","T03");
create table traders(Tcode varchar(10),Tname varchar(30),City varchar(10));
insert into traders values("T01","Electronic Sales","Mumbai");
insert into traders values("T03","Busy Store Corp","Delhi");
insert into traders values("T02","Disp House Inc","Chennai");
select * from items order by Iname asc;
select Iname,price from items where price>=10000 and price<=22000;
select Tcode,COUNT(Tcode) from items GROUP BY Tcode;
select price,Iname,Qty from items where(Qty>150);
select Iname,company from items order by company desc;

