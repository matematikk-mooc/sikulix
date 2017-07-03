import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from mmoocutility import *

try:
    print "==="
    print "TC5"
    print "Fjern merk som ferdig."
    print "Prerequisite: TC4"
    
    firefox = App.open("Firefox")
    
    
    click("1498734846726.png")
    
    assert exists("1498734884685.png")
    
    MMOOCPASSED()
except:
    MMOOCFAILED()
    raise
