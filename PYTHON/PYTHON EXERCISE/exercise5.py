username = input("Enter your username :- ")
password = input("Enter your password :- ")

if username == "admin" and password == "secret123":
    print("Login Successful! Welcome Admin.")
else:
    print("Invalid Credentials, Access Denied!")