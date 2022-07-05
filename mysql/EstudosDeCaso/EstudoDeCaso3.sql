create database EstudoDeCaso3;

use EstudoDeCaso3;

create table Enfermeiro(
	PK_ENFERMEIRO int not null AUTO_INCREMENT,
  	nome varchar(100) not null,
  	coren varchar(15) not null unique,
  	endereco varchar(100) not null,
  
  	primary key(PK_ENFERMEIRO)
);

create table Enfermaria(
	PK_ENFERMARIA int not null AUTO_INCREMENT,
  	lugar varchar(25) not null,
  	qtd_leitos int not null,
  
  	primary key (PK_ENFERMARIA)
);

create table Alocacao(
	PK_ALOCACAO int not null AUTO_INCREMENT,
  	PK_FK_ENFERMEIRO int not null,
  	PK_FK_ENFERMARIA int not null,
  
  	foreign key(PK_FK_ENFERMEIRO) references Enfermeiro(PK_ENFERMEIRO),
  	foreign key(PK_FK_ENFERMARIA) references Enfermaria(PK_ENFERMARIA),
  	
  	primary key(PK_ALOCACAO, PK_FK_ENFERMEIRO, PK_FK_ENFERMARIA)
);