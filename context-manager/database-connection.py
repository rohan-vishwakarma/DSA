import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class DatabaseConnection:

    def __init__(self, host, port, username, password, dbname):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._dbname = dbname
        logging.info(f"Initiating Database Connection")


    
    def __enter__(self):
        logging.info("Database Connected")
        return f""
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.info(f"Database Connection Closed")
        return True

    
with DatabaseConnection("localhost", 3306, "rohan", "helo@1234", "finance_db") as connect:
    print(connect)