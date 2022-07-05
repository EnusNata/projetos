create database EstudoDeCaso2;

use EstudoDeCaso2;

create table Medico(
	PK_MEDICO int not null AUTO_INCREMENT,
  	nome varchar(100) not null,
  	crm varchar(15) not null unique,
  	endereco varchar(100) not null,
  
  	primary key(PK_MEDICO)
);

create table Consulta(
	PK_CONSULTA int not null AUTO_INCREMENT,
  	data date not null,
  	hora time not null,
  	diagnostico varchar(50) not null,
  	FK_MEDICO_CONSULTA int not null,
  
  	primary key(PK_CONSULTA),
  	foreign key(FK_MEDICO_CONSULTA) references Medico(PK_MEDICO)
);