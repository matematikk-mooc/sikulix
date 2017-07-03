import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from mmoocutility import *

try:
    print "==="
    print "Selfregister TC1"
    print "Self register the user Martin"
    print "Prerequisite: The user martin@erlendthune.com should not exist"
    
    firefox = App.open("Firefox")
    
    click("1498737210514.png")
    
    wait(2)
    
    
    paste(Pattern("1498737272828.png").similar(0.90), "martin@erlendthune.com")
    
    type(Key.TAB + "Martin Jaklin" + Key.ENTER)

    wait(1)
    
    click("1498737591941.png")
    
    click("1498737474865.png")
    
    wait(3)
    
    assert exists("1498720604456.png")
    

    MMOOCPASSED()
except:
    MMOOCFAILED()
    raise
    