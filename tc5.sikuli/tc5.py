print "==="
print "TC5"
print "Fjern merk som ferdig."
print "Prerequisite: TC4"

firefox = App.open("Firefox")

r = Region(722,198,1125,923)

r.click("1498214243590.png")

assert exists("1498214266181.png")

print "PASSED"