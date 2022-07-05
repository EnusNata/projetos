create database EstudoDeCaso5;

use EstudoDeCaso5;

create table Cliente(
	PK_CLIENTE int not null AUTO_INCREMENT,
  	nome varchar(100) not null,
  	cpf char(11) not null unique,
  	endereco varchar(100) not null,
  	
  	primary key(PK_CLIENTE)
);

create table Produto(
	PK_PRODUTO int not null AUTO_INCREMENT,
  	codigo int not null unique,
  	data_cadastro date not null,
  	valor double(8,2) not null,
  	
  	primary key(PK_PRODUTO)
);

create table Pedido(
	PK_PEDIDO int not null AUTO_INCREMENT,
  	codigo int not null unique,
  	data_pedido date not null,
  	valor double(8,2) not null,
  	FK_PK_CLIENTE int not null,
  	
  	primary key(PK_PEDIDO),
  
  	foreign key(FK_PK_CLIENTE) references Cliente(PK_CLIENTE)
);

create table Pedido_Produto(
	PK_PEDIDO_PRODUTO int not null AUTO_INCREMENT,
  	PK_FK_PEDIDO int not null,
  	PK_FK_PRODUTO int not null,
  
  	qtd_produto int not null,
  
  	foreign key(PK_FK_PEDIDO) references Pedido(PK_PEDIDO),
  	foreign key(PK_FK_PRODUTO) references Produto(PK_PRODUTO),
  
  	primary key(PK_PEDIDO_PRODUTO, PK_FK_PEDIDO, PK_FK_PRODUTO)
);