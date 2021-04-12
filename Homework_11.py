print ("Hello world!")
s = "The Evaporative Air Cooler should not be used in enclosed spaces. It must be kept level and there must be water in the water tank. Doors and windows should be opened to allow free air flow. The Evaporative Air Cooler works best when placed near an open window, so that outside air is drawn into the Evaporative Air Cooler, circulates in the room, then exits via the door."
s2=(s.find("h")+1)
s3=(s.find("h",s2))
s4=(s.rfind("h",))
print (s)
print (s[:s3]+s[s3:s4].replace("h","H")+s[s4:-1])
