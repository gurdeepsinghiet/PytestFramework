import EMSWS.Constant as Constant
import logging
from EMSWS.Utilities import UtilityClass
from requests.structures import CaseInsensitiveDict
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class AuthenticationFactory(object):
    def getKeyclockToken(self,user,passwrd,realm,expectedCode,variableList = None , xPathList = None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        data = {"grant_type": Constant.grant_type, "username": user, "password": passwrd,"client_id": Constant.client_id}
        if expectedCode == 200 and variableList == None and xPathList == None:
            self.PostAuthRequest(Constant.KeyClockAuthUrl+
                "/auth/realms/"+realm+"/protocol/openid-connect/token",
                data, headers, "keyclocktokenApi", 200, user, passwrd,["access_token"],["$.access_token"])
            LOGGER.info(self.emsVariableList["access_token"])
        elif expectedCode != None and variableList != None and xPathList != None:
            self.PostAuthRequest(Constant.KeyClockAuthUrl +
                                 "/auth/realms/" + realm + "/protocol/openid-connect/token",
                                 data, headers, "keyclocktokenApi", 200, user, passwrd,variableList,xPathList)
        return self


    def addRegistrationTokenWithoutCostomer(self,regTokenXmlPath,keyClockToken,identifier,refId1,refId2,count,expectedCode,variableList = None , xPathList = None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/xml"
        headers["Content-Type"] = "application/xml"
        headers["Authorization"]= "Bearer "+keyClockToken
        self.updateXMLFile(regTokenXmlPath,
                       ["./identifier", "./refId1","./refId2","./count"],
                       [identifier,refId1,refId2,count],["regupdatedXml"],[self.xmlstroutput])
        if expectedCode == 201 and variableList == None and xPathList == None:
            self.PostAuthRequest(Constant.EMSURL+"/token/api/v5/registrationTokens",self.emsVariableList["regupdatedXmlcust"],headers,currentApiFuncName(),expectedCode,Constant.EMSUserName,Constant.EMSPassword,
                                 ["registrationtoken"],["./token"])

        elif expectedCode != None and variableList != None and xPathList != None:
            self.PostAuthRequest(Constant.EMSURL + "", self.emsVariableList["regupdatedXmlcust"], headers,
                                 currentApiFuncName(), expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                 variableList,xPathList)
        return self


    def addRegistrationTokenWithCostomer(self,regTokenXmlPath,keyClockToken,customerName,identifier,refId1,refId2,count,expectedCode,variableList = None , xPathList = None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/xml"
        headers["Content-Type"] = "application/xml"
        headers["Authorization"]= "Bearer "+keyClockToken
        self.updateXMLFile(regTokenXmlPath,
                       [".//name", "./identifier", "./refId1","./refId2","./count"],
                       [customerName,identifier,identifier, refId1,refId2,count],["regupdatedXmlcust"],[self.xmlstroutput])

        if expectedCode == 201 and variableList == None and xPathList == None:
            self.PostAuthRequest(Constant.EMSURL+"/token/api/v5/registrationTokens",self.emsVariableList["regupdatedXmlcust"],headers,currentApiFuncName(),expectedCode,
                                 Constant.EMSUserName,Constant.EMSPassword,["registrationtoken"],["./token"])

        elif expectedCode != None and variableList != None and xPathList != None:
            self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens", self.emsVariableList["regupdatedXmlcust"], headers,
                                 currentApiFuncName(), expectedCode, Constant.EMSUserName, Constant.EMSPassword,variableList,xPathList)
        return self


    def createRegistrationToken(self,regTokenXml,keyClockToken,expectedCode,variableList = None , xPathList = None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/xml"
        headers["Content-Type"] = "application/xml"
        headers["Authorization"]= "Bearer "+keyClockToken
        if expectedCode == 201 and variableList == None and xPathList == None:
            self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens",
                                 regTokenXml, headers, currentApiFuncName(), expectedCode,
                                 Constant.EMSUserName, Constant.EMSPassword, ["registrationtoken"], ["./token"])
        elif expectedCode != None and variableList != None and xPathList != None:
            self.PostAuthRequest(Constant.EMSURL + "/token/api/v5/registrationTokens",
                                 regTokenXml, headers,
                                 currentApiFuncName(), expectedCode, Constant.EMSUserName, Constant.EMSPassword,
                                 variableList, xPathList)
        return self


    def addAccessToken(self):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/xml"
        headers["Content-Type"] = "application/xml"
