import json
import os
import sys
from jsonpath_ng.ext import parse
from EMSWS.Utilities import UtilityClass
import  EMSWS.Constant as Constant
import logging
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class LicenseModelfactory(object):
    def updateLicencezModelAttributeWithTag(self,LM_ATTR_Name,tag,value, response_LM_dictionary):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
        u=UtilityClass()
        AssertionsReport = {}
        AssertionsReport["Api_Name"] = currentFuncName()
        AssertionsReport["inputs"] = u.convertDictinarytoJson(response_LM_dictionary)
        AssertionsReport["Expected_Code"] = "200"
        try:
            jsonpath_expression = parse('$..licenseModelAttribute[*]')
            for match in jsonpath_expression.find(response_LM_dictionary):
                if (match.value["enforcementAttribute"]["name"] == LM_ATTR_Name):
                    match.value[tag] = value
                    self.Updated_LM_Json=response_LM_dictionary
            AssertionsReport["actual_Code"] = "200"
            AssertionsReport["Expected_Response"] = u.convertDictinarytoJson(response_LM_dictionary)
            AssertionsReport["Status"] = "Pass"
            AssertionsReport["Act_Response"] = u.convertDictinarytoJson(response_LM_dictionary)
            AssertionsReport["Response_time"] = ""
        except TypeError as error:
            AssertionsReport["actual_Code"] = "404"
            AssertionsReport["Expected_Response"] = ""
            AssertionsReport["Status"] = "Failed"
            AssertionsReport["Act_Response"] = "Type Error occured during updation of LM json"
            AssertionsReport["Response_time"] = ""
        self.data.append(AssertionsReport)
        return self


    def getLicenceModelAttributeTagValue(self, LM_ATTR_Name, tag, variable ,response_LM_dictionary):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
        u = UtilityClass()
        AssertionsReport = {}
        AssertionsReport["Api_Name"] = currentFuncName()
        AssertionsReport["inputs"] = u.convertDictinarytoJson(response_LM_dictionary)
        AssertionsReport["Expected_Code"] = "200"
        jsonpath_expression = parse('$..licenseModelAttribute[*]')
        try:
            for match in jsonpath_expression.find(response_LM_dictionary):
                if (match.value["enforcementAttribute"]["name"] == LM_ATTR_Name):
                    self.emsVariableList[variable]=match.value[tag]
            LOGGER.info(self.emsVariableList[variable])
            AssertionsReport["actual_Code"] = "200"
            AssertionsReport["Expected_Response"] = u.convertDictinarytoJson(response_LM_dictionary)
            AssertionsReport["Status"] = "Pass"
            AssertionsReport["Act_Response"] = u.convertDictinarytoJson(response_LM_dictionary)
            AssertionsReport["Response_time"] = ""
        except TypeError as error:
            AssertionsReport["actual_Code"] = "404"
            AssertionsReport["Expected_Response"] = ""
            AssertionsReport["Status"] = "Failed"
            AssertionsReport["Act_Response"] = "Type Error occured during updation of LM json"
            AssertionsReport["Response_time"] = ""
        self.data.append(AssertionsReport)

        return self

    #this method update the multiple License Attributes of LM Dictionary object
    #LM_ATTR_NameList : List of Attributed need to be update
    #tagsList: tags names of LM Attributes List
    #valueList : correspondes value of Tags nned to be updated
    #response_LM_dictionry : Dictionary object of LM Json
    def updateLicencezModelAttributesbyTags(self, LM_ATTR_NameList, tagsList,valueList, response_LM_dictionary):
        currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
        u = UtilityClass()
        AssertionsReport = {}
        AssertionsReport["Api_Name"] = currentFuncName()
        AssertionsReport["inputs"] = u.convertDictinarytoJson(response_LM_dictionary)
        AssertionsReport["Expected_Code"] = "200"
        jsonpath_expression = parse('$..licenseModelAttribute[*]')
        try:
            for i, attr in enumerate(LM_ATTR_NameList):
                for match in jsonpath_expression.find(response_LM_dictionary):
                    if (match.value["enforcementAttribute"]["name"] == LM_ATTR_NameList[i]):
                        LOGGER.info(attr[i])
                        LOGGER.info(valueList[i])
                        match.value[tagsList[i]] = valueList[i]
                        self.Updated_LM_Json = response_LM_dictionary
            AssertionsReport["actual_Code"] = "200"
            AssertionsReport["Expected_Response"] = u.convertDictinarytoJson(response_LM_dictionary)
            AssertionsReport["Status"] = "Pass"
            AssertionsReport["Act_Response"] = u.convertDictinarytoJson(response_LM_dictionary)
            AssertionsReport["Response_time"] = ""
        except TypeError as error:
            AssertionsReport["actual_Code"] = "404"
            AssertionsReport["Expected_Response"] = ""
            AssertionsReport["Status"] = "Failed"
            AssertionsReport["Act_Response"] = "Type Error occured during updation of LM json"
            AssertionsReport["Response_time"] = ""
        self.data.append(AssertionsReport)
        return self

    def getLicenceModelAttributesTagsValues(self, LM_ATTR_NameList, tagsList,variableList, response_LM_dictionary):
        currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
        u = UtilityClass()
        AssertionsReport = {}
        AssertionsReport["Api_Name"] = currentFuncName()
        AssertionsReport["inputs"] = u.convertDictinarytoJson(response_LM_dictionary)
        AssertionsReport["Expected_Code"] = "200"
        jsonpath_expression = parse('$..licenseModelAttribute[*]')
        try:
            for i, attr in enumerate(LM_ATTR_NameList):
                for match in jsonpath_expression.find(response_LM_dictionary):
                    if (match.value["enforcementAttribute"]["name"] == LM_ATTR_NameList[i]):
                        LOGGER.info(attr[i])
                        LOGGER.info(variableList[i])
                        self.emsVariableList[variableList[i]]=match.value[tagsList[i]]
            AssertionsReport["actual_Code"] = "200"
            AssertionsReport["Expected_Response"] = u.convertDictinarytoJson(response_LM_dictionary)
            AssertionsReport["Status"] = "Pass"
            AssertionsReport["Act_Response"] = u.convertDictinarytoJson(response_LM_dictionary)
            AssertionsReport["Response_time"] = ""
        except TypeError as error:
            AssertionsReport["actual_Code"] = "404"
            AssertionsReport["Expected_Response"] = ""
            AssertionsReport["Status"] = "Failed"
            AssertionsReport["Act_Response"] = "Type Error occurred during updating of LM json"
            AssertionsReport["Response_time"] = ""

        return self

    def getLicenceModelAttributesTagsValues(self, LM_ATTR_NameList, tagsList, getvalueList, response_LM_dictionry):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        jsonpath_expression = parse('$..licenseModelAttribute[*]')
        for i, attr in enumerate(LM_ATTR_NameList):
            for match in jsonpath_expression.find(response_LM_dictionry):
                if (match.value["enforcementAttribute"]["name"] == LM_ATTR_NameList[i]):
                    LOGGER.info(attr[i])
                    LOGGER.info(getvalueList[i])
                    self.emsVariableList[getvalueList[i]] = match.value[tagsList[i]]
        return self
    def getEnforcement(self):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.getApiresponse = self.getRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS :10.0',"",currentApiFuncName(),200)
        if self.getApiresponse[1] == 200:
            response_Enforcement = utility.convertJsontoDictinary(self.getApiresponse[0])
            enforcementId = response_Enforcement["enforcement"]["id"]
            self.enforcementProps = [enforcementId]
        return self

    def searchEnforcement(self):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.getRequest(url + '/ems/api/v5/enforcements?name=Sentinel RMS',"",currentApiFuncName(),200)
        if self.getApiresponse[1] == 200:
            response_Enforcement = utility.convertJsontoDictinary(self.getApiresponse[0])
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
        self.getRequest(url +'/ems/api/v5/enforcements/' + enforcementId + '/licenseModels/name=Flexible License Model', "", currentApiFuncName(),200)
        if self.getApiresponse[1] == 200:
            flexibleLicenseModelJson = utility.convertJsontoDictinary(self.getApiresponse[0])
            #LOGGER.info(flexibleLicenseModelJson)
            self.FlexibleLicenseModelJson = flexibleLicenseModelJson
        return self

    def searchCloudConnectedLicenceModel(self):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.searchEnforcement();
        enforcementId = self.getEnforcementId()[0];
        self.getRequest(
            url + '/ems/api/v5/enforcements/' + enforcementId + '/licenseModels/name=Connected License Model', "",
            currentApiFuncName(), 200)
        if self.getApiresponse[1] == 200:
            cloudConnectedLicenseModelJson = utility.convertJsontoDictinary(self.getApiresponse[0])
            LOGGER.info(cloudConnectedLicenseModelJson)
            self.CloudConnectedLicenseModelJson = cloudConnectedLicenseModelJson
        return self


    def addFlexibleLicenceModelStandalone(self, LMNameGenerator, response_LM_dict,expectedCode,variableList=None,xPathList=None):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        self.updateLicencezModelAttributeWithTag("ENFORCE_CLOCK_TAMPERED","value", "FALSE", response_LM_dict)
        self.updateLicencezModelAttributeWithTag("LICENSE_TYPE","value" ,"1", response_LM_dict)
        self.updateLicencezModelAttributeWithTag("DEPLOYMENT_TYPE","value", "1", response_LM_dict)
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response_LM_dict["licenseModel"]["name"] = LMNameGenerator
        response_LM_json1 = json.dumps(response_LM_dict)
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


    def addFlexibleLicenceModelNetwork(self, LMNameGenerator, response_LM_dict,expectedCode,resvariableList=None,resxPathList=None):
        self.updateLicencezModelAttributeWithTag("ENFORCE_CLOCK_TAMPERED", "value","FALSE", response_LM_dict)
        self.updateLicencezModelAttributeWithTag("LICENSE_TYPE", "value","0", response_LM_dict)
        self.updateLicencezModelAttributeWithTag("DEPLOYMENT_TYPE", "value","1", response_LM_dict)
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response_LM_dict["licenseModel"]["name"] = LMNameGenerator
        response_LM_json1 = json.dumps(response_LM_dict)
        if expectedCode == 201 and resvariableList == None and resxPathList == None:
            self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                             response_LM_json1, currentApiFuncName(), expectedCode, ["LM_name_onpremNetwork", "lmId_onprem_network"],
                             ['$.licenseModel.name', '$.licenseModel.id'])
            LOGGER.info(self.emsVariableList["LM_name_onpremNetwork"])
            LOGGER.info(self.emsVariableList["lmId_onprem_network"])
        elif (resvariableList != None and resxPathList != None):
            self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels', response_LM_json1, currentApiFuncName(), expectedCode,
                             resvariableList, resxPathList)
        return self


    def addOnPremiseLMNetwork(self, LMNameGenerator, response_LM_dic,expectedCode,resvariableList=None,resxPathList=None):
        self.updateLicencezModelAttributeWithTag("ENFORCE_CLOCK_TAMPERED", "value","FALSE", response_LM_dic)
        self.updateLicencezModelAttributeWithTag("LICENSE_TYPE", "value","0", response_LM_dic)
        self.updateLicencezModelAttributeWithTag("DEPLOYMENT_TYPE","value", "0", response_LM_dic)
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response_LM_dic["licenseModel"]["name"] = LMNameGenerator
        response_LM_json1 = json.dumps(response_LM_dic)
        if expectedCode == expectedCode and resvariableList == None and resxPathList == None:
            self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                             response_LM_json1, currentApiFuncName(), expectedCode, ["LM_name_onPrem_Net", "lmId_onPrem_net"],
                             ['$.licenseModel.name', '$.licenseModel.id'])
            LOGGER.info(self.emsVariableList["LM_name_onPrem_Net"])
            LOGGER.info(self.emsVariableList["lmId_onPrem_net"])
        elif (expectedCode != None and expectedCode != None and resxPathList != None):
            self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels', response_LM_json1, currentApiFuncName(), expectedCode,
                             resvariableList, resxPathList)
        return self

    def addOnPremiseLMStandalone(self, LMNameGenerator, response_LM_dict, expectedCode, resvariableList=None,
                              resxPathList=None):
        self.updateLicencezModelAttributeWithTag("ENFORCE_CLOCK_TAMPERED","value", "FALSE", response_LM_dict)
        self.updateLicencezModelAttributeWithTag("LICENSE_TYPE", "value", "1", response_LM_dict)
        self.updateLicencezModelAttributeWithTag("DEPLOYMENT_TYPE", "value", "0", response_LM_dict)
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response_LM_dict["licenseModel"]["name"] = LMNameGenerator
        response_LM_json1 = json.dumps(response_LM_dict)
        if expectedCode == expectedCode and resvariableList == None and resxPathList == None:
            self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                             response_LM_json1, currentApiFuncName(), expectedCode, ["LM_name_OnpremStand", "lmId_OnpremStand"],
                             ['$.licenseModel.name', '$.licenseModel.id'])
            LOGGER.info(self.emsVariableList["LM_name_OnpremStand"])
            LOGGER.info(self.emsVariableList["lmId_OnpremStand"])
        elif (expectedCode != None and expectedCode != None and resxPathList != None):
            self.PostRequest(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels', response_LM_json1, currentApiFuncName(), expectedCode,
                             resvariableList, resxPathList)
        return self

    def addcloudConnectedLicenceModel(self, LMNameGenerator, response_LM_dict,expectedCode,resvariableList=None,resxPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        response_LM_dict["licenseModel"]["name"] = LMNameGenerator
        response_LM_json1 = json.dumps(response_LM_dict)
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
            self.patchRequest(url + '/ems/api/v5/enforcements/'+enforcementId+'/licenseModels/'+lmid, LM_json, currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        elif lmid !=None and enforcementnameVersion !=None:
            self.patchRequest(url + '/ems/api/v5/enforcements/nameVersion='+enforcementnameVersion+'/licenseModels/'+lmid, LM_json, currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        elif licenseModelId != None and enforcementnameVersion != None:
            self.patchRequest(url + '/ems/api/v5/enforcements/nameVersion='+enforcementnameVersion+'/licenseModels/' + licenseModelId, LM_json,
                                             currentApiFuncName(), expectedCode, resvariableList,resxPathList)
        if licenseModelId != None and enforcementId != None:
            self.patchRequest(url + '/ems/api/v5/enforcements/'+enforcementId+'/licenseModels/' + licenseModelId, LM_json,
                                             currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        elif licenseModelId != None and enforcementnameVersion != None:
            self.patchRequest(url + '/ems/api/v5/enforcements/nameVersion='+enforcementnameVersion+'/licenseModels/'+licenseModelId, LM_json,
                                             currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        elif LMname != None and enforcementId != None:
            self.patchRequest(url + '/ems/api/v5/enforcements/'+enforcementId+'/licenseModels/name='+LMname, LM_json,
                                             currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        elif LMname != None and enforcementnameVersion != None:
            self.patchRequest(url + '/ems/api/v5/enforcements/nameVersion='+enforcementnameVersion+'/licenseModels/name='+LMname, LM_json,
                                             currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        if self.patchApiresponse[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self