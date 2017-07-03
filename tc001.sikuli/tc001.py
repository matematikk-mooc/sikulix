import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from mmoocutility import *

try:
    print "==="
    print "TC1"
    print "Test scroll event list."
    print "Prerequisite: On course page."

    firefox = App.open("Firefox")

    assert exists("1498728504578.png")

    r = Region(1307,487,325,326)
    r.click("1498567843872.png")

    r.click("1498567843872.png")
    r.click("1498567843872.png")
    r.click("1498567843872.png")

    assert exists("1498728547765.png")

    MMOOCPASSED()
except:
    MMOOCFAILED()
    raise