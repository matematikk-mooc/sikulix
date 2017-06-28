print "==="
print "TC2"
print "Test gå til modul."
print "Prerequisite: TC0"
firefox = App.open("Firefox")

r = Region(672,451,945,173)
r.click("1498205444261.png")
wait(2)
assert exists("1498648790146.png")

print "PASSED"
