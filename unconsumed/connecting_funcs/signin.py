import ConnectingToSql as sql
from unconsumed.DTO import users as user


def is_it_correct_name(text):
#בדיקת תקינות השם
    return all(char.islower() or char.isupper() or char == '-' or char == '_' or char.isdigit() for char in text)


def is_it_correct_pass(text):
#בדיקת תקינות הסיסמא
    return len(text) >= 4 and all(char.islower() or char.isupper() or char.isdigit() for char in text)


def is_exsist_name(name):
    #בדיקה האם קיים השם במערכת
    acceptedUser = sql.select_user_by_name(name)
    if(user != None ):
        return acceptedUser
    else:
        return None



def signin(myUser):
    #הרשמה ראשונית
    if isinstance(myUser, user.users):
        #הגבלות לשם משתמש: שיכיל אותיות תמספרים _ או -
        #הגבלות לסיסמא: אותיות או מספרים בלבד חובה שיהיה ארוך מ-4 תווים

        #בדיקה תקינות השם והסיסמא

        if is_exsist_name(myUser.user_name != None):
            return (None, "Username is taken Choose another name")


        elif(is_it_correct_name(myUser.user_name) == False):
            return ("e_n", "error: The username you typed is incorrect.\n Username can only contain letters, numbers, underscore or hyphen")
        elif(is_it_correct_pass(myUser.user_password) == False):
            return ("e_p", "error: The passwor you typed is incorrect.\n password can only contain letters or numbers")
        #שליחה להכנסת הנתונים לSQL
        else:
            return (sql.insert_new_user(myUser.user_name, myUser.user_password), "sucssed")
    else:
        return ("e_t", "type error")

def login(myUser):
    if isinstance(myUser, user.users):
        if (is_it_correct_name(myUser.user_name) == False):
            return ("e_n",
                    "error: The username you typed is incorrect.\n Username can only contain letters, numbers, underscore or hyphen")
        elif (is_it_correct_pass(myUser.user_password) == False):
            return ("e_p", "error: The passwor you typed is incorrect.\n password can only contain letters or numbers")
        elif is_exsist_name(myUser.user_name) == False:
            return (None, "User does not exist in the system")
        else:
            acceptedUser = sql.select_user_by_name(myUser.user_name)
            #print(1)

            #print(acceptedUser.user_name+" "+acceptedUser.user_password)
            #print(myUser.user_name+" "+myUser.user_password)
            if(acceptedUser.user_password == myUser.user_password):
                return (acceptedUser)
            else:
                return (None, "wrong password")
    else:
        return ("e_t", "type error")

#u = user.users("Yuval", "yuvalh")
#print(login(u))