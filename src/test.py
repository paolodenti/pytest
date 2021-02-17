import time
import os

import colored
from colored import stylize

msg = os.environ.get("IOHUB_MSG", "No message defined")

while (True):
    print(stylize(msg, colored.fg("green")))
    time.sleep(2)