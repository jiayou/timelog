USE mysql;

-- DROP USER 'adas'@'%';
CREATE USER 'timelog'@'%' IDENTIFIED BY 'timelog';

DROP DATABASE IF EXISTS `timelog`;
CREATE DATABASE `timelog`;

USE `timelog`;

GRANT ALL PRIVILEGES ON `timelog`.* TO 'timelog'@'%' IDENTIFIED BY 'timelog' WITH GRANT OPTION;
FLUSH PRIVILEGES;

CREATE TABLE `timelog`.`project` ( 
    `id` INT NOT NULL AUTO_INCREMENT , 
    `name` VARCHAR NOT NULL , 
    `productive` BOOLEAN NOT NULL , 
    `priority` INT NOT NULL , 
    `description` VARCHAR NOT NULL , 
    PRIMARY KEY (`id`)
    ); 

CREATE TABLE `timelog`.`user` ( 
    `username` VARCHAR NOT NULL , 
    `name` VARCHAR NOT NULL , 
    `password` VARCHAR NOT NULL , 
    `email` VARCHAR NOT NULL , 
    `role` VARCHAR NOT NULL , 
    PRIMARY KEY (`username`)
    ); 

CREATE TABLE `timelog`.`task` ( 
    `id` INT NOT NULL AUTO_INCREMENT , 
    `user_name` VARCHAR NOT NULL , 
    `project_id` VARCHAR NOT NULL , 
    `date` VARCHAR NOT NULL , 
    `hours` VARCHAR NOT NULL , 
    `desc` VARCHAR NOT NULL , 
    PRIMARY KEY (`id`)
    ); 

INSERT INTO `timelog`.`task` VALUE ()
