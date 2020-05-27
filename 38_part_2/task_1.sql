/*
 * write a query in SQL to display the first name, last name, 
 * department number, and department name for each employee
*/
SELECT e.first_name AS 'First Name'
	   ,e.last_name AS 'Last Name'
	   ,e.department_id AS 'Department Number'
	   ,d.depart_name AS 'Department Name'
FROM employees e
LEFT JOIN departments d ON d.department_id = e.department_id;

/*
 * write a query in SQL to display the first and last name, department,
 * city, and state province for each employee
*/
SELECT e.first_name AS 'First Name'
	   ,e.last_name AS 'Last Name'
	   ,e.department_id AS 'Department Number'
	   ,d.depart_name AS 'Department Name'
	   ,l.city AS 'City'
	   ,l.state_province AS 'State Province'
FROM employees e
LEFT JOIN departments d ON d.department_id = e.department_id
LEFT JOIN locations l ON l.location_id = d.location_id;

/*
 * write a query in SQL to display the first name, last name, 
 * department number, and department name, for all employees 
 * for departments 80 or 40
*/
SELECT e.first_name AS 'First Name'
	   ,e.last_name AS 'Last Name'
	   ,e.department_id AS 'Department Number'
	   ,d.depart_name AS 'Department Name'
FROM employees e
LEFT JOIN departments d ON d.department_id = e.department_id
WHERE e.department_id = 80
   OR e.department_id = 40;
   
/*
 * write a query in SQL to display all departments including those 
 * where does not have any employee
*/
SELECT d.department_id AS 'Department Number'
	   ,d.depart_name AS 'Department Name'
	   ,COUNT(e.employee_id) AS 'Number Of Employees'
FROM departments d
LEFT JOIN employees e ON e.department_id = d.department_id
GROUP BY d.department_id;

/*
 * write a query in SQL to display the first name of all employees 
 * including the first name of their manager
*/
SELECT e1.first_name AS 'Employee First Name'
	   ,e2.first_name AS 'Manager First Name'
FROM employees e1
LEFT JOIN employees e2 ON e2.employee_id = e1.manager_id;

/*
 * write a query in SQL to display the job title, full name 
 * (first and last name ) of the employee, and the difference 
 * between the maximum salary for the job and the salary of the employee
*/
SELECT j.job_title AS 'Job Title'
       ,e.first_name || ' ' || e.last_name AS 'Full Name'
       ,m.max_salary - e.salary AS 'Diff From Max Salary'
FROM employees e
LEFT JOIN jobs j ON j.job_id = e.job_id
LEFT JOIN 
	(SELECT job_id,
	        MAX(salary) AS 'max_salary'
	 FROM employees
	 GROUP BY job_id) m ON m.job_id = e.job_id;

/*
 * write a query in SQL to display the job title 
 * and the average salary of employees
*/
SELECT j.job_title AS 'Job Title'
       ,a.avg_salary AS 'Average Salary'
FROM jobs j 
LEFT JOIN
	(SELECT job_id
	        ,AVG(salary) as 'avg_salary'
	 FROM employees
	 GROUP BY job_id) a ON a.job_id = j.job_id;

/*
 * write a query in SQL to display the full name (first and last name), 
 * and salary of those employees who work in any department located in London
*/
SELECT e.first_name || ' ' || e.last_name AS 'Full Name'
	   ,e.salary AS 'Salary'
FROM employees e
LEFT JOIN departments d ON d.department_id = e.department_id
LEFT JOIN locations l ON l.location_id = d.location_id
WHERE l.city = 'London';

/*
 * write a query in SQL to display the department name 
 * and the number of employees in each department
*/
SELECT d.depart_name AS 'Department Name'
       ,CASE
           WHEN c.count_emp IS NULL THEN 0
           ELSE c.count_emp
       END AS 'Number Of Employees'
FROM departments d
LEFT JOIN
    (SELECT department_id
            ,COUNT(employee_id) AS 'count_emp'
     FROM employees
     GROUP BY department_id) c ON c.department_id = d.department_id;