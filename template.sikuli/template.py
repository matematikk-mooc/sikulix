import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from mmoocutility import *

try:    print "==="
    print "TC3"
    print "Klikk på side i indeks."
    print "Prerequisite: TC2"

    firefox = App.open("Firefox")

    MMOOCPASSED()
except:
    MMOOCFAILED()
    raise
    