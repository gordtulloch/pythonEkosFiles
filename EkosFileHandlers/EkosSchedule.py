import xmltodict

class EkosSchedule:
    def __init__(self,inputFile):
        self.inFile=open(inputFile,'r')
        self.xmlText=self.inFile.read()
        self.xmlDict=xmltodict.parse(self.xmlText)
        self.jobList=self.xmlDict["SequenceQueue"]["Job"]
        self.templateJob=self.jobList[0]
        self.inFile.close()

    ######################################################################
    # Getters and setters
       
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

