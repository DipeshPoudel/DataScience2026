-- =============================================================================
-- MariaDB Join Demonstration — run top to bottom, one statement at a time
-- Topics: INNER JOIN, LEFT JOIN, RIGHT JOIN, CROSS JOIN
-- =============================================================================

CREATE DATABASE if NOT EXISTS uni_db;

use uni_db;

-- STEP 1: Clean up (safe to re-run)
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS shirt_colors;
DROP TABLE IF EXISTS shirt_sizes;

-- STEP 2: Create tables
CREATE TABLE departments (
    dept_id   INT          NOT NULL PRIMARY KEY,
    dept_name VARCHAR(50)  NOT NULL
);

CREATE TABLE employees (
    emp_id    INT          NOT NULL PRIMARY KEY,
    emp_name  VARCHAR(50)  NOT NULL,
    dept_id   INT          NULL,
    CONSTRAINT fk_employees_dept
        FOREIGN KEY (dept_id) REFERENCES departments (dept_id)
);

CREATE TABLE shirt_colors (
    color_id   INT         NOT NULL PRIMARY KEY,
    color_name VARCHAR(20) NOT NULL
) ;

CREATE TABLE shirt_sizes (
    size_id   INT         NOT NULL PRIMARY KEY,
    size_code VARCHAR(5)  NOT NULL
);

-- STEP 3: Load data
INSERT INTO departments (dept_id, dept_name) VALUES
    (10, 'Sales'),
    (20, 'Engineering'),
    (30, 'Marketing'),
    (40, 'HR');

INSERT INTO employees (emp_id, emp_name, dept_id) VALUES
    (1,  'Alice',   10),
    (2,  'Bob',     10),
    (3,  'Carol',   20),
    (4,  'David',   20),
    (5,  'Eve',     NULL),
    (6,  'Frank',   NULL);

INSERT INTO shirt_colors (color_id, color_name) VALUES
    (1, 'Red'),
    (2, 'Blue'),
    (3, 'Green');

INSERT INTO shirt_sizes (size_id, size_code) VALUES
    (1, 'S'),
    (2, 'M'),
    (3, 'L');

-- STEP 4: Preview source tables (4 departments, 6 employees)
SELECT 'departments' AS table_name;
SELECT * FROM departments ORDER BY dept_id;

SELECT 'employees' AS table_name;
SELECT * FROM employees ORDER BY emp_id;

-- STEP 5: INNER JOIN — only rows with a match on both sides (expect 4 rows)
SELECT
    e.emp_id,
    e.emp_name,
    d.dept_id,
    d.dept_name
FROM employees AS e
INNER JOIN departments AS d
    ON e.dept_id = d.dept_id
ORDER BY e.emp_id;

-- STEP 6: LEFT JOIN — all employees, dept filled when matched (expect 6 rows)
SELECT
    e.emp_id,
    e.emp_name,
    d.dept_id,
    d.dept_name
FROM employees AS e
LEFT JOIN departments AS d
    ON e.dept_id = d.dept_id
ORDER BY e.emp_id;

-- STEP 7: RIGHT JOIN — all departments, employee filled when matched (expect 5 rows)
SELECT
    e.emp_id,
    e.emp_name,
    d.dept_id,
    d.dept_name
FROM employees AS e
RIGHT JOIN departments AS d
    ON e.dept_id = d.dept_id
ORDER BY d.dept_id, e.emp_id;

-- STEP 8: Preview CROSS JOIN source tables (3 colors, 3 sizes)
SELECT 'shirt_colors' AS table_name;
SELECT * FROM shirt_colors ORDER BY color_id;

SELECT 'shirt_sizes' AS table_name;
SELECT * FROM shirt_sizes ORDER BY size_id;

-- STEP 9: CROSS JOIN — every color paired with every size (expect 9 rows)
SELECT
    c.color_name,
    s.size_code
FROM shirt_colors AS c
CROSS JOIN shirt_sizes AS s
ORDER BY c.color_name, s.size_code;
