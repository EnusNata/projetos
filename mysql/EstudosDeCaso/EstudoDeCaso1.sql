create database EstudoDeCaso1;

use EstudoDeCaso1;

create table Empregado(
	PK_EMPREGADO int not null AUTO_INCREMENT,
  	nome varchar(100) not null,
  	cpf char(11) not null unique,
  	endereco varchar(100) not null,
  	
  	primary key(PK_EMPREGADO)
);

create table Departamento(
	PK_DEPARTAMENTO int not null AUTO_INCREMENT,
  	nome varchar(25) not null unique,
  	numero int not null unique,
  	FK_EMPREGADO_GERENTE int not null unique, 
  
  	primary key(PK_DEPARTAMENTO),
  	foreign key(FK_EMPREGADO_GERENTE) references Empregado(PK_EMPREGADO)
);

