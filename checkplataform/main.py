#LEARNED HOW TO INTERACT WITH COMPUTER TO RECIEVE INFORMATION ABOUT HARDWARE AND SOFTWARE

import getpass
import platform
from datetime import datetime

print(platform.node())
print(platform.architecture())
print(platform.system())
print(platform.release())
print(platform.processor())
print(platform.python_version())

print(datetime.now().year)

print(getpass.getuser())