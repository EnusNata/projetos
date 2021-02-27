create database primeiroprojeto;

use primeiroprojeto;

create table MEDICO(
	CRM  varchar(15) not null unique,
	nome varchar(100) not null,
	primary key (CRM)
);

create table PACIENTE(
	codigo int(2) not null unique,
	nome varchar(100) not null,
	primary key(codigo)
);

create table CONSULTA(
	data date not null,
	hora time not null,
	CRM varchar(15),
	codigo int(2),
	
	foreign key (CRM) 
		references MEDICO(CRM),
	foreign key (codigo)
		references PACIENTE(codigo),
	primary key(codigo,CRM,data)
);

insert into MEDICO(CRM,nome)
			values
            ('meucrm','doctorwho'),
            ('seucrm','doctorhouse');

insert into PACIENTE(codigo,nome)
			values
            (01,'naruto'),
            (17,'bolsonaro');
            
insert into CONSULTA(data,hora,CRM,codigo)
			values
            ('2018-09-10','15:21:11','meucrm',01),
            ('2018-09-11','17:21:11','seucrm',17);

#verificações

show tables;

desc MEDICO;
desc PACIENTE;
desc CONSULTA;

select *from CONSULTA
where year(data) = 2019;

#verificações