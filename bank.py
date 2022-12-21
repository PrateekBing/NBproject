import mysql.connector
connect = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="moni")
cursor = connect.cursor()

def authenticate(username, password):
    cursor.execute("SELECT * FROM accounts WHERE username = %s AND password = %s", (username, password))
    data = cursor.fetchone()
    if data:
        return True
    else:
        return False

def createUser(username, password, moni):
    cursor.execute("INSERT INTO accounts VALUES (%s, %s, %s)", (username, password, moni))
    connect.commit()

def showUsers():
    cursor.execute("SELECT * FROM accounts")
    data = cursor.fetchall()
    for row in data:
        print(row)

def addMoney(username, amount):
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE username = %s", (amount, username))
    connect.commit()

def withdrawMoney(username, amount):
    cursor.execute("UPDATE accounts SET balance = balance - %s WHERE username = %s", (amount, username))
    connect.commit()    

def deleteUser(username):
    cursor.execute("DELETE FROM accounts WHERE username = %s", (username,))
    connect.commit()

a = 0
while a == 0:
    choice = input("1. Authenticate account \n 2. Create account \n 3. Show accounts \n 4. Delete account \n 5. Add money \n 6. Withdraw money \n Choose an option: ")
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
        moni = int(input("Enter the amount you want to deposit: "))
        try:
            createUser(u_name, pwd, moni)
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
            print("No account found. Please try again!")

    elif choice == "5":
        u_name = input("Enter your username: ")
        pwd = input("Enter your password: ")
        authy = authenticate(u_name, pwd)
        if authy:
            amount = int(input("Enter the amount you want to add: "))
            addMoney(u_name, amount)
            print("Money added successfully!")
        else:
            print("Wrong username or password. Please try again!")

    elif choice == "6":
        u_name = input("Enter your username: ")
        pwd = input("Enter your password: ")
        authy = authenticate(u_name, pwd)
        if authy:
            amount = int(input("Enter the amount you want to withdraw: "))
            withdrawMoney(u_name, amount)
            print("Money withdrawn successfully!")
        else:
            print("Wrong username or password. Please try again!")

    else:
        print("Invalid option. Please try again!")

    cont = input("Do you want to continue? (y/n): ")
    if cont == "y":
        a = 0
    else:
        a = 1