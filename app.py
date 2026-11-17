import pymysql

connection = pymysql.connect(
 host='localhost',
 user='python_app_2',
 password='python@123',  
 database='camerin_students_2j',
 port=3306
)
print("my sql connection is successful")



# try:
#     # cursur = connection.cursor()
#     with connection.cursor() as cursur:
#         cursur.execute("select * from students")
        # records = cursur.fetchmany(4)
        # records = cursur.fetchall()
        # records = cursur.fetchone()

try: 
    with connection.cursor() as cursor:
        # query = """
        #  ALTER TABLE students
        #  ADD COLUMN phone VARCHAR(15) not null default'111'
        # """
        # cursor.execute(query)
        # print("column created successfully")
        # query = "DESC students"
        # cursor.execute(query)

        # result = cursor.fetchall()
        # for col in result:
        #     print(col)"""

        # query = """
        #     ALTER TABLE students
        #     RENAME COLUMN phone TO contact_num
        # """

        cursor.execute(query)
        connection.commit()
        print("column created successfully")

        query = "DESC students"
        cursor.execute(query)

        result = cursor.fetchall()
        for col in result:
            print(col)

except Exception as e:
    print(f"Error occurred: {e}")
finally:
    connection.close()
    print("operation completed")


        
        # user_input = "' or '1'='1"
        # query = f""" SELECT *
        #             FROM students
        #             where s_name ='{user_input}' """
        # cursur.execute(query)
        # result = cursur.fetchall()
        # print(result)

#SQL INJECTION
    #      username = input()
    #     password = input()
    #     query = f""" 
    #             select * from users 
    #             where username = %s
    #             and password = %S
    # """
    #     cursor.execute(query,(username,password))

    #     query = """ 
    #         insert into students
    #         values(%s,%s,%s,%s)
    #     """

    #     values = (108,"akhil","akhil@gmail.com","kochi")
    #     cursur.execute(query,values)
    # connection.commit()


# update,delete,truncate,drop,insert operation-find difference

# INSERT OPERATION
    # query= """
    #        INSERT INTO students VALUES (%s, %s, %s,%s)
    #        """
    # values = (106, 'akhil','akhil@gmail.com', 'kochi')
    # cursur.execute(query, values)
    # connection.commit()


    # # UPDATE OPERATION
    # query = """
    #         UPDATE students
    #         SET city = %s
    #         WHERE student_id = %s
    #         """
    # values = ('thrissur', 106)
    # cursur.execute(query, values)
    # connection.commit()


    # # DELETE OPERATION
    # query = """
    #         DELETE FROM students
    #         WHERE student_id = %s
    #         """
    # values = (106,)
    # cursur.execute(query, values)
    # connection.commit()


#     # TRUNCATE OPERATION
#     query = """
#             TRUNCATE TABLE students
#             """
#     cursur.execute(query)
#     connection.commit()

          


# hllo worldddd
# joyal