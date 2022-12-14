import mysql.connector
connect = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="travel")
cursor = connect.cursor()

def addLocations(city, hotel, price):
    cursor.execute("INSERT INTO locations VALUES (%s, %s, %s)", (city, hotel, price))
    connect.commit()

def removeLocations(city):
    cursor.execute("DELETE FROM locations WHERE city = %s", (city,))
    connect.commit()

def showLocations():
    cursor.execute("SELECT * FROM locations")
    data = cursor.fetchall()
    for row in data:
        print(row)

def showHotels():
    cursor.execute("SELECT hotels FROM locations")
    data = cursor.fetchall()
    for row in data:
        print(row)

def showPrices():
    cursor.execute("SELECT price FROM locations")
    data = cursor.fetchall()
    for row in data:
        print(row)

def showCities():
    cursor.execute("SELECT city FROM locations")
    data = cursor.fetchall()
    for row in data:
        print(row)


while True:
    choice = input("1. Add a location \n 2. Remove a location \n 3. Show all locations \n 4. Show all hotels \n 5. Show all prices \n 6. Show all cities \n Choose an option: ")
    if choice == "1":
        city = input("Enter the city: ")
        hotel = input("Enter the hotel: ")
        price = input("Enter the price: ")
        addLocations(city, hotel, price)
        print("Location added successfully!")

    elif choice == "2":
        city = input("Enter the city: ")
        removeLocations(city)
        print("Location removed successfully!")

    elif choice == "3":
        showLocations()

    elif choice == "4":
        showHotels()

    elif choice == "5":
        showPrices()

    elif choice == "6":
        showCities()

    else:
        print("Invalid option. Please try again!")