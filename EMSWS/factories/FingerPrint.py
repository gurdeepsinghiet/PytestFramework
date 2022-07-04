import EMSWS.EMSConfig as Constant
import EMSWS.JsonPath as JsonPath
import EMSWS.ErrorCode as ErrorCode
import logging
from EMSWS.Utilities import UtilityClass
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class FingerPrintFactory(object):

    def addFingerPrint(self, expectedReturnCode, customerId,outParameterList=None, outJsonPathList=None):
        utility=UtilityClass()
        fpxml=self.retriveFingerPrint("testfp")
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(JsonPath.fingerPrintJsonPath, ['$..friendlyName','$..refId1','$..refId2','$..fingerprintXml'],
                            ["fp"+self.RandomString(9),"fprefId1"+self.RandomString(9),"fprefId2"+self.RandomString(9),fpxml])
        LOGGER.info(self.UpdateJsonFileResponse)
        if expectedReturnCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/customers/'+customerId+'/fingerprints', self.UpdateJsonFileResponse, currentApiFuncName(),
                             expectedReturnCode, ["friendlyName"],
                             ['$..friendlyName'])
            LOGGER.info(self.out_param_List["friendlyName"])

        elif (expectedReturnCode != None and outParameterList != None and outJsonPathList != None):
            self.PostRequest(url + '/ems/api/v5/customers/'+customerId+'fingerprints', self.UpdateJsonFileResponse, currentApiFuncName(),
                             expectedReturnCode, outParameterList, outJsonPathList)
        return self

