# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing XML
#
import xml.dom.minidom as xdm   # DOM = Document Object Model

# use the parse() function to load and parse an XML file
doc = xdm.parse("samplexml.xml")

# print out the document node and the name of the first child tag
print(doc.nodeName)
print(doc.firstChild.tagName) # These are standard names in Document Object Model (DOM) 

# get a list of XML tags from the document and print each one
skills = doc.getElementsByTagName("skill")
print("Skill count:", skills.length)
for skill in skills:
  print(skill.getAttribute("name"))
    
# create a new XML tag and add it into the document
new_skill = doc.createElement("skill")
new_skill.setAttribute("name", "JQuery")
doc.firstChild.appendChild(new_skill) # This will put the new skill within the person tag

# Note that the new skill is not written in the .xml file because the code for that is absent
# What happen is that the new skill only exists in the RAM and therefore can be seen in print()

skills = doc.getElementsByTagName("skill")
print("Skill count:", skills.length)
for skill in skills:
  print(skill.getAttribute("name"))

