import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from mmoocutility import *

try:
    print "==="
    print "TC6"
    print "Mark several items as done on module page."
    print "Prerequisite: TC5"
    
    firefox = App.open("Firefox")
    
    def tc6part1():
        click("1498734948729.png")
        wait(4)
        click("1498734965919.png")
        wait(4)
        
    
        click("1498735017151.png")
        wait(4)
        click("1498734965919.png")
        wait(4)
        
        
        click("1498735064288.png")
        wait(4)
        click("1498734965919.png")
        wait(4)
    
    
        click("1498823537034.png")
        wait(4)
        click("1498734965919.png")
        wait(4)
    
    
        click("1499065130951.png")
        wait(4)
    
        click("1498734965919.png")
        wait(4)
    
        #Go to course home page to check if progress is updated.
        click("1498735117523.png")
    
        wait(3) 
        assert exists("1498735245897.png")
    
    #Go back to module page to reset to initial state.
    def tc6part2():
        r3 = Region(393,513,60,94)
        #Click on the first item.
        r3.click(Location(363, 578))
    
        wait(3)
         
        click("1498735310873.png")
     
        wait(4)
    
        click("1499065660258.png")
        wait(4)
        click("1498735310873.png")
        wait(4)
    
   
        click(Pattern("1499065642720.png").similar(0.88))
        wait(4)
        click("1498735310873.png")
        wait(4)
    
    
        click("1499065773972.png")
        wait(4)
        click("1498735310873.png")
     
        wait(4)
    
    
        click(Pattern("1499071485692.png").exact())
        wait(4)
        click("1498735310873.png")
        wait(4)

        assert exists(Pattern("1498736608705.png").similar(0.89))
    
    tc6part1()
    tc6part2()
    
    MMOOCPASSED()
except:
    MMOOCFAILED()
    raise
