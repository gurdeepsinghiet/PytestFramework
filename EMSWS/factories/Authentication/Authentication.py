import EMSWS.EMSConfig as Constant
import  EMSWS.ErrorCode as ErrorCode
import logging
from EMSWS.Utilities import UtilityClass
from requests.structures import CaseInsensitiveDict
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class AuthenticationFactory(object):

    def getIDPConfiguration(self,expectedCode,resvariableList,resxPathList):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.GetAuthRequest(Constant.EMSURL +"/token/api/v5/idpConfigurations","", "", currentApiFuncName(), Constant.HTTP200, "", "",resvariableList,resxPathList)
        if self.getAuthApiresponse[1] == expectedCode:
                for i, resvar in enumerate(resvariableList):
                    LOGGER.info(resvariableList[i])
                    LOGGER.info(self.emsVariableList[resvariableList[i]])

        return self


    def getKeyclockToken(self,user,passwrd,expectedCode,variableList = None,xPathList = None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        self.getIDPConfiguration(ErrorCode.HTTP200,["realm","tokenEndpoint","clientId"],["$..realm","$..tokenEndpoint","$..clientId"])
        data = {"grant_type": Constant.grant_type, "username": user, "password": passwrd,
                "client_id": self.emsVariableList["clientId"]}
        if expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None:
            self.PostAuthRequest(self.emsVariableList["tokenEndpoint"].split("/auth")[0]+
                "/auth/realms/"+self.emsVariableList["realm"]+"/protocol/openid-connect/token",
                data, headers, "keyclocktokenApi", expectedCode, user, passwrd,["access_token"],["$.access_token"],bearerAuth="Yes")
            LOGGER.info(self.emsVariableList["access_token"])
        elif expectedCode != None and variableList != None and xPathList != None:
            self.PostAuthRequest(self.emsVariableList["tokenEndpoint"].split("/auth")[0] +
                                 "/auth/realms/" + self.emsVariableList["realm"] + "/protocol/openid-connect/token",
                                 data, headers, "keyclocktokenApi", expectedCode, user, passwrd,variableList,xPathList,bearerAuth="Yes")
        return self


    def addRegistrationTokenWithoutCostomer(self,regTokenXmlJsonPath,keyClockToken,identifier,refId1,refId2,count,expectedCode,variableList =None,xPathList = None,outputXmlResVar=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if self.isXmlFile(self.getModulePath()+regTokenXmlJsonPath):
            self.updateXMLFile(regTokenXmlJsonPath,
                               ["./identifier", "./refId1", "./refId2", "./count"],
                               [identifier, refId1, refId2, count])

            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + keyClockToken
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            if expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(),
                                     expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                     ["registrationtoken"], ["./token"], bearerAuth="Yes",
                                     outputXmlResVar=outputXmlResVar)

            elif expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(),
                                     expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                     ["registrationtoken"], ["./token"], bearerAuth="Yes")

            elif expectedCode != None and variableList != None and xPathList != None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                     variableList, xPathList, bearerAuth="Yes", outputXmlResVar=outputXmlResVar)

            elif expectedCode != None and variableList != None and xPathList != None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                     variableList, xPathList, bearerAuth="Yes")
        elif self.isJsonFile(self.getModulePath()+regTokenXmlJsonPath):
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + keyClockToken
            self.UpdateJsonFile(regTokenXmlJsonPath,
                                ['$..identifier', '$..refId1', '$..refId2', '$..count'],
                                [identifier, refId1, refId2, count])
            if expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None:
                self.PostAuthRequest(url + '/token/api/v5/registrationTokens', self.UpdateJsonFileResponse, headers,currentApiFuncName(), expectedCode,"","",
                                 ["regToken", "registrationRes"],
                                 ['$..token', '$'],bearerAuth="Yes")
                LOGGER.info(self.emsVariableList["regToken"])
                LOGGER.info(self.emsVariableList["registrationRes"])
            elif expectedCode != None and variableList != None and xPathList != None:
                self.PostAuthRequest(url + '/token/api/v5/registrationTokens', self.UpdateJsonFileResponse, headers,currentApiFuncName(),
                                 expectedCode,"","", variableList, xPathList,bearerAuth="Yes")


        return self


    def addRegTokenWithoutCostomer(self,regTokenXmlJsonPath,keyClockToken,count,expectedCode,variableList = None,xPathList = None,outputXmlResVar=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        identifier="regToken"+self.RandomString(8)
        refId1="regTokenrefId1"+self.RandomString(8)
        refId2="regTokenrefId2"+self.RandomString(8)
        if self.isXmlFile(self.getModulePath()+regTokenXmlJsonPath):
            self.updateXMLFile(regTokenXmlJsonPath,
                               ["./identifier", "./refId1", "./refId2", "./count"],
                               [identifier, refId1, refId2, count])
            headers = CaseInsensitiveDict()
            headers["Authorization"] = f'Bearer {keyClockToken}'
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            LOGGER.info(self.xmlstroutput)
            if expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode, "", "",
                                     ["registrationtoken"], ["./token"], bearerAuth="Yes")
            elif expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode, "", "",
                                     ["registrationtoken"], ["./token"], bearerAuth="Yes",
                                     outputXmlResVar=outputXmlResVar)

            elif expectedCode != None and variableList != None and xPathList != None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                     variableList, xPathList, bearerAuth="Yes")
            elif expectedCode != None and variableList != None and xPathList != None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                     variableList, xPathList, bearerAuth="Yes", outputXmlResVar=outputXmlResVar)
        elif self.isJsonFile(self.getModulePath()+regTokenXmlJsonPath):
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + keyClockToken
            self.UpdateJsonFile(regTokenXmlJsonPath,
                                ['$..identifier', '$..refId1', '$..refId2', '$..count'],
                                [identifier, refId1, refId2, count])
            if expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None:
                self.PostAuthRequest(url + '/token/api/v5/registrationTokens', self.UpdateJsonFileResponse, headers,
                                     currentApiFuncName(), expectedCode,"","",
                                     variableList=["regToken", "registrationRes","tokenId"],
                                     xPathList=['$..token', '$','$..id'],bearerAuth="Yes",outputXmlResVar=None)
                LOGGER.info(self.emsVariableList["regToken"])
                LOGGER.info(self.emsVariableList["registrationRes"])
            elif expectedCode != None and variableList != None and xPathList != None:
                self.PostAuthRequest(url + '/token/api/v5/registrationTokens', self.UpdateJsonFileResponse,headers, currentApiFuncName(),
                                 expectedCode,"","", variableList, xPathList,bearerAuth="Yes",outputXmlResVar=None)


        return self


    def addRegistrationTokenWithCostomer(self,regTokenXmlJsonPath,keyClockToken,customerName,identifier,refId1,refId2,count,expectedCode,variableList = None,
                                         xPathList = None,outputXmlResVar=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if self.isXmlFile(self.getModulePath()+regTokenXmlJsonPath):
            self.updateXMLFile(regTokenXmlJsonPath,
                               [".//name", "./identifier", "./refId1", "./refId2", "./count"],
                               [customerName, identifier, identifier, refId1, refId2, count])
            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            headers["Authorization"] = "Bearer " + keyClockToken
            if expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode,
                                     Constant.EMSUserName, Constant.EMSPassword,
                                     ["registrationtoken"], ["./token"], bearerAuth="Yes")
            elif expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode,
                                     Constant.EMSUserName, Constant.EMSPassword,
                                     ["registrationtoken"], ["./token"], bearerAuth="Yes",
                                     outputXmlResVar=outputXmlResVar)

            elif expectedCode != None and variableList != None and xPathList != None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                     variableList, xPathList, bearerAuth="Yes")
            elif expectedCode != None and variableList != None and xPathList != None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                    variableList, xPathList, bearerAuth="Yes", outputXmlResVar=outputXmlResVar)
        elif self.isJsonFile(self.getModulePath()+regTokenXmlJsonPath):
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + keyClockToken
            self.UpdateJsonFile(regTokenXmlJsonPath,
                                ['$..name','$..identifier', '$..refId1', '$..refId2', '$..count'],
                                [customerName,identifier, refId1, refId2, count])
            if expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None:
                self.PostAuthRequest(url + '/token/api/v5/registrationTokens', self.UpdateJsonFileResponse, headers,
                                     currentApiFuncName(), expectedCode,"","",
                                     ["regToken", "registrationRes"],
                                     ['$..token', '$'], bearerAuth="Yes")
                LOGGER.info(self.emsVariableList["regToken"])
                LOGGER.info(self.emsVariableList["registrationRes"])
            elif expectedCode != None and variableList != None and xPathList != None:
                self.PostAuthRequest(url + '/token/api/v5/registrationTokens', self.UpdateJsonFileResponse, headers,
                                     currentApiFuncName(),
                                     expectedCode, "","",variableList, xPathList, bearerAuth="Yes")

        return self

    def addRegTokenWithCostomer(self,regTokenXmlJsonPath,keyClockToken,customerName,count,expectedCode,variableList = None,xPathList = None,outputXmlResVar=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        identifier = "regCustToken" + self.RandomString(8)
        refId1 = "regCustTokenrefId1" + self.RandomString(8)
        refId2 = "regCustTokenrefId2" + self.RandomString(8)
        if self.isXmlFile(self.getModulePath()+regTokenXmlJsonPath):
            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            headers["Authorization"] = "Bearer " + keyClockToken

            self.updateXMLFile(regTokenXmlJsonPath,
                               [".//name", "./identifier", "./refId1", "./refId2", "./count"],
                               [customerName, identifier, identifier, refId1, refId2, count])

            if expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode,
                                     Constant.EMSUserName, Constant.EMSPassword, ["registrationtoken"], ["./token"],
                                     bearerAuth="Yes")

            elif expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode,
                                     Constant.EMSUserName, Constant.EMSPassword, ["registrationtoken"], ["./token"],
                                     bearerAuth="Yes", outputXmlResVar=outputXmlResVar)
            elif expectedCode != None and variableList != None and xPathList != None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                     variableList, xPathList,
                                     bearerAuth="Yes")
            elif expectedCode != None and variableList != None and xPathList != None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                     variableList, xPathList,
                                     bearerAuth="Yes", outputXmlResVar=outputXmlResVar)
        elif self.isJsonFile(self.getModulePath()+regTokenXmlJsonPath):
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + keyClockToken
            self.UpdateJsonFile(regTokenXmlJsonPath,
                                ['$..name','$..identifier', '$..refId1', '$..refId2', '$..count'],
                                [customerName,identifier, refId1, refId2, count])
            if expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None:
                self.PostAuthRequest(url + '/token/api/v5/registrationTokens', self.UpdateJsonFileResponse, headers,
                                     currentApiFuncName(), expectedCode,"","",
                                     ["regToken", "registrationRes"],
                                     ['$..token', '$'], bearerAuth="Yes")
                LOGGER.info(self.emsVariableList["regToken"])
                LOGGER.info(self.emsVariableList["registrationRes"])
            elif expectedCode != None and variableList != None and xPathList != None:
                self.PostAuthRequest(url + '/token/api/v5/registrationTokens', self.UpdateJsonFileResponse, headers,
                                     currentApiFuncName(),
                                     expectedCode, "","",variableList, xPathList, bearerAuth="Yes")

        return self


    def createRegistrationToken(self,regTokenXmlJson,keyClockToken,expectedCode,variableList = None,xPathList = None,outputXmlResVar=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/xml"
        headers["Accept"] = "application/xml"
        headers["Authorization"]= "Bearer "+keyClockToken
        if self.isXml(regTokenXmlJson):
            if expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", regTokenXmlJson, headers,
                                     currentApiFuncName(), expectedCode,
                                     Constant.EMSUserName, Constant.EMSPassword, ["registrationtoken"], ["./token"],
                                     bearerAuth="Yes")

            elif expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", regTokenXmlJson, headers,
                                     currentApiFuncName(), expectedCode,
                                     Constant.EMSUserName, Constant.EMSPassword, ["registrationtoken"], ["./token"],
                                     bearerAuth="Yes", outputXmlResVar=outputXmlResVar)
            elif expectedCode != None and variableList != None and xPathList != None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", regTokenXmlJson, headers,
                                     currentApiFuncName(), expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                     variableList, xPathList,
                                     bearerAuth="Yes")
            elif expectedCode != None and variableList != None and xPathList != None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", regTokenXmlJson, headers,
                                     currentApiFuncName(), expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                     variableList, xPathList,
                                     bearerAuth="Yes", outputXmlResVar=outputXmlResVar)
        elif self.isJson(regTokenXmlJson):
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + keyClockToken
            if expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None:
                self.PostAuthRequest(url + '/token/api/v5/registrationTokens', regTokenXmlJson, headers,
                                     currentApiFuncName(), expectedCode,"","",
                                     ["regToken", "registrationRes"],
                                     ['$..token', '$'], bearerAuth="Yes")
                LOGGER.info(self.emsVariableList["regToken"])
                LOGGER.info(self.emsVariableList["registrationRes"])
            elif expectedCode != None and variableList != None and xPathList != None:
                self.PostAuthRequest(url + '/token/api/v5/registrationTokens', regTokenXmlJson, headers,
                                     currentApiFuncName(),
                                     expectedCode,"","", variableList, xPathList, bearerAuth="Yes")

        return self


    def addAccessToken(self,accessTokenXmlJsonPath,registrationToken,identifier,fqdn,refId1,refId2,expectedCode,variableList =None,xPathList = None,outputXmlResVar=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        headers = CaseInsensitiveDict()
        if self.isXmlFile(self.getModulePath()+accessTokenXmlJsonPath):
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            headers["Authorization"] = "Basic " + registrationToken

            self.updateXMLFile(accessTokenXmlJsonPath,
                               ["./identifier", "./refId1", "./refId2", "./fqdn"],
                               [identifier, refId1, refId2, fqdn], ["acessTokenupdatedXml"], [self.xmlstroutput])
            if expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/authTokens",
                                     self.emsVariableList["acessTokenupdatedXml"], headers, currentApiFuncName(),
                                     expectedCode, Constant.EMSUserName, Constant.EMSPassword, ["accesstoken"],
                                     ["./token"], bearerAuth="Yes", outputXmlResVar=outputXmlResVar)
            elif expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/authTokens",
                                     self.emsVariableList["acessTokenupdatedXml"], headers,
                                     currentApiFuncName(), expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                     variableList, xPathList, bearerAuth="Yes")
            elif expectedCode != None and variableList != None and xPathList != None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/authTokens",
                                     self.emsVariableList["acessTokenupdatedXml"], headers,
                                     currentApiFuncName(), expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                     variableList, xPathList, bearerAuth="Yes")

            elif expectedCode != None and variableList != None and xPathList != None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/authTokens",
                                     self.emsVariableList["acessTokenupdatedXml"], headers,
                                     currentApiFuncName(), expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                     variableList, xPathList, bearerAuth="Yes", outputXmlResVar=outputXmlResVar)
        elif self.isJsonFile(self.getModulePath()+accessTokenXmlJsonPath):
            self.UpdateJsonFile(accessTokenXmlJsonPath,
                                ['$..identifier', '$..refId1', '$..refId2', '$..fqdn'],
                                [identifier, refId1, refId2, fqdn])
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Basic " + registrationToken
            if expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None:
                self.PostAuthRequest(url + '/token/api/v5/authTokens', self.UpdateJsonFileResponse, headers,
                                     currentApiFuncName(), expectedCode,"","",
                                     ["authToken", "authAccessRes"],
                                     ['$..token', '$'], bearerAuth="Yes")
                LOGGER.info(self.emsVariableList["regToken"])
                LOGGER.info(self.emsVariableList["authAccessRes"])
            elif expectedCode != None and variableList != None and xPathList != None:
                self.PostAuthRequest(url + '/token/api/v5/authTokens', self.UpdateJsonFileResponse, headers,
                                     currentApiFuncName(),
                                     expectedCode, "","",variableList, xPathList, bearerAuth="Yes")

        return self


    def addAccToken(self,accessTokenXmlJsonPath,registrationToken,expectedCode,variableList = None,xPathList = None,outputXmlResVar=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        identifier = "regCustToken" + self.RandomString(8)
        refId1 = "regCustTokenrefId1" + self.RandomString(8)
        refId2 = "regCustTokenrefId2" + self.RandomString(8)
        fqdn = "fqdn" + self.RandomString(9)
        if self.isXmlFile(self.getModulePath()+accessTokenXmlJsonPath):

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            headers["Authorization"] = "Basic " + registrationToken

            self.updateXMLFile(accessTokenXmlJsonPath,
                               ["./identifier", "./refId1", "./refId2", "./fqdn"],
                               [identifier, refId1, refId2, fqdn])
            if expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/authTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(),
                                     expectedCode, "", "", ["accesstoken"],
                                     ["./token"], bearerAuth="Yes", outputXmlResVar=outputXmlResVar)

            elif expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/authTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(),
                                     expectedCode, "", "", ["accesstoken"],
                                     ["./token"], bearerAuth="Yes")
            elif expectedCode != None and variableList != None and xPathList != None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/authTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode, "", "",
                                     variableList, xPathList, bearerAuth="Yes")

            elif expectedCode != None and variableList != None and xPathList != None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/authTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode, "", "",
                                     variableList, xPathList, bearerAuth="Yes", outputXmlResVar=outputXmlResVar)
        elif self.isJsonFile(self.getModulePath()+accessTokenXmlJsonPath):
            self.UpdateJsonFile(accessTokenXmlJsonPath,
                                ['$..identifier', '$..refId1', '$..refId2', '$..fqdn'],
                                [identifier, refId1, refId2, fqdn])
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Basic " + registrationToken
            if expectedCode == ErrorCode.HTTP201 and variableList == None and xPathList == None:
                self.PostAuthRequest(url + '/token/api/v5/authTokens', self.UpdateJsonFileResponse, headers,
                                     currentApiFuncName(), expectedCode,"","",
                                     ["authToken", "authAccessRes"],
                                     ['$..token', '$'], bearerAuth="Yes")
                LOGGER.info(self.emsVariableList["regToken"])
                LOGGER.info(self.emsVariableList["authAccessRes"])
            elif expectedCode != None and variableList != None and xPathList != None:
                self.PostAuthRequest(url + '/token/api/v5/authTokens', self.UpdateJsonFileResponse, headers,
                                     currentApiFuncName(),
                                     expectedCode,"","", variableList, xPathList, bearerAuth="Yes")

        return self

    def getRegistrationToken(self, keyClockToken, expectedCode,resvariableList,resxPathList,id=None,identifier=None,refId1=None,refId2=None,token=None,outputXmlResVar=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Bearer " + keyClockToken
        if (id != None):
            self.GetAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens/" + id, "", headers,
                                currentApiFuncName(),
                                expectedCode, "", "",resvariableList,resxPathList,bearerAuth="Yes")
        elif(identifier != None):
            self.GetAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens?identifier" + identifier, "", headers,
                                currentApiFuncName(),
                                expectedCode, "", "",resvariableList,resxPathList,bearerAuth="Yes")
        elif (refId1 != None):
            self.GetAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens?refId1" + refId1, "",
                                headers,
                                currentApiFuncName(),
                                expectedCode, "", "", resvariableList, resxPathList, bearerAuth="Yes")
        elif (refId2 != None):
            self.GetAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens?refId2" + refId2, "",
                                headers,
                                currentApiFuncName(),
                                expectedCode, "", "", resvariableList, resxPathList, bearerAuth="Yes")
        elif (token != None):
            self.GetAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens?token=" + token, "",
                                headers, currentApiFuncName(),
                                expectedCode, "", "", bearerAuth="Yes")
        if self.getAuthApiresponse[1] == expectedCode:
            for i,resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
                LOGGER.info("enter in the get Api")

        return self

    def deleteRegistrationToken(self, keyClockToken, expectedCode,
                                resvariableList=None, resxPathList=None, id=None, identifier=None, refId1=None,
                                refId2=None, token=None, customer=None, customerId=None, outputXmlResVar=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Bearer " + keyClockToken
        if (id != None):
            self.deleteAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens/" + id, "", headers,
                                   currentApiFuncName(), expectedCode, "", "", bearerAuth="Yes")
        elif (identifier != None):
            self.deleteAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens?identifier=" + identifier, "",
                                   headers, currentApiFuncName(),
                                   expectedCode, "", "", bearerAuth="Yes")
        elif (refId1 != None):
            self.deleteAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens?refId1=" + refId1, "",
                                   headers, currentApiFuncName(),
                                   expectedCode, "", "", bearerAuth="Yes")
        elif (refId2 != None):
            self.deleteAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens?refId2=" + refId2, "",
                                   headers, currentApiFuncName(),
                                   expectedCode, "", "", bearerAuth="Yes")
        elif (token != None):
            self.deleteAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens?token=" + token, "",
                                   headers, currentApiFuncName(),
                                   expectedCode, "", "", bearerAuth="Yes")
        if self.deleteapiAuthResponse[0] == expectedCode:
            if (int(self.deleteApiresponse[0])== Constant.HTTP204):
                LOGGER.info("Contact deleted successfully")
            else:
                for i, resvar in enumerate(resvariableList):
                    LOGGER.info(resvariableList[i])
                    LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def updateAccessToken(self, accessTokenXmlJson, registrationToken, expectedCode, id=None,
                          resvariableList=None, resxPathList=None, outputXmlResVar=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Basic " + registrationToken
        if (id != None):
            self.PatchAuthRequest(url + "/token/api/v5/authTokens/" + id, accessTokenXmlJson, headers,
                                  currentApiFuncName(), Constant.HTTP200, "", "", ["authToken"], ["$..access_token"],
                                  bearerAuth="Yes")

        if self.patchAuthApiResponse[1] == expectedCode and resvariableList != None and resxPathList != None and outputXmlResVar == None:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
                LOGGER.info("enter in the put api")
        return self
