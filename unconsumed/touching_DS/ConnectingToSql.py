import pypyodbc as odbc
import unconsumed.DTO.users as user

# פונקצית החיבור לDB
conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=DESKTOP-V6585A6\SQLEXPRESS;'
    r'DATABASE=SECURITY_CAMERA_PROJECT;'
    r'Trusted_Connection=yes;'
)


###############################################################user
# new user
def insert_new_user(myUser):
    if isinstance(myUser, user.users):
        conn = odbc.connect(conn_str)
        cursor = conn.cursor()
        # insert new user

        try:
            name = myUser.user_name
            password = myUser.user_password
            cursor.execute(f'''INSERT INTO [users] (user_name, user_password)
                            VALUES
                           ('{name}', '{password}')
                           ''')
            conn.commit()
            return ("User successfully added")

        except:
            return ("Add failed")
    else:
        return ("object error")


def select_user_by_name(name):
    try:
        try:
            conn = odbc.connect(conn_str)
            cursor = conn.cursor()
        except:
            return ("The process failed to fetch from the database please check the connection.")
        cursor.execute(f"SELECT * FROM users WHERE user_name = '{name}';")
        # יצירת האוביקט והחזרתו
        data = cursor.fetchone()
        accepted_user = user.users(data[1], data[2])
        accepted_user.user_name = accepted_user.user_name.__str__().rstrip()
        accepted_user.user_password = accepted_user.user_password.__str__().rstrip()
        return accepted_user
    except:
        return None


d = select_user_by_name("Meira")
#print()
# print(conn)
#
#
# cursor = conn.cursor()

# #insert
# cursor.execute('''
#                 INSERT INTO [Person] (id, name, address)
#                 VALUES
#                 (1,'Ari','USA'),
#                 (2,'Yael','Israel')
#                 ''')
# conn.commit()
#
# #delete
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
