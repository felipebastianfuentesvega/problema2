-- borramos las tablas, si ya existian
drop table multas_estacionamiento;
drop table inspectores;

-- creamos las tablas .

create table inspectores(
    id int auto_increment,
    nombre varchar(50),
    rut varchar(13),
    primary key(id)
);




create table multas_estacionamiento(
    id int auto_increment,
    patente varchar(6),
    fechayhora datetime,
    lugar varchar(200),
    pagada bool,
    inspectorid int,
    primary key(id),
    foreign key (inspectorid) references inspectores(id)
);

-- insertamos un par de datos para probar

insert into inspectores (nombre, rut) values ('Juan Lopez' , '12678764-2');
insert into inspectores (nombre, rut) values ('Edmundo Contreras' , '13123267-5');


insert into multas_estacionamiento 
    (patente, fechayhora , lugar, pagada , inspectorid )
    VALUES
    ('CFHT32', now() , 'Antonio Varas frente al 666' , FALSE , 1 );

insert into multas_estacionamiento 
    (patente, fechayhora , lugar, pagada , inspectorid )
    VALUES
    ('UN1111', now() , 'Pasaje Uno, frente al 132' , FALSE , 2 );


-- vemos si todo anda bien:
select nombre, patente, lugar from multas_estacionamiento inner join inspectores 
on inspectores.id = multas_estacionamiento.inspectorid;


