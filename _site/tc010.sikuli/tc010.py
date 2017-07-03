import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from mmoocutility import *

try:
    print "==="
    print "TC10"
    print "Complete 1.1.1.c."
    print "Logged into Canvas as test user."
    
    firefox = App.open("Firefox")

 
    Region(308,386,262,174).click("1499072188180.png")
    
    MMOOCWAIT()
    click("1498740516156.png")

    MMOOCWAIT()

    click(Location(804, 1034))
    MMOOCWAIT()

    #Sikulix does not seem to handle dynamic web pages, so use location instead.
    paste(Location(788, 1044),"This is a post from Martin.")
    MMOOCWAIT()

    #Click on publiser svar
    click("1499073584078.png")
    MMOOCWAIT()

    assert exists("1498802910268.png")

    
    MMOOCPASSED()
except:
    MMOOCFAILED()
    raise
