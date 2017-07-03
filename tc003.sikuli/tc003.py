import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from mmoocutility import *

try:
    print "==="
    print "TC3"
    print "Klikk på side i indeks."
    print "Prerequisite: TC2"

    firefox = App.open("Firefox")

    click("1498821033179.png")

    wait(5)
    assert exists("1498821072938.png")
    MMOOCPASSED()
except:
    MMOOCFAILED()
    raise
    