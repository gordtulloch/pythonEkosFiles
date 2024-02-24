import xmltodict

class EkosSequence:
    xmlText=''
    def __init__(self,inputFile):
        self.inFile=open(inputFile,'r')
        self.xmlText=self.inFile.read()
        self.xmlDict=xmltodict.parse(self.xmlText)
        self.jobList=self.xmlDict["SequenceQueue"]["Job"]
        self.templateJob=self.jobList[0]
        self.inFile.close()

    ######################################################################
    # Getters and setters
    #   GuideDeviation enabled="false">2</GuideDeviation>
    def getGuideDeviation():
        return self.xmlDict["SequenceQueue"]["GuideDeviation"]
        pass
    def setGuideDeviation(Enable,Text):
        self.xmlDict["SequenceQueue"]["GuideDeviation"]['@enabled'] = Enable
        self.xmlDict["SequenceQueue"]["GuideDeviation"]["#text"]    = Text
        return
	#   GuideStartDeviation enabled="false">2</GuideStartDeviation>
    def getGuideStartDeviation():
        return self.xmlDict["SequenceQueue"]["GuideStartDeviation"]
        pass
    def setGuideStartDeviation(Enable,Text):
        self.xmlDict["SequenceQueue"]["GuideStartDeviation"]['@enabled'] = Enable
        self.xmlDict["SequenceQueue"]["GuideStartDeviation"]["#text"]    = Text
        return
	#   HFRCheck enabled="false">
	#	    <HFRDeviation>0.5</HFRDeviation>
	#	    <HFRCheckAlgorithm>0</HFRCheckAlgorithm>
	#	    <HFRCheckThreshold>10</HFRCheckThreshold>
	#	    <HFRCheckFrames>1</HFRCheckFrames>
    def getHFRCheck():
        return self.xmlDict["SequenceQueue"]["HFRCheck"]
    def setHFRCheck(Enable,HFRDeviation,HFRCheckAlgorithm,HFRCheckThreshold,HFRCheckFrames):
        self.xmlDict["SequenceQueue"]["HFRCheck"]['@enabled']=Enable
        self.xmlDict["SequenceQueue"]["HFRCheck"]["HFRDeviation"]=HFRDeviation
        self.xmlDict["SequenceQueue"]["HFRCheck"]["HFRCheckAlgorithm"]=HFRCheckAlgorithm
        self.xmlDict["SequenceQueue"]["HFRCheck"]["HFRCheckThreshold"]=HFRCheckThreshold
        self.xmlDict["SequenceQueue"]["HFRCheck"]["HFRCheckFrames"]=HFRCheckFrames
        return
    #   RefocusOnTemperatureDelta enabled="false">1</RefocusOnTemperatureDelta>
    def getRefocusOnTemperatureDelta(Enable,Text):
        return self.xmlDict["SequenceQueue"]["RefocusOnTemperatureDelta"]
    def setRefocusOnTemperatureDelta():
        self.xmlDict["SequenceQueue"]["RefocusOnTemperatureDelta"]['@enabled']=Enable
        self.xmlDict["SequenceQueue"]["RefocusOnTemperatureDelta"]['#text']=Text
        return
	#   RefocusEveryN enabled="false">60</RefocusEveryN>
    def getRefocusEveryN():
        return self
    def setRefocusEveryN(Enable,Text):
        self.xmlDict["SequenceQueue"]["setRefocusEveryN"]['@enabled']=Enable
        self.xmlDict["SequenceQueue"]["setRefocusEveryN"]['#text']=Text
        return
	#   RefocusOnMeridianFlip enabled="false"></RefocusOnMeridianFlip>
    def getRefocusOnMeridianFlip():
        return self.xmlDict["SequenceQueue"]["RefocusOnMeridianFlip"]
    def setRefocusOnMeridianFlip():
        self.xmlDict["SequenceQueue"]["RefocusOnMeridianFlip"]['@enabled']=Enable
        return
    ##############################################################
    # Save routines
    def save():
        outFile=open(inputFile,'w')
        outFile.write(xmltodict.unparse(xmlDict, pretty=True))
        outFile.close()
        return
    # Save the new Sequence file to a specified filename
    def saveAs(outputFile):
        outFile=open(outputFile,'w')
        outFile.write(xmltodict.unparse(xmlDict, pretty=True))
        outFile.close()
        return
    
    #############################################################
    # Job handling
    #   Return a list of exposure jobs    
    def getJobs(self):
        return(self.jobList)
    #   Add an additional exposure job, returns job index number
    def addJob(self):
        jobList.append(self.templateJob)
        return len(self.jobList)
    #   Remove all exposure jobs
    def delJobs(self):
        pass
    # Return a specific job 
    def getJob(self,seqNo):
        return self.jobList[seqNo]
    
    # Design decision - let the user just manipulate job entries directly, getters and setters more of a pain than they're worth

