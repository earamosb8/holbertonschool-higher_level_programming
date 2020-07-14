-- script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
-- using CHAR_lENGTH
SELECT score, name FROM second_table WHERE CHAR_LENGTH(name) > 0 ORDER BY score DESC;
