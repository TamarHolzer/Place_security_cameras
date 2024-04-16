import pypyodbc as odbc
print("Hi")


conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=DESKTOP-V6585A6\SQLEXPRESS;'
    r'DATABASE=MY_CAMERAS_PROCECT1;'
    r'Trusted_Connection=yes;'
)
conn = odbc.connect(conn_str)
print(conn)


# cursor = conn.cursor()
#
#
# #insert
# cursor.execute('''
#                 INSERT INTO [Person] (id, name, address)
#                 VALUES
#                 (1,'Ari','USA'),
#                 (2,'Yael','Israel')
#                 ''')
# conn.commit()
#
# #select
# # cursor.execute('''
# #                 DELETE FROM [Person]
# #                 WHERE id = 1
# #                ''')
# #
# # conn.commit()
#
# #select
# data = cursor.execute("select * from [Person];")
# for i in cursor:
#     print(i)
