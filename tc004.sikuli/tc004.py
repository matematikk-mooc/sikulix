import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from mmoocutility import *

try:
    print "==="
    print "TC4"
    print "Merk som ferdig."
    print "Prerequisite: TC3"
    
    firefox = App.open("Firefox")
    
    
    click("1498734759112.png")
    assert exists("1498734769523.png")
    
    MMOOCPASSED()
except:
    MMOOCFAILED()
    raise
    
    