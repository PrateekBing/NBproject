import mysql.connector
connect = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="users")
cursor = connect.cursor()

def authenticate(username, password):
    cursor.execute("SELECT * FROM accounts WHERE username = %s AND password = %s", (username, password))
    data = cursor.fetchone()
    if data:
        return True
    else:
        return False

def createUser(username, password, DOB):
    cursor.execute("INSERT INTO accounts VALUES (%s, %s, %s)", (username, password, DOB))
    connect.commit()

def showUsers():
    cursor.execute("SELECT * FROM accounts;")
    data = cursor.fetchall()
    for row in data:
        print(row)

def deleteUser(username):
    cursor.execute("DELETE FROM accounts WHERE username = %s", (username,))
    connect.commit()

def forgotPassword(username, password, DOB):
    deleteUser(username)
    createUser(username, password, DOB)

a = 0
while a == 0:
    choice = input("1. Authenticate account \n 2. Create account \n 3. Show accounts \n 4. Delete account \n 5. Forgot Password \n Choose an option: ")
    if choice == "1":
        u_name = input("Enter your username: ")
        pwd = input("Enter your password: ")
        authy = authenticate(u_name, pwd)
        if authy:
            print("Login successful!")
        else:
            print("Wrong username or password. Please try again!")

    elif choice == "2":
        u_name = input("Enter your username: ")
        pwd = input("Enter your password: ")
        dob = input("Enter your DOB: ")
        try:
            createUser(u_name, pwd, dob)
            print("Account created successfully!")
        except:
            print("Username already exists. Please try again!")

    elif choice == "3":
        try:
            showUsers()
        except:
            print("No accounts found. Please try again!")
    
    elif choice == "4":
        u_name = input("Enter the username you want to delete: ")
        try:
            deleteUser(u_name)
            print("Account deleted successfully!")
        except:
            print("Account does not exist. Please try again!")

    elif choice == "5":
        u_name = input("Enter your username: ")
        pwd = input("Enter your new Password: ")
        DOB = input("Enter your DOB: ")
        try:
            forgotPassword(u_name, pwd, DOB)
            print("Password changed successfully!")
        except:
            print("Account does not exist. Please try again!")

    else:
        print("Invalid choice. Please try again!")