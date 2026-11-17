import pymysql

connection = pymysql.connect(
 host='localhost',
 user='python_app_2',
 password='python@123',  
 database='camerin_students_2j',
 port=3306
)
def get_data():
   query = """ 
            select * from students
            where students_id = 102
            """
   
   cursor.execute(query)
   print(cursor.fetchone())
   

try:
   with connection.cursor() as cursor:
      print("== original data ==")
      print(get_data())


      cursor.execute("""
         update students set city = %s
         where students_id = %s
         """,("delhi",102))


      print("== After update (before commit) ==")
      print(get_data())

      connection.commit()
      print("== after commit ==")
      print(get_data())

      cursor.execute("""
                update students set city = %s
                where students_id = %s
                """,("thrissur",102))


      print("== after second update (before rollback) ==")
      print(get_data())


      connection.rollback()
      print("== after rollback ==")
      print(get_data())


     

except Exception as e:
    print(f"Error occurred: {e}")
finally:
    connection.close()
    print("operation completed")