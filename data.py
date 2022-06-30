import numpy as np
import pandas as pd
import psycopg2

data = pd.read_csv('archive/Books.csv')

data_new = data.dropna()

columns = ['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication']

table_date = data_new[columns]
table_date = table_date.iloc[:, :].values


def connectDB(isbn_no, title, author, year):
    conn = None
    try:
        conn = psycopg2.connect(host='localhost',
                                database='LIBRARY',
                                user='postgres',
                                password="Ram@446177",
                                port='5432')
        curr = conn.cursor()
        isbn_no, title, author, year = data
        curr.execute(f"INSERT INTO books (isbn_no,book_title,book_author,year_of_publication) VALUES (%s,%s,%s,%s)",
                     (isbn_no, title, author, year))
        conn.commit()
        print('Number of rows affected: ', curr.rowcount)
        curr.close()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


for data in table_date:
    isbn_no, title, author, year = data
    connectDB(isbn_no=isbn_no, title=title, author=author, year=year)
    print('Successfully added')
