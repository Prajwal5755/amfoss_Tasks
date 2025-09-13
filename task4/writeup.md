WRITEUP FOR DATABASE FOR MY REFERENCE
```
mysql
Queries

INSERT
syntax 
INSERT INTO table(col1,col2...) VALUES (val1,val2..)

DELETE
syntax
DELETE FROM table WHERE condition;

UPDATE 
UPDATE table SET col1=val1 WHERE col2=val2;

CREATE
CREATE TABLE table_name(
 id INT PRIMARY KEY,
 name VARCHAR(255)
);

ALTER
ALTER TABLE table_name ADD col DATATYPE;

DROP TABLE table_name; delete

TRUNCATE TABLE table_name;

RENAME TABLE old_table TO new;

SELECT*FROM table WHERE condition;

DQL(Data Query Language)
SELECT 


DDL
CREATE,ALTER,DROP,TRUNCATE,RENAME

DML
INSERT,UPDATE,DELETE

DQL
SELECT

DCL
GRANT,REVOKE

TCL
START TRANSACTION,COMMIT,ROLLBACK

cusor
Is a mysql database object iterate through rows
one row at a time and readonly
```

APPROACH TO PROJECT
```
Fisrst i have expoerted all csv file data to my csv file, Then in dashboard.py i have defined function to fetch data from my database and Learnt about QTableWidget to populate table to be displayed 
```

```
Then I created list for user fiter and edited buttons according to it like made True for elments in List buttonstyle then executed query to compare user filter and databse 
```

```
Then i have exported table i got to csv file like creating new csv file
```

