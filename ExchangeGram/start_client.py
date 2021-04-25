from client.app import start_client
from common.database.json_database import jsonDatabase
from common.database.mysql_database import mysqlDatabase
from common.database.database_abstraction_layer import Dbal
import os

if __name__ == "__main__":
    # db = mysqlDatabase(
    #     host="localhost", username="root", password="", database="exchangegram"
    # )
    db = jsonDatabase(path=os.path.join(os.getcwd(), "data"))
    dbal = Dbal(db)
    start_client(dbal)
    # names = ["testA", "testB", "testC", "testD"]
    # for n in names:
    #     dbal.register(username=n, email=f"{n}@{n}.com", password=n)
    #     dbal.add_post(user_id=n, content=f"Random Content from {n}")
    #     dbal.add_comment(post_id=n, user_id=n, content="Random Content")
    #     dbal.authenticate(username=n, password=n)
