def check_password(password):
    if len(password) < 8:
        return "Пароль слишком короткий."
    
    if password == "password123":
        return "Пароль слишком простой."
    
    else:
        return "Пароль подходит."
print(check_password("123"))
print(check_password("password123"))
print(check_password("MyStrongPass"))