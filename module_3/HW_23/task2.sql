select first_name as "First Name", last_name as "Last Name" from employees;

select distinct department_id from employees;

select * from employees order by first_name desc;

select first_name, last_name, salary, 0.12*salary as PF from employees;

select max(salary), min(salary) from employees;

select round(div(salary, 12), 2) as "monthly salary" from employees;