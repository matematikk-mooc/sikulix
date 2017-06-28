print "==="
print "TC4"
print "Merk som ferdig."
print "Prerequisite: TC3"

firefox = App.open("Firefox")

r = Region(708,202,1116,913)

r.click("1498214140585.png")
assert exists("1498214157651.png")

print "PASSED"