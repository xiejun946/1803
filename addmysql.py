import pymysql.cursors
#import datetime
domains=[kj;lk

]

insert_table_sql="""
SELECT id FROM gc_set
"""
query_table_sql="""
SHOW DATABASES
"""

for domain in domains:
    datalists=[]
    connection=pymysql.connect(
    host=domain,
    user='root',
    password='kWln94we2P3R3',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:        
            cursor.execute(query_table_sql)
            databases=cursor.fetchall()
            #print(databases)
            for database in databases:
                #print(database.get('Database'))
                datalists.append(database.get('Database'))               
          
    finally:
        connection.close()
    #得到每个实例中数据库表    
    #print(datalists)
    for db in datalists[6:]:
        #print(db)
        connection=pymysql.connect(
        host=domain,
        user='root',
        password='kWln94we2P3R3',
        db=db,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
        #建立mysql连接执行插入语句
        try:
            with connection.cursor() as cursor:

                cursor.execute(insert_table_sql)
                connection.commit()
                #result = cursor.fetchall()
                #print(result)
                
        except:
            pass

        finally:
            connection.close()            
