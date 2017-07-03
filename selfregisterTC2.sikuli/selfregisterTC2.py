import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from mmoocutility import *

try:
    print "==="
    print "selfregisterTC2"
    print "Self register in sikuli course."
    print "Prerequisite: TC1 or on empty course overview page."
    
    firefox = App.open("Firefox")
    
    click("1498726666565.png")
    
    wait(5)
    
    click("1498726713071.png")
    
    wait(1)
    
    click("1498726735346.png")
    
    wait(5)
    
    assert exists("1498726765844.png")
    

    MMOOCPASSED()
except:
    MMOOCFAILED()
    raise