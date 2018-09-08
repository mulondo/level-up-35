import psycopg2

#connect to database
con=psycopg2.connect(host="localhost", database="eventapp",user="postgres",password="angels",port="5432")

cur=con.cursor()

con.autocommit=True

user_table="""create table if not exists Users(user_id serial PRIMARY KEY NOT NULL,
                                                first_name TEXT NOT NULL,
                                                last_name TEXT NOT NULL,
                                                age INT NOT NULL,
                                                email TEXT NOT NULL,
                                                password TEXT NOT NULL,
                                                create_at_DATE
                                                )"""
cur.execute(user_table)

event_table="""create table if not exists Event(event_id serial PRIMARY KEY NOT NULL,
                                                event_name TEXT NOT NULL,
                                                price TEXT NOT NULL,
                                                location INT NOT NULL
                                                )"""
cur.execute(event_table)

Ticket_table="""create table if not exists Ticket(ticket_id serial PRIMARY KEY NOT NULL,
                                                user_id INT,
                                                event_id INT,
                                                is_valid INT,
                                                verification_code BIGINT,
                                                created_at DATE
                                                )"""
cur.execute(Ticket_table)