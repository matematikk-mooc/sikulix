import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from mmoocutility import *

try:
    print "==="
    print "Self register TC3"
    print "Gå til kurs side fra alle tilgjengelig kurs."
    print "Prerequisite: Self register TC2"
    
    firefox = App.open("Firefox")
    
    click("1498726846504.png")
    
    MMOOCWAIT()
    
    assert Region(306,129,793,457).exists("1498823374168.png")
    
    MMOOCPASSED()
except:
    MMOOCFAILED()
    raise