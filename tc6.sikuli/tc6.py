print "==="
print "TC6"
print "Mark several items as done on module page."
print "Prerequisite: TC5"

firefox = App.open("Firefox")
r = Region(386,261,324,967)
r2 = Region(653,264,921,242)

def tc6part1():
    r.click("1498559617479.png")
    wait(2)
    r2.click("1498559454749.png")
    wait(2)
    

    r.click("1498559761107.png")
    wait(2)
    r2.click("1498559454749.png")
    wait(2)
    
    
    r.click("1498559864146.png")
    wait(2)
    r2.click("1498559454749.png")
    wait(2)



    r.click("1498560028777.png")
    wait(2)
    r2.click("1498559454749.png")
    wait(2)


    r.click("1498560056575.png")
    wait(2)
    r2.click("1498559454749.png")

    wait(2)

    #Go to course home page to check if progress is updated.
    Region(430,194,247,212).click("1498560432242.png")

    wait(3) 
    assert exists("1498562925840.png")

#Go back to module page to reset to initial state.
def tc6part2():
    r3 = Region(429,468,101,183)
    r3.click(Pattern("1498560518303.png").exact())

    wait(3)
     
    r2.click("1498560627202.png")
 
    wait(2)

    r.click("1498564614022.png")
    wait(2)
    r2.click("1498560627202.png")
    wait(2)


    r.click("1498561068950.png")
    wait(2)
    r2.click("1498560627202.png")
    wait(2)


    r.click("1498561312510.png")
    wait(2)
    r2.click("1498560627202.png")

    wait(2)


    r.click("1498561374993.png")
    wait(2)
    r2.click("1498560627202.png")
    wait(2)


tc6part1()
tc6part2()

print "PASSED"