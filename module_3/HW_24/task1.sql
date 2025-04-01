-- 1
select
	first_name,
	last_name,
	e.department_id,
	depart_name
from
	employees e
join departments d on
	e.department_id = d.department_id;

-- 2
select
	first_name,
	last_name,
	depart_name,
	city,
	state_province
from
	employees e
join departments d on
	e.department_id = d.department_id
join locations l on
	d.location_id = l.location_id;

-- 3
select
	first_name,
	last_name,
	e.department_id,
	depart_name
from
	employees e
join departments d on
	e.department_id = d.department_id
where
	e.department_id in (80, 40);

-- 4
select
	first_name,
	last_name,
	d.department_id,
	depart_name
from
	employees e
right join departments d on
	e.department_id = d.department_id;

-- 5
select
	e.first_name as employee,
	m.first_name as manager
from
	employees e
left join employees m on
	e.manager_id = m.employee_id;

-- 6
select
	job_title,
	concat(first_name, ' ', last_name) as "full name",
	max_salary - salary as difference
from
	employees e
join jobs j on
	e.job_id = j.job_id;

-- 7
select
	job_title,
	avg(salary)
from
	employees e
join jobs j on
	e.job_id = j.job_id
group by
	job_title;

-- 8
select
	concat(first_name, ' ', last_name) as "full name",
	salary,
	city
from
	employees e
join departments d on
	e.department_id = d.department_id
join locations l on
	d.location_id = l.location_id
where
	city = 'London';

-- 9
select
	depart_name,
	count(employee_id)
from
	employees e
right join departments d on
	e.department_id = d.department_id
group by
	depart_name;