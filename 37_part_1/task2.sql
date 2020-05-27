/*
 * write a query to display the names (first_name, last_name) using alias name 
 * "First Name", "Last Name" from the table of employees;
 */
SELECT first_name AS 'First Name'
	   ,last_name AS 'Last Name'
FROM employees;

/*
 * write a query to get the unique department ID from the employee table
 */
SELECT DISTINCT department_id
FROM employees;

/*
 * write a query to get all employee details from the employee table 
 * ordered by first name, descending
 */
SELECT *
FROM employees
ORDER BY first_name DESC;

/*
 * write a query to get the names (first_name, last_name), salary, 
 * PF of all the employees (PF is calculated as 12% of salary) 
*/
SELECT first_name AS 'First Name'
	   ,last_name AS 'Last Name'
	   ,salary AS 'Salary'
	   ,salary * 0.12 AS 'PF'
FROM employees;

/*
 * write a query to get the maximum and minimum salary from the employees table
*/
SELECT MAX(salary) AS "Max Salary"
	   ,MIN(salary) AS "Min Salary"
FROM employees;

/*
 * write a query to get a monthly salary (round 2 decimal places) of each and every employee
*/
SELECT first_name AS 'First Name'
	   ,last_name AS 'Last Name'
	   ,round(salary, 2) AS 'Monthly Salary'
FROM employees;
