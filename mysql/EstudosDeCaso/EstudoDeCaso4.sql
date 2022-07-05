show databases;

create database EstudoDeCaso4;

use EstudoDeCaso4;

create table Passageiro(
	PK_PASSAGEIRO int not null AUTO_INCREMENT,
  	nome varchar(100) not null,
  	cpf char(11) not null unique,
  	endereco varchar(100) not null,
  
  	primary key(PK_PASSAGEIRO)
);

create table Voo(
	PK_VOO int not null AUTO_INCREMENT,
  	numero int not null unique,
  	data_voo date not null,
  	aeronave varchar(15) not null,
  	origem varchar(25) not null,
  	destino varchar(25) not null,
  
  	primary key(PK_VOO)
);

create table Reserva(
	PK_RESERVA int not null AUTO_INCREMENT,
  	PK_FK_PASSAGEIRO int not null,
  	PK_FK_VOO int not null,
  
  	codigo int not null unique,
  	data_reserva date not null,
  
  	foreign key(PK_FK_PASSAGEIRO) references Passageiro(PK_PASSAGEIRO),
  	foreign key(PK_FK_VOO) references Voo(PK_VOO),
  	
  	primary key(PK_RESERVA, PK_FK_PASSAGEIRO, PK_FK_VOO)
);