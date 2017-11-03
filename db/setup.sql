-- 1. Login as the postgres user and run 'create database netscan'.
-- 2. Use psql to create the netscan tables like this:
--    psql -h db_host -U user -d netscan < setup.sql

create table ports(
name varchar(32) not null default 'unknown',
number integer primary key,
description text not null default 'unknown');

create table hosts(
address inet primary key,
name varchar(128) not null default 'unknown'
);

create table activity(
date timestamp not null,
host inet REFERENCES hosts (address) ON DELETE RESTRICT ON UPDATE RESTRICT not null,
port integer REFERENCES ports (number) ON DELETE CASCADE ON UPDATE RESTRICT not null,
off_campus boolean not null default false,
primary key (date, host, port));

