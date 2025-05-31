import pymysql

# function to create a connection to the MySQL DB
def create_db_connection():
    return pymysql.connect(
        host="host.docker.internal",      # MySQL server host
        user="root",           # MySQL username
        password="some_password", # MySQL password
        database="demodb"      # MySQL database name
    )

# function to create a table to store if it doesn't exist
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usernames (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255)
        )
    """)
    connection.commit()
    cursor.close()

# function to insert a name into the DB
def insert_name(connection, name):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO usernames (name) VALUES (%s)", (name,))
    connection.commit()
    cursor.close()
    #Insert name into files also
    # with open("server.txt", "a") as file:
        # file.write(name+"\n")

# function to fetch all usernames from the database
def fetch_all_usernames(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM usernames")
    names = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return names

# main function
def main():
    connection = create_db_connection()
    create_table(connection)

    while True:
        print("1. Add a name")
        print("2. Show all usernames")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter a name: ")
            insert_name(connection, name)
            print(f"Name '{name}' added to the database.")
        elif choice == "2":
            usernames = fetch_all_usernames(connection)
            if usernames:
                print("usernames in the database:")
                for name in usernames:
                    print(name)
            else:
                print("No usernames found in the database.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    connection.close()

if __name__ == "__main__":
    main()
