import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from mmoocutility import *

try:
    print "==="
    print "TC9"
    print "Complete 1.1.1.b."
    print "Logged into Canvas as test user."
    
    firefox = App.open("Firefox")

    click("1498740397121.png")
    wait(3)
    click("1498740344992.png")
    wait(3)
    assert exists("1498804634062.png")
    
    
    MMOOCPASSED()
except:
    MMOOCFAILED()
    raise
