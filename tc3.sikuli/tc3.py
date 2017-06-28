print "==="
print "TC3"
print "Klikk på side i indeks."
print "Prerequisite: TC2"

firefox = App.open("Firefox")

r = Region(439,269,209,557)
r.click("1498648879841.png")
wait(2)

assert r.exists("1498648893801.png")

print "PASSED"