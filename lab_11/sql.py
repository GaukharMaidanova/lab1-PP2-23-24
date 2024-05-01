import psycopg2
import csv

# Database connection parameters
db_params = {
    'dbname': 'suppliers',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

# Connect to the PostgreSQL database
conn = psycopg2.connect(**db_params)
conn.autocommit = True
cur = conn.cursor()

# Step 1: Create the PhoneBook database (if not already created)
try:
    cur.execute("CREATE DATABASE PhoneBook")
except psycopg2.errors.DuplicateDatabase:
    print("PhoneBook database already exists")

# Reconnect to the PhoneBook database
db_params['dbname'] = 'PhoneBook'
conn = psycopg2.connect(**db_params)
conn.autocommit = True
cur = conn.cursor()

# Step 2: Create the Contacts table
cur.execute("""
CREATE TABLE IF NOT EXISTS Contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE
)
""")

# Step 3: Implementing functions and stored procedures

# Function to return records based on a pattern
cur.execute("""
CREATE OR REPLACE FUNCTION search_contacts(pattern VARCHAR)
RETURNS TABLE (id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT Contacts.id, Contacts.name, Contacts.phone
    FROM Contacts
    WHERE Contacts.name ILIKE '%' || pattern || '%'
       OR Contacts.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
""")

# Procedure to insert new user or update phone if user already exists
cur.execute("""
CREATE OR REPLACE PROCEDURE upsert_user(new_name VARCHAR, new_phone VARCHAR)
AS $$
BEGIN
    PERFORM id FROM Contacts WHERE name = new_name;

    IF FOUND THEN
        UPDATE Contacts
        SET phone = new_phone
        WHERE name = new_name;
    ELSE
        INSERT INTO Contacts (name, phone)
        VALUES (new_name, new_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;
""")

# Procedure to insert many new users using JSONB
cur.execute("""
CREATE OR REPLACE FUNCTION bulk_insert_users(new_users JSONB)
RETURNS TABLE (name VARCHAR, phone VARCHAR, error VARCHAR) AS $$
DECLARE
    user JSONB;
    new_name VARCHAR;
    new_phone VARCHAR;
    phone_length INT := 10; -- Adjust the expected phone number length as needed
    is_valid BOOLEAN;
BEGIN
    FOR user IN SELECT * FROM jsonb_array_elements(new_users)
    LOOP
        new_name := user->>'name';
        new_phone := user->>'phone';
        
        -- Check the phone number format (only digits and correct length)
        is_valid := new_phone ~ '^\d+$' AND length(new_phone) = phone_length;
        
        IF is_valid THEN
            -- Check if the user already exists based on name
            IF EXISTS (SELECT 1 FROM Contacts WHERE name = new_name) THEN
                -- Update the phone number if the user exists
                UPDATE Contacts
                SET phone = new_phone
                WHERE name = new_name;
            ELSE
                -- Insert a new user if the user does not exist
                INSERT INTO Contacts (name, phone)
                VALUES (new_name, new_phone);
            END IF;
        ELSE
            -- Return incorrect data with an error message
            RETURN QUERY
            SELECT new_name, new_phone, 'Invalid phone number' AS error;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
""")

# Function to query data from tables with pagination
cur.execute("""
CREATE OR REPLACE FUNCTION paginate_contacts(limit_value INT, offset_value INT)
RETURNS TABLE (id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT Contacts.id, Contacts.name, Contacts.phone
    FROM Contacts
    ORDER BY Contacts.id
    LIMIT limit_value OFFSET offset_value;
END;
$$ LANGUAGE plpgsql;

""")

# Procedure to delete data from tables by username or phone
cur.execute("""
CREATE OR REPLACE PROCEDURE delete_user(target_name VARCHAR, target_phone VARCHAR)
AS $$
BEGIN
    IF target_name IS NOT NULL THEN
        DELETE FROM Contacts
        WHERE name = target_name;
    END IF;

    IF target_phone IS NOT NULL THEN
        DELETE FROM Contacts
        WHERE phone = target_phone;
    END IF;
END;
$$ LANGUAGE plpgsql;
""")

# Step 4: Implementing CSV file uploading

def upload_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            name, phone = row
            cur.execute("INSERT INTO Contacts (name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING", (name, phone))
    print(f"CSV data uploaded from {file_path}")

# Step 5: Providing code for entering user data from the console

def enter_user_data():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO Contacts (name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING", (name, phone))
    print(f"Added user: {name}, Phone: {phone}")

# Usage example
def main():
    # Upload data from CSV file
    upload_csv('C:\\Users\\Gauhar\\suppliers\\file.csv')
    
    # Enter user data from console
    enter_user_data()
    
    # Search contacts based on a pattern
    pattern = input("Enter a pattern to search: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    results = cur.fetchall()
    print("Search results:")
    for result in results:
        print(result)
    
    # Use pagination to query data
    limit_value = int(input("Enter limit for pagination: "))
    offset_value = int(input("Enter offset for pagination: "))
    cur.execute("SELECT * FROM paginate_contacts(%s, %s)", (limit_value, offset_value))
    paginated_results = cur.fetchall()
    print("Paginated results:")
    for result in paginated_results:
        print(result)
    
    # Deleting data by username or phone
    delete_name = input("Enter name to delete (or leave blank): ")
    delete_phone = input("Enter phone to delete (or leave blank): ")
    cur.execute("CALL delete_user(%s, %s)", (delete_name, delete_phone))
    print(f"Deleted records for name: {delete_name} and phone: {delete_phone}")

# Run the script
if __name__ == "__main__":
    main()

# Close the connection
cur.close()
conn.close()