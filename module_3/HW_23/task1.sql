create table teachers (
	teacher_id integer primary key,
	teacher_name varchar(50) not null,
	salary money,
	date_of_joining date
);

alter table teachers rename to lecturers;

alter table lecturers add column regalia varchar(25) not null;

INSERT INTO lecturers (teacher_id, teacher_name, salary, date_of_joining, regalia) VALUES 
(1, 'Anna', 5000, '01/01/2021', 'docent'),
(2, 'Maksym', 4000, '01/08/2020', 'docent'),
(3, 'Denys', 3000, '03/07/2023', 'senior lecturer');


UPDATE lecturers SET salary = 6000 WHERE teacher_id = 1;

DELETE from lecturers WHERE teacher_name = 'Maksym';