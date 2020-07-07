create table Ubicacion(
Cod_Ubicacion int not null,
Region varchar(50) not null,
Ciudad varchar(50) not null,
Comuna varchar(50) not null,
primary key (Cod_Ubicacion)
);

create table Aporte(
Cod_Aporte int not null,
Tipo_Aporte varchar(60) not null,
primary key (Cod_Aporte)
);

create table Empresa(
Cod_Empresa int not null,
Cod_Ubicacion int not null,
Nom_Empresa varchar(50) not null,
Nom_Representante varchar(60) not null,
Fono_Empresa int not null,
Email_emporesa varchar(60) not null,
primary key (cod_Empresa),
foreign key (cod_Ubicacion) references Ubicacion (cod_Ubicacion)
);

create table Trabajador(
Rut int not null,
Nom_Trabajador varchar(60) not null,
Email_Trabajador varchar(60) not null,
Fono_Trabajador int not null,
Password varchar(16) not null,
primary key (Rut)
);

create table Trabaja(
Cod_Trabaja int not null,
Rut int not null,
Cod_Empresa int not null,
Cod_Aporte int not null,
Fecha_Inicio date not null,
Fecha_Final date,
primary key (Cod_Trabaja),
foreign key (Rut) references Trabajador(Rut),
foreign key (Cod_Empresa) references Empresa(Cod_Empresa),
foreign key (Cod_Aporte) references Aporte(Cod_Aporte)
); 
