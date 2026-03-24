import pyodbc

# --- Configuration ---
server = 'SQLServerName'          # Replace with your school's SQL Server name
database = 'yourdatabase'         # Replace with your specific database name
username = 'your_username'        # Your provided SQL Server login
password = 'your_passphrase'      # Your provided passphrase

# --- Connection String ---
# Note: Driver 18 is standard for modern SSMS, but you may need 'ODBC Driver 17 for SQL Server' 
# if the lab machines are slightly older. 
conn_str = (
    f'DRIVER={{ODBC Driver 18 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
    'Encrypt=yes;'
    'TrustServerCertificate=yes;' 
)

try:
    # Establish connection
    with pyodbc.connect(conn_str) as conn:
        with conn.cursor() as cursor:
            print("Successfully connected to the database!")
            
            # --- Execute a Query ---
            # Replace 'YourTableName' with an actual table in your DB
            query = "SELECT TOP 5 * FROM YourTableName"
            cursor.execute(query)
            
            # Fetch and print results
            rows = cursor.fetchall()
            for row in rows:
                print(row)

except Exception as e:
    print(f"Error: {e}")
