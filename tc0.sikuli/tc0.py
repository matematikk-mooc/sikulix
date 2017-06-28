#Prerequisites for this script is that you should open the following course page:
#https://ikt.instructure.com/courses/62 in Firefox.
print "==="
print "TC0"
print "Test course home page."
print "Prerequisite: None"

firefox = App.open("Firefox")
type("l", KeyModifier.CMD)
paste("https://ikt.instructure.com/courses/62")
type(Key.ENTER)
assert exists("1498212833530.png")
print "PASSED"