import psycopg2

book_name = input("Enter the name of the book you want: ")


def selectRow(book_name):
    conn = None
    try:
        conn = psycopg2.connect(host='localhost',
                                database='LIBRARY',
                                user='postgres',
                                password="Ram@446177",
                                port='5432')
        curr = conn.cursor()
        curr.execute(f'''
                SELECT * FROM books
                WHERE book_title = '{book_name}'
                ''')
        conn.commit()
        rows = curr.fetchall()

        if rows is None:
            print('Sorry not available')
        else:
            for row in rows:
                print(row)


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


selectRow(book_name)
