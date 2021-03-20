from db.db import *


def create_account(username, password, email, avatar):
    execute(f"INSERT INTO account_data VALUES ('{username}', '{password}', '{email}', '{avatar}', '0', '0')")
    commit()
