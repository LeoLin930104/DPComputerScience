from client.app import start_client
from common.database.json_database import jsonDatabase
from common.models.user import User
import os

if __name__ == "__main__":
    # start_client()
    db = jsonDatabase(path=os.path.join(os.getcwd(), "data"))
    # names = [
    #     "testA",
    #     "testB",
    #     "testC",
    #     "testD",
    # ]
    # for n in names:
    #     u = User(username=n, email=f"{n}@{n}.com", password_hash=n)

    #     db.create_user(u)
    # db._save_users()