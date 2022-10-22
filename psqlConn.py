import psycopg2 #importing psql library 

host = "localhost"
port ="5432"
user = "postgres"
password = "postgres"
database = "mydata"

def con():
    try:
        conn = psycopg2.connect(database=database,host=host,port=port,
                                user=user, password=password)
        print("conneted....")
        
    except:
        print("cannot connect to database ")

    try:
        #cursor object to help execute queries 
        cursor = conn.cursor()
        #insert data into database table
        insert_query = "insert into friends (name,number) values('john','3430')"
        #execute query
        cursor.execute(insert_query)
        #commit data
        conn.commit()
        #delete query
        delete_query = "delete from friends where name ='john errtnike'"
        # execute query
        cursor.execute(delete_query)
        # commit data
        conn.commit()
        # query to select from database table 
        select_query = ("select * from friends")
        cursor.execute(select_query)
        #fetching data...'fetchone() to get the first data
        #'fetchall()' to get all data
        # 'fetchmany()' to get a particular amount of data i.e fetchmany(size=5)
        print(cursor.fetchall())
    except:
        print("error performing operations")

con()


