import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from mmoocutility import *

try:
    print "==="
    print "Login TC1"
    print "Login to Canvas."
    print "Prerequisite: Self register TC1. martin@erlendthune.com must exist."
    
    firefox = App.open("Firefox")
    
    
    MMOOCPASSED()
except:
    MMOOCFAILED()
