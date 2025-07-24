# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT e2.employee_id, e2.name, count(DISTINCT e1.employee_id) AS reports_count, round(avg(e1.age), 0) AS average_age
FROM Employees e1
JOIN Employees e2
WHERE e1.reports_to = e2.employee_id
GROUP BY employee_id