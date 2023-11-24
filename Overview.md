### SQLite - A Lightweight Relational Database Management System

## Table of Contents

- [Introduction](#introduction)
- [Package/Library Selection](#package-library-selection)
- [Package/Library Details](#package-library-details)
- [Package/Library History](#package-library-history)
- [Reasons for Selection](#reasons-for-selection)
- [Impact on Learning](#impact-on-learning)
- [Overall Experience](#overall-experience)

## 1. Introduction <a name="introduction"></a>

SQLite is a widly-used, lightweight, relational database management system. SQLite does not have server process instead it reads and write directly to ordinary db files.[1]

## 2. Package/Library Selection <a name="package-library-selection"></a>

For this project, I selected the following package/library:

Package/Library: sqlite3

SQLite was chosen for its simplicity, portability and reputation of being most widly used database engine in the world.[2]

### How to use it?

1. First, you need to import the 'sqlite3' module [5]

   ```python
   import sqlite3
   ```

2. To work with an SQLite database, you need to establish a connection to it. If the specified database does not exist, SQLite will create it for you. [5]

   ```python
   conn = sqlite3.connect('mydatabase.db')
   ```

3. Create tables. SQLite is a relational database so you need to define tables with columns to structure your data. 'CREATE TABLE' statements define your tables. [5]

   ```python
   # Create a table
   conn.execute('''
       CREATE TABLE IF NOT EXISTS employees (
           id INTEGER PRIMARY KEY,
           name TEXT NOT NULL,
           department TEXT,
           salary REAL
       )
   ''')
   ```

4. You can insert data into your SQLite database using SQL INSERT statements. The execute() method is used to run SQL commands. [5]

   ```python
   # Insert data into the table
    conn.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", ("John Doe", "HR", 50000.0))
   ```

5. To retrieve data from the database, you can use SQL SELECT statements. The execute() method is also used to run queries, and the results can be fetched using the fetchone() or fetchall() methods. [5]
   ```python
   # Query data from the table
    result = conn.execute("SELECT * FROM employees")
    for row in result:
        print(row)
   ```
6. Update and Delete data. [5]

   ```python
   # Update data
   conn.execute("UPDATE employees SET salary = 55000.0 WHERE name = 'John Doe'")

   # Delete data
   conn.execute("DELETE FROM employees WHERE name = 'John Doe'")
   ```

7. After making changes to the database, it's essential to commit those changes using the commit() method. Finally, close the database connection to release resources [5]

   ```python
   # Commit changes and close the connection
   conn.commit()
   conn.close()
   ```

## 3. Package/Library Details <a name="package-library-details"></a>

SQLite serves as an embedded, serverless relational database management system. It's an open-source library, useful for applications requiring database management wihout a server.[3]

SQLite offers a wide range of functionalities, including:

- Creating Databases: You can create a new SQLite database using the sqlite3 command or by connecting to an existing database file.
- Defining Tables: You can define tables with columns and data types.
- Inserting Data: You can insert records into tables using SQL INSERT statements.
- Querying Data: Retrieve data from tables using SQL SELECT statements.
- Updating and Deleting Data: Modify and delete data using SQL UPDATE and DELETE statements.
- Transaction Support: SQLite supports transactions to ensure data integrity.
- Indexing: You can create indexes on columns for faster query performance.
- Data Types: Supports various data types, including INTEGER, TEXT, REAL, BLOB, and NULL.
- Triggers and Views: Allows creating triggers and views to manage data and queries efficiently.[1]

## Example:

```python
import sqlite3

# Connect to a database or create a new one
conn = sqlite3.connect('mydatabase.db')

# Create a table
conn.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT,
        salary REAL
    )
''')

# Insert data
conn.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", ("John Doe", "HR", 50000.0))

# Query data
result = conn.execute("SELECT * FROM employees")
for row in result:
    print(row)

# Commit changes and close the connection
conn.commit()
conn.close()

```

## 4. Package/Library History <a name="package-library-history"></a>

SQLite was designed by D. Richard Hipp in the spring of 2000, initially as a Tcl extension. It evolved over time, with significant updates like SQLite 3.0 adding internationalization and other major improvements [3]

## 5. Reasons for Selection <a name="reasons-for-selection"></a>

I've already had experience using SQLite in other language. It occured to me that SQLite would be a good combination with beautiful soup library which I used in previous exploration acitivy. Beautiful soup is about data extraction and I integrated SQLite which is data management library to further enhance my program.

## 6. Impact on Learning <a name="impact-on-learning"></a>

Integrating SQLite's database management capabilities with the data parsing functions of Beautiful Soup in python significantly enhanced my understanding of how different libraries can work together.

## 7. Overall Experience <a name="overall-experience"></a>

- SQLite's simplicity and efficiency in managing database definetly makes it a great tool.
- recommended for projects where database server is not required or where portability is a priority [4]
- I will continue using SQLite for my future application because it's efficient when full-fledged database server is not required

### References

1. ["What is SQLite?" Database.guide.](https://database.guide/what-is-sqlite/)
2. ["SQLite Home Page." SQLite.org.](https://www.sqlite.org/index.html)
3. ["SQLite - Wikipedia." Wikipedia.](https://en.wikipedia.org/wiki/SQLite/)
4. ["7 Advantages of SQLite." SQL Docs.](https://sqldocs.org/sqlite/sqlite-advantages/)
5. [sqlite3 — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3/library/sqlite3.html)
