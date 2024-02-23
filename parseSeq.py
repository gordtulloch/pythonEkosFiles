import xmltodict

# Parse XML from a template to a Dict
inFile=open('test.esq','r')
xmlText=inFile.read()
xmlDict=xmltodict.parse(xmlText)

# Modify what we need to in the Dict structure
jobDict=xmlDict["SequenceQueue"]["Job"]
print(len(jobDict))
jobDict.append(jobDict[6])
print(len(jobDict))
    
'''xmlDict["SequenceQueue"]["Job"][0]["Exposure"]=10
print(xmlDict["SequenceQueue"]["Job"][0])
print(xmlDict["SequenceQueue"]["Job"][1])
xmlDict["SequenceQueue"]["Job"][1]=xmlDict["SequenceQueue"]["Job"][0]
print(xmlDict["SequenceQueue"]["Job"][1])'''
inFile.close()

# Write the result to a new XML file
#outFile=open('output.esq','w')
#outFile.write(unparse(xmlDict, pretty=True))
#outFile.close()