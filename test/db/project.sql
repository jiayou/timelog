USE `timelog`;
create table project (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	project_name VARCHAR(50),
	category VARCHAR(50),
	`priority` VARCHAR(50),
	`description` TEXT
)default charset=utf8;
insert into project (id, project_name, category, `priority`, `description`) values (1, 'Marin', 'Ford', 'L', 'Donec ut mauris eget massa tempor convallis.');
insert into project (id, project_name, category, `priority`, `description`) values (2, 'Gusty', 'Mitsubishi', '3XL', 'In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem.');
insert into project (id, project_name, category, `priority`, `description`) values (3, 'Lurline', 'Mazda', 'L', 'Duis consequat dui nec nisi volutpat eleifend.');
insert into project (id, project_name, category, `priority`, `description`) values (4, 'Row', 'Pontiac', '2XL', 'Donec vitae nisi.');
insert into project (id, project_name, category, `priority`, `description`) values (5, 'Tallia', 'Eagle', 'XS', 'Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci.');
insert into project (id, project_name, category, `priority`, `description`) values (6, 'Reinald', 'Mitsubishi', 'XS', 'Cras pellentesque volutpat dui.');
insert into project (id, project_name, category, `priority`, `description`) values (7, 'Desmond', 'Toyota', 'XL', 'Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis.');
insert into project (id, project_name, category, `priority`, `description`) values (8, 'Stacy', 'Mitsubishi', '3XL', 'Suspendisse potenti.');
insert into project (id, project_name, category, `priority`, `description`) values (9, 'Steve', 'Nissan', 'M', 'Nam dui.');
insert into project (id, project_name, category, `priority`, `description`) values (10, 'Colby', 'Acura', 'L', 'Nulla nisl.');
insert into project (id, project_name, category, `priority`, `description`) values (11, 'Thacher', 'Jensen', 'XS', 'Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo.');
insert into project (id, project_name, category, `priority`, `description`) values (12, 'Jesse', 'Pontiac', 'XS', 'Etiam vel augue.');
insert into project (id, project_name, category, `priority`, `description`) values (13, 'Eugine', 'Mitsubishi', 'XL', 'Vestibulum quam sapien, varius ut, blandit non, interdum in, ante.');
insert into project (id, project_name, category, `priority`, `description`) values (14, 'Web', 'Land Rover', '2XL', 'Sed accumsan felis.');
insert into project (id, project_name, category, `priority`, `description`) values (15, 'Terri', 'Pontiac', 'XS', 'Maecenas rhoncus aliquam lacus.');
insert into project (id, project_name, category, `priority`, `description`) values (16, 'Terese', 'Bentley', 'XS', 'Vestibulum ac est lacinia nisi venenatis tristique.');
insert into project (id, project_name, category, `priority`, `description`) values (17, 'Griffie', 'GMC', 'XS', 'Maecenas tincidunt lacus at velit.');
insert into project (id, project_name, category, `priority`, `description`) values (18, 'Jo ann', 'Bentley', 'S', 'Sed ante.');
insert into project (id, project_name, category, `priority`, `description`) values (19, 'Darrell', 'Mitsubishi', 'XL', 'Duis ac nibh.');
insert into project (id, project_name, category, `priority`, `description`) values (20, 'Loydie', 'Chevrolet', '2XL', 'Vestibulum sed magna at nunc commodo placerat.');
insert into project (id, project_name, category, `priority`, `description`) values (21, 'Perle', 'Toyota', 'XL', 'Pellentesque at nulla.');
insert into project (id, project_name, category, `priority`, `description`) values (22, 'Abbi', 'Mazda', '2XL', 'Aenean auctor gravida sem.');
insert into project (id, project_name, category, `priority`, `description`) values (23, 'Candie', 'BMW', 'XS', 'Ut tellus.');
insert into project (id, project_name, category, `priority`, `description`) values (24, 'Hale', 'Dodge', '2XL', 'Phasellus in felis.');
insert into project (id, project_name, category, `priority`, `description`) values (25, 'Zia', 'Mercury', 'L', 'Mauris sit amet eros.');
insert into project (id, project_name, category, `priority`, `description`) values (26, 'Adria', 'Mercedes-Benz', 'XL', 'Fusce posuere felis sed lacus.');
insert into project (id, project_name, category, `priority`, `description`) values (27, 'Sabrina', 'Land Rover', 'L', 'Ut tellus.');
insert into project (id, project_name, category, `priority`, `description`) values (28, 'Althea', 'Toyota', 'XL', 'Curabitur in libero ut massa volutpat convallis.');
insert into project (id, project_name, category, `priority`, `description`) values (29, 'Eberto', 'Ford', 'XS', 'Nullam molestie nibh in lectus.');
insert into project (id, project_name, category, `priority`, `description`) values (30, 'Flem', 'Kia', 'S', 'Vivamus tortor.');
insert into project (id, project_name, category, `priority`, `description`) values (31, 'Daveta', 'GMC', '3XL', 'Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue.');
insert into project (id, project_name, category, `priority`, `description`) values (32, 'Irita', 'Lexus', 'M', 'Aliquam sit amet diam in magna bibendum imperdiet.');
insert into project (id, project_name, category, `priority`, `description`) values (33, 'Jaquenette', 'Daewoo', 'XL', 'Donec ut mauris eget massa tempor convallis.');
insert into project (id, project_name, category, `priority`, `description`) values (34, 'Fionna', 'Chevrolet', 'XL', 'Aliquam quis turpis eget elit sodales scelerisque.');
insert into project (id, project_name, category, `priority`, `description`) values (35, 'Jody', 'Mercedes-Benz', 'XS', 'Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.');
insert into project (id, project_name, category, `priority`, `description`) values (36, 'Eliot', 'Dodge', 'M', 'Curabitur gravida nisi at nibh.');
insert into project (id, project_name, category, `priority`, `description`) values (37, 'Matelda', 'Plymouth', '3XL', 'Pellentesque eget nunc.');
insert into project (id, project_name, category, `priority`, `description`) values (38, 'Ximenez', 'Chevrolet', '3XL', 'Morbi non lectus.');
insert into project (id, project_name, category, `priority`, `description`) values (39, 'Brig', 'Lexus', 'XS', 'In hac habitasse platea dictumst.');
insert into project (id, project_name, category, `priority`, `description`) values (40, 'Sile', 'Ford', 'L', 'Aenean sit amet justo.');
insert into project (id, project_name, category, `priority`, `description`) values (41, 'North', 'Ford', 'XL', 'Suspendisse potenti.');
insert into project (id, project_name, category, `priority`, `description`) values (42, 'Alley', 'BMW', 'S', 'Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue.');
insert into project (id, project_name, category, `priority`, `description`) values (43, 'Josi', 'Ford', 'M', 'In hac habitasse platea dictumst.');
insert into project (id, project_name, category, `priority`, `description`) values (44, 'Trix', 'Volkswagen', 'XL', 'Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.');
insert into project (id, project_name, category, `priority`, `description`) values (45, 'Scarface', 'Infiniti', '2XL', 'Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.');
insert into project (id, project_name, category, `priority`, `description`) values (46, 'Celia', 'Chevrolet', 'M', 'Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue.');
insert into project (id, project_name, category, `priority`, `description`) values (47, 'Rafael', 'Dodge', '2XL', 'Integer ac neque.');
insert into project (id, project_name, category, `priority`, `description`) values (48, 'Drugi', 'Buick', 'L', 'Nulla facilisi.');
insert into project (id, project_name, category, `priority`, `description`) values (49, 'Gerard', 'Cadillac', 'L', 'Integer tincidunt ante vel ipsum.');
insert into project (id, project_name, category, `priority`, `description`) values (50, 'Olimpia', 'Mazda', 'L', 'Nullam varius.');
