import re

#function to call file name for subject

def get_filename(filename):
    with open(filename) as f:
        return f.read()

pattern = r'\.\s(.+):\sDescription:(.+)'
# other patterns to parse with:

# Valid for space_marine_cat.txt:
# 'name="(.+).+(\<.)' finds 2720 results e.g: name="Description" typeId="21befb24-fc85-4f52-a745-64b2e48f8228">After this Warlord makes a charge move, you can select one enemy unit within 1&quot; of this Warlord and roll one D6; on a 2+ that enemy unit suffers 1 mortal wound.</
# '.+type="rule"' finds e.g: common rules - angels of death & explode
# 'description.+' finds 264 results e.g: Description" typeId="21befb24-fc85-4f52-a745-64b2e48f8228">In your command phase, one model from your army with an Orbital comms array that has not been used this battle can use it to call in an orbital barrage. If it does, select one point on the battlefield and roll one D6 for each unit within D6&quot; of that point, subtracting 1 from the result if the unit being roll for is a CHARACTER. On a 4+, that unit suffers D3 mortal wounds</characteristic>
# '(description.+|name.+|rule.+)' finds 9100+ results - any name, rule or description line
# 'profile\sid=".+"\s name=(".+?").+'
# 'name=(".+?")\stypeId=".+"(>.+)<' finds 2720 results e.g: name="Description" typeId="21befb24-fc85-4f52-a745-64b2e48f8228">When you give a model this Relic, select one bolt weapon (see Codex: Space Marines) that model is equipped with. When that model is chosen to shoot with, you can choose for that weapon to fire a quake bolt. If you do, you can only make one attack with that weapon, but if a hit is scored, the target is felled until the end of the turn and the attack sequence continues. When resolving an attack made with a melee weapon against a felled unit, add 1 to the hit roll.<
# 'profile id=".+" name="(.+?)"' finds 654 results e.g: <profile id="17fb-6a10-ec0f-bcd5" name="Quake Bolts"
# 'name=("[^\d{3}].+?")\shidden="false"\stypeId="' Finds 606 "typename=Unit" results

#Valid for Space Marie Extraction.txt:
# '\.\s(.+):\sDescription:(.+)' Should find ability name as group 1 and decription text as group 2

subject = get_filename('Space Marine Extraction.txt')
regex = re.compile(pattern)

######## The six main tasks we're likely to have ########

# Task 1: Is there a match?
#print("*** Is there a Match? ***")
#if regex.search(subject):
#	print ("Yes")
#else:
#	print ("No")

# Task 2: How many matches are there?
print("\n" + "*** Number of Matches ***")
matches = regex.findall(subject)
print(len(matches))

# Task 3: What is the first match?
#print("\n" + "*** First Match ***")
#match = regex.search(subject)
#if match:
#	print("Overall match: ", match.group(0))
#	print("Group 1 : ", match.group(1))
#	print("Group 2 : ", match.group(2))
#	print("Group 3 : ", match.group(3))

# Task 4: What are all the matches?
#print("\n" + "*** All Matches ***\n")
#print("------ Method 1: finditer ------\n")
#for match in regex.finditer(subject):
	#print ("--- Start of Match ---")
	#print("Overall match: ", match.group(0))
	#print("Group 1 : ", match.group(1))
	#print("Group 2 : ", match.group(2))
	#print("Group 3 : ", match.group(3))
	#print ("--- End of Match---\n")

print("\n------ Method 2: findall ------\n")
# if there are capture groups, findall doesn't return the overall match
# therefore, in that case, wrap the pattern in capturing parentheses
# the overall match becomes group 1, so other group numbers are bumped up!
wrappedpattern = "(" + pattern + ")"
wrappedregex = re.compile(wrappedpattern)
matches = wrappedregex.findall(subject)
if len(matches)>0:
	for match in matches:
	    print ("--- Start of Match ---")
	    #print ("Overall Match: ",match[0])
	    print ("Group 1: ",match[1])
	    print ("Group 2: ",match[2])
	    #print ("Group 3: ",match[3])
	    print ("--- End of Match---\n")

# Task 5: Replace the matches
# simple replacement: reverse group
#print("\n" + "*** Replacements ***")
#print("Let's reverse the groups")
#def reversegroups(m):
#	return m.group(3) + ":" + m.group(2) + ":" + m.group(1)
#replaced = regex.sub(reversegroups, subject)
#print(replaced)

# Task 6: Split
#print("\n" + "*** Splits ***")
# Let's split at colons or spaces
#splits = re.split(r">|\"",subject)
#for split in splits:
#	    print (split)
