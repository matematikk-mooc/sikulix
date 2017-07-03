import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from mmoocutility import *

try:
    print "==="
    print "TC8"
    print "Complete second item in module 1."
    print "Logged into Canvas as test user."
    
    firefox = App.open("Firefox")

    Region(295,202,303,305).click("1499072071057.png")
    wait(3)
    click("1498740344992.png")
    wait(3)
    assert Region(291,217,282,301).exists("1499071944755.png")
    
    
    MMOOCPASSED()
except:
    MMOOCFAILED()
    raise
