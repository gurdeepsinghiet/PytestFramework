import json
import os
from jsonpath_ng.ext import parse
from EMSWS.Utilities import UtilityClass
import  EMSWS.Constant as Constant
import logging
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class LicenseModelfactory(object):

    def updateLicencezModelAttribute(self,LM_ATTR_Name , value, response_LM_json):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        jsonpath_expression = parse('$..licenseModelAttribute[*]')
        for match in jsonpath_expression.find(response_LM_json):
            if (match.value["enforcementAttribute"]["name"] == LM_ATTR_Name):
                match.value["value"] = value
        self.Updated_LM_Json=response_LM_json
        LOGGER.info(response_LM_json)
        return self

    def updateLicencezModelAttributes(self,LM_ATTR_NameList , valueList, response_LM_json):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        jsonpath_expression = parse('$..licenseModelAttribute[*]')
        for i,attr in enumerate(LM_ATTR_NameList):
            for match in jsonpath_expression.find(response_LM_json):
                if (match.value["enforcementAttribute"]["name"] == LM_ATTR_NameList[i]):
                    LOGGER.info(attr[i])
                    LOGGER.info(valueList[i])
                    match.value["value"] = valueList[i]
        self.Updated_LM_Json = response_LM_json
        return self

    def getEnforcement(self):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response = self.getRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS :10.0',"",currentApiFuncName(),200)
        if response[1] == 200:
            response_Enforcement = utility.convertJsontoDictinary(response[0])
            enforcementId = response_Enforcement["enforcement"]["id"]
            self.enforcementProps = [enforcementId]
        return self

    def searchEnforcement(self):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response = self.getRequest(url + '/ems/api/v5/enforcements?name=Sentinel RMS',"",currentApiFuncName(),200)
        if response[1] == 200:
            response_Enforcement = utility.convertJsontoDictinary(response[0])
            enforcementId = response_Enforcement["enforcements"]["enforcement"][0]["id"]
            self.enforcementProps = [enforcementId]
        return self

    def getEnforcementId(self) ->list:
        return self.enforcementProps

    def searchFlexibleLicenseModel(self):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.searchEnforcement();
        enforcementId=self.getEnforcementId()[0];
        responseFlexibleLicenseModel = self.getRequest(url +'/ems/api/v5/enforcements/' + enforcementId + '/licenseModels/name=Flexible License Model', "", currentApiFuncName(),200)
        if responseFlexibleLicenseModel[1] == 200:
            flexibleLicenseModelJson = utility.convertJsontoDictinary(responseFlexibleLicenseModel[0])
            #LOGGER.info(flexibleLicenseModelJson)
            self.FlexibleLicenseModelJson = flexibleLicenseModelJson
        return self

    def searchCloudConnectedLicenceModel(self):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.searchEnforcement();
        enforcementId = self.getEnforcementId()[0];
        responseFlexibleLicenseModel = self.getRequest(
            url + '/ems/api/v5/enforcements/' + enforcementId + '/licenseModels/name=Connected License Model', "",
            currentApiFuncName(), 200)
        if responseFlexibleLicenseModel[1] == 200:
            cloudConnectedLicenseModelJson = utility.convertJsontoDictinary(responseFlexibleLicenseModel[0])
            LOGGER.info(cloudConnectedLicenseModelJson)
            self.CloudConnectedLicenseModelJson = cloudConnectedLicenseModelJson
        return self


    def addFlexibleLicenceModelStandalone(self, LMNameGenerator, response_LM_json,expectedCode,variableList=None,xPathList=None):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        self.updateLicencezModelAttribute("ENFORCE_CLOCK_TAMPERED", "FALSE", response_LM_json)
        self.updateLicencezModelAttribute("LICENSE_TYPE", "1", response_LM_json)
        self.updateLicencezModelAttribute("DEPLOYMENT_TYPE", "1", response_LM_json)
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response_LM_json["licenseModel"]["name"] = LMNameGenerator
        response_LM_json1 = json.dumps(response_LM_json)
        if expectedCode == 201 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                             response_LM_json1, currentApiFuncName(), expectedCode, ["LM_name", "lmId","LMRES"],
                             ['$.licenseModel.name', '$.licenseModel.id','$'])
            LOGGER.info(self.emsVariableList["LM_name"])
            LOGGER.info(self.emsVariableList["lmId"])
            LOGGER.info(self.emsVariableList["LMRES"])
        elif (variableList != None and xPathList != None):
            LOGGER.info("========================================")
            self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels', response_LM_json1, currentApiFuncName(), expectedCode,
                             variableList, xPathList)
        return self


    def addFlexibleLicenceModelNetwork(self, LMNameGenerator, response_LM_json,expectedCode,resvariableList=None,resxPathList=None):
        self.updateLicencezModelAttribute("ENFORCE_CLOCK_TAMPERED", "FALSE", response_LM_json)
        self.updateLicencezModelAttribute("LICENSE_TYPE", "0", response_LM_json)
        self.updateLicencezModelAttribute("DEPLOYMENT_TYPE", "1", response_LM_json)
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response_LM_json["licenseModel"]["name"] = LMNameGenerator
        response_LM_json1 = json.dumps(response_LM_json)
        if expectedCode == 201 and resvariableList == None and resxPathList == None:
            self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                             response_LM_json1, currentApiFuncName(), expectedCode, ["LM_name", "lmId"],
                             ['$.licenseModel.name', '$.licenseModel.id'])
            LOGGER.info(self.emsVariableList["LM_name"])
            LOGGER.info(self.emsVariableList["lmId"])
        elif (resvariableList != None and resxPathList != None):
            self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels', response_LM_json1, currentApiFuncName(), expectedCode,
                             resvariableList, resxPathList)
        return self


    def addOnPremiseLMNetwork(self, LMNameGenerator, response_LM_json,expectedCode,resvariableList=None,resxPathList=None):
        self.updateLicencezModelAttribute("ENFORCE_CLOCK_TAMPERED", "FALSE", response_LM_json)
        self.updateLicencezModelAttribute("LICENSE_TYPE", "0", response_LM_json)
        self.updateLicencezModelAttribute("DEPLOYMENT_TYPE", "0", response_LM_json)
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response_LM_json["licenseModel"]["name"] = LMNameGenerator
        response_LM_json1 = json.dumps(response_LM_json)
        if expectedCode == expectedCode and resvariableList == None and resxPathList == None:
            self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                             response_LM_json1, currentApiFuncName(), expectedCode, ["LM_name", "lmId"],
                             ['$.licenseModel.name', '$.licenseModel.id'])
            LOGGER.info(self.emsVariableList["LM_name_onPrem_Net"])
            LOGGER.info(self.emsVariableList["lmId_onPrem_net"])
        elif (expectedCode != None and expectedCode != None and resxPathList != None):
            self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels', response_LM_json1, currentApiFuncName(), expectedCode,
                             resvariableList, resxPathList)
        return self

    def addOnPremiseLMStandalone(self, LMNameGenerator, response_LM_json, expectedCode, resvariableList=None,
                              resxPathList=None):
        self.updateLicencezModelAttribute("ENFORCE_CLOCK_TAMPERED", "FALSE", response_LM_json)
        self.updateLicencezModelAttribute("LICENSE_TYPE", "1", response_LM_json)
        self.updateLicencezModelAttribute("DEPLOYMENT_TYPE", "0", response_LM_json)
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response_LM_json["licenseModel"]["name"] = LMNameGenerator
        response_LM_json1 = json.dumps(response_LM_json)
        if expectedCode == expectedCode and resvariableList == None and resxPathList == None:
            self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                             response_LM_json1, currentApiFuncName(), expectedCode, ["LM_name", "lmId"],
                             ['$.licenseModel.name', '$.licenseModel.id'])
            LOGGER.info(self.emsVariableList["LM_name_OnpremStand"])
            LOGGER.info(self.emsVariableList["lmId_OnpremStand"])
        elif (expectedCode != None and expectedCode != None and resxPathList != None):
            self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels', response_LM_json1, currentApiFuncName(), expectedCode,
                             resvariableList, resxPathList)
        return self

    def addcloudConnectedLicenceModel(self, LMNameGenerator, response_LM_json,expectedCode,resvariableList=None,resxPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response_LM_json["licenseModel"]["name"] = LMNameGenerator
        response_LM_json1 = json.dumps(response_LM_json)
        if expectedCode == 201 and resvariableList == None and resxPathList == None:
            self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                                        response_LM_json1, currentApiFuncName(), expectedCode,["LM_name","lmId"],['$.licenseModel.name','$.licenseModel.id'])
            LOGGER.info(self.emsVariableList["LM_name"])
            LOGGER.info(self.emsVariableList["lmId"])
        elif(expectedCode != None and expectedCode !=None and resxPathList !=None):
            self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels', response_LM_json1, currentApiFuncName(), expectedCode, resvariableList, resxPathList)
        return self


    def partialUpdateLM(self, LM_json, expectedCode,resvariableList, resxPathList,enforcementId=None,enforcementnameVersion=None,licenseModelId=None,lmid=None,LMname=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if lmid !=None and enforcementId !=None:
            response = self.patchRequest(url + '/ems/api/v5/enforcements/'+enforcementId+'/licenseModels/'+lmid, LM_json, currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        elif lmid !=None and enforcementnameVersion !=None:
            response = self.patchRequest(url + '/ems/api/v5/enforcements/nameVersion='+enforcementnameVersion+'/licenseModels/'+lmid, LM_json, currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        elif licenseModelId != None and enforcementnameVersion != None:
            response = self.patchRequest(url + '/ems/api/v5/enforcements/nameVersion='+enforcementnameVersion+'/licenseModels/' + licenseModelId, LM_json,
                                             currentApiFuncName(), expectedCode, resvariableList,resxPathList)
        if licenseModelId != None and enforcementId != None:
            response = self.patchRequest(url + '/ems/api/v5/enforcements/'+enforcementId+'/licenseModels/' + licenseModelId, LM_json,
                                             currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        elif licenseModelId != None and enforcementnameVersion != None:
            response = self.patchRequest(url + '/ems/api/v5/enforcements/nameVersion='+enforcementnameVersion+'/licenseModels/'+licenseModelId, LM_json,
                                             currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        elif LMname != None and enforcementId != None:
            response = self.patchRequest(url + '/ems/api/v5/enforcements/'+enforcementId+'/licenseModels/name='+LMname, LM_json,
                                             currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        elif LMname != None and enforcementnameVersion != None:
            response = self.patchRequest(url + '/ems/api/v5/enforcements/nameVersion='+enforcementnameVersion+'/licenseModels/name='+LMname, LM_json,
                                             currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        if response[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self