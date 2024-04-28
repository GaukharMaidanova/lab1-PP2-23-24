import psycopg2
import csv
import os

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(dbname="suppliers", user="postgres", password="postgres", host="localhost")
cursor = conn.cursor()

# Create the PhoneBook database and Contacts table
def create_database_and_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Contacts (id SERIAL PRIMARY KEY, username TEXT NOT NULL, phone TEXT NOT NULL);")
    conn.commit()

# Insert data into the Contacts table from CSV file
def insert_data_from_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                username, phone = row
                cursor.execute("INSERT INTO Contacts (username, phone) VALUES (%s, %s);", (username, phone))
        conn.commit()
    except FileNotFoundError:
        print(f"File not found: {file_path}. Please check the file path and try again.")

# Insert data into the Contacts table from the console
def insert_data_from_console():
    username = input("Enter the username: ")
    phone = input("Enter the phone number: ")
    cursor.execute("INSERT INTO Contacts (username, phone) VALUES (%s, %s);", (username, phone))
    conn.commit()

# Update data in the Contacts table
def update_data():
    username = input("Enter the username to update: ")
    new_username = input("Enter the new username (leave blank to skip): ")
    new_phone = input("Enter the new phone number (leave blank to skip): ")

    if new_username:
        cursor.execute("UPDATE Contacts SET username = %s WHERE username = %s;", (new_username, username))
    if new_phone:
        cursor.execute("UPDATE Contacts SET phone = %s WHERE username = %s;", (new_phone, username))

    conn.commit()

# Query data from the Contacts table with filters
def query_data():
    filter_choice = input("Filter by (username/phone): ").strip().lower()
    filter_value = input(f"Enter the {filter_choice} to filter by: ")

    query = f"SELECT * FROM Contacts WHERE {filter_choice} = %s;"
    cursor.execute(query, (filter_value,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

# Delete data from the Contacts table by username or phone
def delete_data():
    delete_choice = input("Delete by (username/phone): ").strip().lower()
    delete_value = input(f"Enter the {delete_choice} to delete: ")

    query = f"DELETE FROM Contacts WHERE {delete_choice} = %s;"
    cursor.execute(query, (delete_value,))
    conn.commit()

file_path = "C:\\Users\\Gauhar\\suppliers\\file.csv"
# Main function
def main():
    create_database_and_table()
    insert_data_from_csv(file_path)
    insert_data_from_console()
    update_data()
    #query_data()
    # delete_data()

    # Close the connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()