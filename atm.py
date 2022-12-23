import mysql.connector
import random
connect = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="moni")
cursor = connect.cursor()

def authenticatePin(cardNumber, pin):
    cursor.execute("SELECT * FROM card WHERE number = %s AND pin = %s", (cardNumber, pin))
    return cursor.fetchone()

def getBalance(cardNumber):
    cursor.execute("SELECT balance FROM card WHERE number = %s", (cardNumber,))
    return cursor.fetchone()[0]

def updateBalance(cardNumber, balance):
    cursor.execute("UPDATE card SET balance = %s WHERE number = %s", (balance, cardNumber))
    connect.commit()

a = 0
while a == 0:
    print("1. Create an account \n 2. Log into account \n 0. Exit")
    choice = int(input())
    if choice == 1:
        cardNumber = "400000" + str(random.randint(1, 999))
        pin = str(random.randint(1000, 9999))
        print("Your card has been created")
        print("Your card number:")
        print(cardNumber)
        print("Your card PIN:")
        print(pin)
        cursor.execute("INSERT INTO card (number, pin) VALUES (%s, %s)", (cardNumber, pin))
        connect.commit()
    elif choice == 2:
        print("Enter your card number:")
        cardNumber = input()
        print("Enter your PIN:")
        pin = input()
        if authenticatePin(cardNumber, pin):
            print("You have successfully logged in!")
            while True:
                print("1. Check balance \n 2. Add or withdraw \n 2. Log out")
                choice = int(input())
                if choice == 1:
                    print("Balance: " + str(getBalance(cardNumber)))
                elif choice == 2:
                    print("1. Add \n 2. Withdraw")
                    choice = int(input())
                    if choice == 1:
                        print("Enter the amount you want to add:")
                        amount = int(input())
                        updateBalance(cardNumber, getBalance(cardNumber) + amount)
                        print("Balance: " + str(getBalance(cardNumber)))
                    elif choice == 2:
                        print("Enter the amount you want to withdraw:")
                        amount = int(input())
                        updateBalance(cardNumber, getBalance(cardNumber) - amount)
                        print("Balance: " + str(getBalance(cardNumber)))
        else:
            print("Wrong card number or PIN!")
    