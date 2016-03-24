from lib.logger import LogConfig
from app import Main, Other

log = LogConfig()
app = Main()
app.do_something()

app2 = Other()
app2.do_something()

