print "==="
print "Admin TC1"
print "Enable self register for a course."
print "Prerequisite: On course settings page."

firefox = App.open("Firefox")
wheel(Location(1332, 385), WHEEL_UP , 20)

wait(1)
click("1498723067654.png")

click("1498721926526.png")
click(Pattern("1498723364359.png").exact())
wait(1)
click(Pattern("1498723319202.png").exact())
wheel(Location(1332, 385), WHEEL_UP , 30)

m = find("1498723729665.png")

click(m.getTarget())

wait(5)

assert exists("1498722056575.png")


print "PASSED"