from client.app import start_client
from common.database.json_database import jsonDatabase
from common.database.mysql_database import mysqlDatabase
from common.database.database_abstraction_layer import Dbal
import os

if __name__ == "__main__":
    mysql_db = mysqlDatabase(
        host="localhost", username="root", password="", database="exchangegram"
    )
    json_db = jsonDatabase(path=os.path.join(os.getcwd(), "data"))
    dbal = Dbal(mysql_db)
    start_client(dbal)