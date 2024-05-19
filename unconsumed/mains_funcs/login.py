from unconsumed.connecting_funcs import signin
from unconsumed.DTO import users as user


def login(myUser, isSignin):
    #to serve SQL
    if isSignin == True:
        signin.signin(myUser)
    else:
        signin.login(myUser)


print(23)
t = login(user.users("Ysrael", "y123"), False)
t = t + "...."
print()
###לא מציג את המשתמש למרות שהוא קיים במערכת לבדוק את זה!!!