USE timelog;

CREATE TABLE `timelog`.`project` ( 
    `id` INT AUTO_INCREMENT , 
    `name` VARCHAR(32) , 
    `category` INT , 
    `priority` INT , 
    `description` VARCHAR(256) ,
    PRIMARY KEY (`id`)
    )default charset=utf8; 

CREATE TABLE `timelog`.`user` ( 
    `username` VARCHAR(32) , 
    `name` VARCHAR(32) , 
    `password` VARCHAR(32) , 
    `email` VARCHAR(32) , 
    `role` VARCHAR(32) , 
    PRIMARY KEY (`username`)
    )default charset=utf8; 

CREATE TABLE `timelog`.`task` ( 
    `id` INT AUTO_INCREMENT , 
    `user_name` VARCHAR(32) , 
    `project_id` INT , 
    `date` DATE , 
    `hours` INT , 
    `desc` VARCHAR(256) , 
    PRIMARY KEY (`id`)
    )default charset=utf8; 
