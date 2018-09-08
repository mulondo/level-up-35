import psycopg2

#connect to database
con=psycopg2.connect(host="localhost", database="school",user="postgres",password="angels",port="5432")

cur=con.cursor()

con.autocommit=True

user_table="""create table if not exists students(student_id serial PRIMARY KEY NOT NULL,
                                                first_name VARCHAR NOT NULL,
                                                last_name VARCHAR NOT NULL
                                                )"""
cur.execute(user_table)