import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from mmoocutility import *

try:
    print "==="
    print "TC2"
    print "Test gå til modul."
    print "Prerequisite: TC0"
    firefox = App.open("Firefox")

    r = Region(672,451,945,173)
    r.click("1498205444261.png")
    wait(3)
    m = exists("1498733483629.png")
    
    MMOOCPASSED()
except:
    MMOOCFAILED()
    raise