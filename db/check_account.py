from db.db import *


def check_account(username, password):
    account_info = records(f"SELECT * FROM account_data WHERE Username = '{username}'")
    print(account_info)

    if not account_info:
        commit()
        return False

    if account_info[0][1] == password:
        commit()
        return True
    commit()
    return False
