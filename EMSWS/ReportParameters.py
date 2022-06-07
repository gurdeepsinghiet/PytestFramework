class ReportParam(object):

    def __init__(self):
        self.ReportParameters={}

    def setApiName(self,ApiName):
        self.ReportParameters["Api_Name"] = ApiName

    def setInputs(self,inputs):
        self.ReportParameters["inputs"] = inputs

    def setExpectedCode(self,ExpectedCode):
        self.ReportParameters["Expected_Code"] = ExpectedCode

    def setActualCode(self,ActualCode):
        self.ReportParameters["actual_Code"] = ActualCode

    def setResponseTime(self, ResponseTime):
        self.ReportParameters["Response_time"] = ResponseTime

    def setActualRespone(self, ActualResponse):
        self.ReportParameters["Act_Response"] = ActualResponse

    def setStatus(self, Status):
        self.ReportParameters["Status"] = Status

    def setComments(self, Comments):
        self.ReportParameters["Comments"] = Comments

    def setExpectedResponse(self, ExpectedResponse):
        self.ReportParameters["Expected_Response"] = ExpectedResponse

    def getReportParameters(self):
        return self.ReportParameters