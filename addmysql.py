import pymysql.cursors
#import datetime
domains=['xjpyc01rds.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'xjpyc02rds.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'xjpyc03rds.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'xipyc04rds.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'yicairds05.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'yicairds06.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'yicairds07.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'yicairds08.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'yicairds09.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'yicairds10.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'yicairds11.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'yicairds12.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'yicairds13.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'yicairds14.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'yicairds15.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'yicairds16.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'yicairds17.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'yicairds18.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
'yicairds19.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com'
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
