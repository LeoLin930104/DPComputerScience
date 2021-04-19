from client.app import start_client
from common.database.json_database import jsonDatabase
from common.database.database_abstraction_layer import Dbal
from common.models.User import User
import os

if __name__ == "__main__":
    # start_client()
    db = jsonDatabase(path=os.path.join(os.getcwd(), "data"))
    dbal = Dbal(db)
    names = ["testA", "testB", "testC", "testD"]
    for n in names:
        dbal.signup(username=n, email=f"{n}@{n}.com", password=n)
        dbal.add_post(user_id=n, content=f"Random Content from {n}")
