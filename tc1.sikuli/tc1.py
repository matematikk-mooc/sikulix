import sys
sys.stdout.write('.')

print "==="
print "TC1"
print "Test scroll event list."
print "Prerequisite: TC0"

firefox = App.open("Firefox")

assert exists("1498648654043.png")

r = Region(1307,487,325,326)
r.click("1498567843872.png")

r.click("1498567843872.png")
r.click("1498567843872.png")
r.click("1498567843872.png")

assert exists("1498648579716.png")
print "PASSED"
