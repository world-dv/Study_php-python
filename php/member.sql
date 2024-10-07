create table member (
	num int not null auto_increment,
	id char(20) not null,
	name char(20) not null,
	gender char(1),
	post_num char(8),
	address char(80),
	tel char(20),
	age int,
	primary key(num)
);

insert into member (id, name, gender, post_num, address, tel, age) value ('ga', '가', 'M', '100-011', '서울시 중구 충무로 1가', '234-8879', 35);
insert into member (id, name, gender, post_num, address, tel, age) value ('na', '나', 'M', '607-010', '부산시 동래구 명륜동', '764-3784', 33);
insert into member (id, name, gender, post_num, address, tel, age) value ('da', '다', 'M', '503-200', '광주시 남구 지석동', '298-9730', 34);
insert into member (id, name, gender, post_num, address, tel, age) value ('ra', '라', 'M', '503-201', '부산시 영도구 봉래동 5가', '838-4347', 21);
insert into member (id, name, gender, post_num, address, tel, age) value ('ma', '마', 'W', '606-065', '서울시 은평구 응암4동', '399-9809', 24);
insert into member (id, name, gender, post_num, address, tel, age) value ('ba', '바', 'M', '122-014', '경기도 과천시 중앙동', '857-5683', 30);
insert into member (id, name, gender, post_num, address, tel, age) value ('sa', '사', 'W', '427-760', '경기도 시흥시 신천동', '234-7677', 22);
insert into member (id, name, gender, post_num, address, tel, age) value ('oa', '아', 'M', '429-020', '광주시 남구 도금동', '370-6003', 63);