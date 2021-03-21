from gui.main.operation import Operation
from db import db

version = "0.0.2"

db.build()
app = Operation()
app.mainloop()
