import xmltodict

class EkosSequence(inputFile):
    def __init__(self,inputFile):
        self.inFile=open(inputFile,'r')
        self.xmlText=self.inFile.read()
        self.xmlDict=xmltodict.parse(xmlText)
        self.jobList=self.xmlDict["SequenceQueue"]["Job"]
        self.templateJob=self.jobList[0]
        self.inFile.close()

    # Return a list of exposure jobs    
    def getExposures():
        return(self.jobList)
    # Add an additional exposure job, returns job index number
    def addExposure():
        jobDict.append(self.templateJob)
        return len(jobDict)
    # Remove all exposure jobs
    def delExposures():
        pass
    #GuideDeviation enabled="false">2</GuideDeviation>
    def getGuideDeviation():
        return self.xmlDict["SequenceQueue"]["GuideDeviation"]
        pass
    def setGuideDeviation(Enable,Text):
        self.xmlDict["SequenceQueue"]["GuideDeviation"]['@enabled'] = Enable
        self.xmlDict["SequenceQueue"]["GuideDeviation"]["#text"]    = Text
        return
	# GuideStartDeviation enabled="false">2</GuideStartDeviation>
    def getGuideStartDeviation():
        return self.xmlDict["SequenceQueue"]["GuideStartDeviation"]
        pass
    def setGuideStartDeviation(Enable,Text):
        self.xmlDict["SequenceQueue"]["GuideStartDeviation"]['@enabled'] = Enable
        self.xmlDict["SequenceQueue"]["GuideStartDeviation"]["#text"]    = Text
        return
	#HFRCheck enabled="false">
	#	<HFRDeviation>0.5</HFRDeviation>
	#	<HFRCheckAlgorithm>0</HFRCheckAlgorithm>
	#	<HFRCheckThreshold>10</HFRCheckThreshold>
	#	<HFRCheckFrames>1</HFRCheckFrames>
    def getHFRCheck():
        return self.xmlDict["SequenceQueue"]["HFRCheck"]
    def setHFRCheck(Enable,HFRDeviation,HFRCheckAlgorithm,HFRCheckThreshold,HFRCheckFrames):
        self.xmlDict["SequenceQueue"]["HFRCheck"]['@enabled']=Enable
        self.xmlDict["SequenceQueue"]["HFRCheck"]["HFRDeviation"]=HFRDeviation
        self.xmlDict["SequenceQueue"]["HFRCheck"]["HFRCheckAlgorithm"]=HFRCheckAlgorithm
        self.xmlDict["SequenceQueue"]["HFRCheck"]["HFRCheckThreshold"]=HFRCheckThreshold
        self.xmlDict["SequenceQueue"]["HFRCheck"]["HFRCheckFrames"]=HFRCheckFrames
        return
    #RefocusOnTemperatureDelta enabled="false">1</RefocusOnTemperatureDelta>
    def getRefocusOnTemperatureDelta(Enable,Text):
        return self.xmlDict["SequenceQueue"]["RefocusOnTemperatureDelta"]
    def setRefocusOnTemperatureDelta():
        self.xmlDict["SequenceQueue"]["RefocusOnTemperatureDelta"]['@enabled']=Enable
        self.xmlDict["SequenceQueue"]["RefocusOnTemperatureDelta"]['#text']=Text
        return
	#RefocusEveryN enabled="false">60</RefocusEveryN>
    def getRefocusEveryN():
        return self.xmlDict["SequenceQueue"]["RefocusEveryN"]

    def setRefocusEveryN(Enable,Text):
        self.xmlDict["SequenceQueue"]["setRefocusEveryN"]['@enabled']=Enable
        self.xmlDict["SequenceQueue"]["setRefocusEveryN"]['#text']=Text
        return
	# RefocusOnMeridianFlip enabled="false"></RefocusOnMeridianFlip>
    def getRefocusOnMeridianFlip():
        return self.xmlDict["SequenceQueue"]["RefocusOnMeridianFlip"]
    def setRefocusOnMeridianFlip():
      pass

    # Save the Sequence file to the same filename as when loaded
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

'''<Job>
		<Exposure>1</Exposure>
		<Format>Mono</Format>
		<Encoding>FITS</Encoding>
		<Binning>
			<X>1</X>
			<Y>1</Y>
		</Binning>
		<Frame>
			<X>0</X>
			<Y>0</Y>
			<W>1280</W>
			<H>1024</H>
		</Frame>
		<Temperature force="false">0</Temperature>
		<Filter>Red</Filter>
		<Type>Light</Type>
		<Count>1</Count>
		<Delay>0</Delay>
		<TargetName></TargetName>
		<GuideDitherPerJob>0</GuideDitherPerJob>
		<FITSDirectory>/home/gtulloch/AstroPictures</FITSDirectory>
		<PlaceholderFormat>/%t/%T/%F/%t_%T_%F</PlaceholderFormat>
		<PlaceholderSuffix>3</PlaceholderSuffix>
		<UploadMode>0</UploadMode>
		<Properties></Properties>
		<Calibration>
			<PreAction>
				<Type>0</Type>
			</PreAction>
			<FlatDuration dark="false">
				<Type>Manual</Type>
			</FlatDuration>
		</Calibration>
	</Job>'''
