import re

#function to call file name for subject

def get_filename(filename):
    with open(filename) as f:
        return f.read()

#def give_filename(filename):
#  to add

pattern = r'\.\s(.+):\sDescription:(.+)'
# other patterns to parse with:

#Valid for current Space Marie Extraction.txt:
# '\.\s(.+):\sDescription:(.+)' Should find ability name as group 1 and decription text as group 2

subject = get_filename('Space Marine Extraction.txt')
regex = re.compile(pattern)

# Task: How many matches are there?
print("\n" + "*** Number of Matches ***")
matches = regex.findall(subject)
print(len(matches))

print("\n------ Method 2: findall ------\n")
wrappedpattern = "(" + pattern + ")"
wrappedregex = re.compile(wrappedpattern)
matches = wrappedregex.findall(subject)
if len(matches)>0:
	for match in matches:
	    print ("{")
	    #print ("Overall Match: ",match[0])
	    print ("  name: `",match[1],"`,")
	    print ("  desc: `",match[2],"`,")
	    #print ("Group 3: ",match[3])
	    print ("  when: [add_phase],\n},")

# Task: Replace the matches
# simple replacement: reverse group
#print("\n" + "*** Replacements ***")
#print("Let's reverse the groups")
#def reversegroups(m):
#	return m.group(3) + ":" + m.group(2) + ":" + m.group(1)
#replaced = regex.sub(reversegroups, subject)
#print(replaced)
