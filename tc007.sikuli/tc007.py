import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from mmoocutility import *

try:
    print "==="
    print "TC7"
    print "Complete first item in module 1."
    print "Logged into Canvas as test user."
    
    firefox = App.open("Firefox")

    click("1498740251250.png")
    wait(5)
    click("1498740264782.png")
    wait(5)

    r = Region(386,492,923,126)
    r.click("1498740318217.png")
    wait(5)
    click("1498740344992.png")
    wait(3) 
    assert exists("1498804516984.png")
    
    
    MMOOCPASSED()
except:
    MMOOCFAILED()
    raise
