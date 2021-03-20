from gui.main.operation import Operation
from gui.account.menu import Menu
from gui.account.login import Login
from db import db

db.build()
app = Operation()
app.mainloop()
