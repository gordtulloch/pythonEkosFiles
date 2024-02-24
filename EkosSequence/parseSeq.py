import xmltodict

# Parse XML from a template to a Dict
inFile=open('test.esq','r')
xmlText=inFile.read()
xmlDict=xmltodict.parse(xmlText)
inFile.close()

# Copy the Job part of the dictionary
jobDict=xmlDict["SequenceQueue"]["Job"]

# Modify what we need to in the Dict structure
#  First two jobs are there already just edit it
print(jobDict[0])
print(jobDict[1])

# Subsequent jobs need to be added with .append
jobDict.append(jobDict[0])

# Load jobDict into xmlDict
xmlDict["SequenceQueue"]["Job"]=jobDict

# Write the result to a new XML file
outFile=open('output.esq','w')
outFile.write(xmltodict.unparse(xmlDict, pretty=True))
outFile.close()