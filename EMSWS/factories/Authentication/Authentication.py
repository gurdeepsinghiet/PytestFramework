import EMSWS.Constant as Constant
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
        self.getIDPConfiguration(Constant.HTTP200,["realm","tokenEndpoint","clientId"],["$..realm","$..tokenEndpoint","$..clientId"])
        data = {"grant_type": Constant.grant_type, "username": user, "password": passwrd,
                "client_id": self.emsVariableList["clientId"]}
        if expectedCode == Constant.HTTP200 and variableList == None and xPathList == None:
            self.PostAuthRequest(Constant.KeyClockAuthUrl+
                "/auth/realms/"+self.emsVariableList["realm"]+"/protocol/openid-connect/token",
                data, headers, "keyclocktokenApi", 200, user, passwrd,["access_token"],["$.access_token"],bearerAuth="Yes")
            LOGGER.info(self.emsVariableList["access_token"])
        elif expectedCode != None and variableList != None and xPathList != None:
            self.PostAuthRequest(Constant.KeyClockAuthUrl +
                                 "/auth/realms/" + self.emsVariableList["realm"] + "/protocol/openid-connect/token",
                                 data, headers, "keyclocktokenApi", 200, user, passwrd,variableList,xPathList,bearerAuth="Yes")
        return self


    def addRegistrationTokenWithoutCostomer(self,regTokenXmlJsonPath,keyClockToken,identifier,refId1,refId2,count,expectedCode,variableList =None,xPathList = None,outputXmlResVar=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if self.isXml(regTokenXmlJsonPath):
            self.updateXMLFile(regTokenXmlJsonPath,
                               ["./identifier", "./refId1", "./refId2", "./count"],
                               [identifier, refId1, refId2, count])

            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + keyClockToken
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            if expectedCode == Constant.HTTP201 and variableList == None and xPathList == None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(),
                                     expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                     ["registrationtoken"], ["./token"], bearerAuth="Yes",
                                     outputXmlResVar=outputXmlResVar)

            elif expectedCode == Constant.HTTP201 and variableList == None and xPathList == None and outputXmlResVar == None:
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
        elif self.isJson(regTokenXmlJsonPath):
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + keyClockToken
            self.UpdateJsonFile(regTokenXmlJsonPath,
                                ['$..identifier', '$..refId1', '$..refId2', '$..count'],
                                [identifier, refId1, refId2, count])
            if expectedCode == Constant.HTTP201 and variableList == None and xPathList == None:
                self.PostAuthRequest(url + '/token/api/v5/registrationTokens', self.UpdateJsonFileResponse, headers,currentApiFuncName(), 201,"","",
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
        if self.isXmlFile(regTokenXmlJsonPath):
            self.updateXMLFile(regTokenXmlJsonPath,
                               ["./identifier", "./refId1", "./refId2", "./count"],
                               [identifier, refId1, refId2, count])
            headers = CaseInsensitiveDict()
            headers["Authorization"] = f'Bearer {keyClockToken}'
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            LOGGER.info(self.xmlstroutput)
            if expectedCode == Constant.HTTP201 and variableList == None and xPathList == None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode, "", "",
                                     ["registrationtoken"], ["./token"], bearerAuth="Yes")
            elif expectedCode == Constant.HTTP201 and variableList == None and xPathList == None and outputXmlResVar != None:
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
        elif self.isJsonFile(regTokenXmlJsonPath):
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + keyClockToken
            self.UpdateJsonFile(regTokenXmlJsonPath,
                                ['$..identifier', '$..refId1', '$..refId2', '$..count'],
                                [identifier, refId1, refId2, count])
            if expectedCode == Constant.HTTP201 and variableList == None and xPathList == None:
                self.PostAuthRequest(url + '/token/api/v5/registrationTokens', self.UpdateJsonFileResponse, headers,
                                     currentApiFuncName(), 201,"","",
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
        if self.isXmlFile(regTokenXmlJsonPath):
            self.updateXMLFile(regTokenXmlJsonPath,
                               [".//name", "./identifier", "./refId1", "./refId2", "./count"],
                               [customerName, identifier, identifier, refId1, refId2, count])
            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            headers["Authorization"] = "Bearer " + keyClockToken
            if expectedCode == 201 and variableList == None and xPathList == None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode,
                                     Constant.EMSUserName, Constant.EMSPassword,
                                     ["registrationtoken"], ["./token"], bearerAuth="Yes")
            elif expectedCode == 201 and variableList == None and xPathList == None and outputXmlResVar != None:
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
        elif self.isJsonFile(regTokenXmlJsonPath):
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + keyClockToken
            self.UpdateJsonFile(regTokenXmlJsonPath,
                                ['$..name','$..identifier', '$..refId1', '$..refId2', '$..count'],
                                [customerName,identifier, refId1, refId2, count])
            if expectedCode == Constant.HTTP201 and variableList == None and xPathList == None:
                self.PostAuthRequest(url + '/token/api/v5/registrationTokens', self.UpdateJsonFileResponse, headers,
                                     currentApiFuncName(), 201,"","",
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
        if self.isXmlFile(regTokenXmlJsonPath):
            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            headers["Authorization"] = "Bearer " + keyClockToken

            self.updateXMLFile(regTokenXmlJsonPath,
                               [".//name", "./identifier", "./refId1", "./refId2", "./count"],
                               [customerName, identifier, identifier, refId1, refId2, count])

            if expectedCode == Constant.HTTP201 and variableList == None and xPathList == None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(), expectedCode,
                                     Constant.EMSUserName, Constant.EMSPassword, ["registrationtoken"], ["./token"],
                                     bearerAuth="Yes")

            elif expectedCode == Constant.HTTP201 and variableList == None and xPathList == None and outputXmlResVar != None:
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
        elif self.isJsonFile(regTokenXmlJsonPath):
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + keyClockToken
            self.UpdateJsonFile(regTokenXmlJsonPath,
                                ['$..name','$..identifier', '$..refId1', '$..refId2', '$..count'],
                                [customerName,identifier, refId1, refId2, count])
            if expectedCode == Constant.HTTP201 and variableList == None and xPathList == None:
                self.PostAuthRequest(url + '/token/api/v5/registrationTokens', self.UpdateJsonFileResponse, headers,
                                     currentApiFuncName(), 201,"","",
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
            if expectedCode == Constant.HTTP201 and variableList == None and xPathList == None and outputXmlResVar == None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", regTokenXmlJson, headers,
                                     currentApiFuncName(), expectedCode,
                                     Constant.EMSUserName, Constant.EMSPassword, ["registrationtoken"], ["./token"],
                                     bearerAuth="Yes")

            elif expectedCode == Constant.HTTP201 and variableList == None and xPathList == None and outputXmlResVar != None:
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
        elif self.isJsonFile(regTokenXmlJson):
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer " + keyClockToken
            if expectedCode == Constant.HTTP201 and variableList == None and xPathList == None:
                self.PostAuthRequest(url + '/token/api/v5/registrationTokens', regTokenXmlJson, headers,
                                     currentApiFuncName(), 201,"","",
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
        if self.isXmlFile(accessTokenXmlJsonPath):
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            headers["Authorization"] = "Basic " + registrationToken

            self.updateXMLFile(accessTokenXmlJsonPath,
                               ["./identifier", "./refId1", "./refId2", "./fqdn"],
                               [identifier, refId1, refId2, fqdn], ["acessTokenupdatedXml"], [self.xmlstroutput])
            if expectedCode == Constant.HTTP201 and variableList == None and xPathList == None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/authTokens",
                                     self.emsVariableList["acessTokenupdatedXml"], headers, currentApiFuncName(),
                                     expectedCode, Constant.EMSUserName, Constant.EMSPassword, ["accesstoken"],
                                     ["./token"], bearerAuth="Yes", outputXmlResVar=outputXmlResVar)
            elif expectedCode == Constant.HTTP201 and variableList == None and xPathList == None and outputXmlResVar != None:
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
        elif self.isJsonFile(accessTokenXmlJsonPath):
            self.UpdateJsonFile(accessTokenXmlJsonPath,
                                ['$..identifier', '$..refId1', '$..refId2', '$..fqdn'],
                                [identifier, refId1, refId2, fqdn])
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Basic " + registrationToken
            if expectedCode == 201 and variableList == None and xPathList == None:
                self.PostAuthRequest(url + '/token/api/v5/authTokens', self.UpdateJsonFileResponse, headers,
                                     currentApiFuncName(), 201,"","",
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
        if self.isXmlFile(accessTokenXmlJsonPath):

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/xml"
            headers["Accept"] = "application/xml"
            headers["Authorization"] = "Basic " + registrationToken

            self.updateXMLFile(accessTokenXmlJsonPath,
                               ["./identifier", "./refId1", "./refId2", "./fqdn"],
                               [identifier, refId1, refId2, fqdn])
            if expectedCode == Constant.HTTP201 and variableList == None and xPathList == None and outputXmlResVar != None:
                self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/authTokens", self.xmlstroutput, headers,
                                     currentApiFuncName(),
                                     expectedCode, "", "", ["accesstoken"],
                                     ["./token"], bearerAuth="Yes", outputXmlResVar=outputXmlResVar)

            elif expectedCode == Constant.HTTP201 and variableList == None and xPathList == None and outputXmlResVar == None:
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
        elif self.isJsonFile(accessTokenXmlJsonPath):
            self.UpdateJsonFile(accessTokenXmlJsonPath,
                                ['$..identifier', '$..refId1', '$..refId2', '$..fqdn'],
                                [identifier, refId1, refId2, fqdn])
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Basic " + registrationToken
            if expectedCode == 201 and variableList == None and xPathList == None:
                self.PostAuthRequest(url + '/token/api/v5/authTokens', self.UpdateJsonFileResponse, headers,
                                     currentApiFuncName(), 201,"","",
                                     ["authToken", "authAccessRes"],
                                     ['$..token', '$'], bearerAuth="Yes")
                LOGGER.info(self.emsVariableList["regToken"])
                LOGGER.info(self.emsVariableList["authAccessRes"])
            elif expectedCode != None and variableList != None and xPathList != None:
                self.PostAuthRequest(url + '/token/api/v5/authTokens', self.UpdateJsonFileResponse, headers,
                                     currentApiFuncName(),
                                     expectedCode,"","", variableList, xPathList, bearerAuth="Yes")

        return self

    def getRegistrationToken(self, keyClockToken, expectedCode,resvariableList,resxPathList,id=None,refId1=None,outputXmlResVar=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Bearer " + keyClockToken
        if (id != None):
            self.GetAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens/" + id, "", headers,
                                currentApiFuncName(),
                                Constant.HTTP200, "", "",resvariableList,resxPathList,bearerAuth="Yes")
        elif(refId1 != None):
            self.GetAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens/refId1" + refId1, "", headers,
                                currentApiFuncName(),
                                Constant.HTTP200, "", "",resvariableList,resxPathList,bearerAuth="Yes")
        if self.getAuthApiresponse[1] == expectedCode:
            for i,resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
                LOGGER.info("enter in the get Api")

        self