from EMSWS.Utilities import UtilityClass
import  EMSWS.EMSConfig as Constant
import logging
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class UserManagementFactory(object):
    def addUser(self, userJsonFilePath,loginId,userName,userEmailId,userPassword,userType,userState,expectedCode,outVariableList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(userJsonFilePath,["$.user.loginId","$.user.name","$..emailId","$..password","$..userType","$..userState"],
                            [loginId,userName,userEmailId,userPassword,userType,userState])
        if expectedCode == 201 and outVariableList == None and outJsonPathList == None:
            self.PostRequest(url +'/ems/api/v5/users', self.UpdateJsonFileResponse,currentApiFuncName(),
                             expectedCode,["resvar","userName","userId","userEmailId","userType","userState"],
            ["$", "$.user.name", "$..id", "$..emailId", "$..userType", "$..state"])

        elif (expectedCode != None and outVariableList != None and outJsonPathList != None):
            self.PostRequest(url + '/ems/api/v5/users', self.UpdateJsonFileResponse, currentApiFuncName(),
                             expectedCode, outVariableList, outJsonPathList)
        return self

    def createUser(self,user_Json,expectedCode,outVariableList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedCode == 201 and outVariableList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/users', user_Json, currentApiFuncName(), expectedCode,
            ["resvar", "userName", "userId", "userEmailId", "userPassword", "userType", "userState"],
            ["$", "$.user.name", "$..id", "$..emailid", "$..password", "$..usertype", "$..userState"])
            # LOGGER.info(self.emsVariableList["userName"])
            # LOGGER.info(self.emsVariableList["userEmailId"])
            # LOGGER.info(self.emsVariableList["userPassword"])
            # LOGGER.info(self.emsVariableList["userType"])
            # LOGGER.info(self.emsVariableList["userState"])
        elif (expectedCode != None and outVariableList != None and outJsonPathList != None):
            self.PostRequest(url + '/ems/api/v5/users', self.UpdateJsonFileResponse, currentApiFuncName(),
                             expectedCode, outVariableList, outJsonPathList)
            return self

    def getUser(self,outVariableList,outJsonPathList,expectedCode,id=None,emailid=None,loginId=None,externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id!=None:
            self.getRequest(url + '/ems/api/v5/users/' + id, "", currentApiFuncName(), expectedCode,
                            outVariableList, outJsonPathList)
        elif emailid!=None:
            self.getRequest(url + '/ems/api/v5/users/emailid=' + emailid, "", currentApiFuncName(), expectedCode,
                            outVariableList, outJsonPathList)
        elif loginId!=None:
            self.getRequest(url + '/ems/api/v5/users/loginId=' + loginId, "", currentApiFuncName(), expectedCode,
                            outVariableList, outJsonPathList)
        elif externalId != None:
                self.getRequest(url + '/ems/api/v5/users/externalId=' + externalId, "", currentApiFuncName(), expectedCode,
                                outVariableList, outJsonPathList)
        if self.getApiresponse[1] == expectedCode:
            for i, resvar in enumerate(outVariableList):
                LOGGER.info(outVariableList[i])
                LOGGER.info(self.emsVariableList[outVariableList[i]])
        return self

    def searchUser(self,expectedCode,outVariableList,outJsonPathList,id=None, state=None, roleName=None,loginId=None, name=None,
                      marketGroupName=None,emailId =None,refId1=None, refId2=None,externalId =None,creationDateFrom=None,creationDateTo=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        responeurl = ""
        if (id != None):
            responeurl +="id="+id+"&"
        if (name != None):
            responeurl +="name="+name+"&"
        if (state != None):
            responeurl +="state="+state+"&"
        if (roleName != None):
            responeurl +="roleName="+roleName+"&"
        if (loginId != None):
            responeurl += "loginId=" + loginId + "&"
        if (roleName != None):
            responeurl += "marketGroupName=" + marketGroupName + "&"
        if (emailId != None):
            responeurl += "emailId=" + emailId + "&"
        if (refId1 != None):
            responeurl += "refId1=" + refId1 + "&"
        if (refId2 != None):
            responeurl += "refId2=" + refId2 + "&"
        if (externalId != None):
            responeurl += "externalId=" + externalId + "&"
        if (creationDateFrom != None):
            responeurl += "creationDateFrom=" + creationDateFrom + "&"
        if (creationDateTo != None):
            responeurl += "creationDateTo=" + creationDateTo + "&"
        self.getRequest(url + "/ems/api/v5/users?" + responeurl[0:-1], "", currentApiFuncName(), expectedCode,
                            outVariableList, outJsonPathList)
        if self.getApiresponse[1] == expectedCode:
                for i, resvar in enumerate(outVariableList):
                    LOGGER.info(outVariableList[i])
                    LOGGER.info(self.emsVariableList[outVariableList[i]])
        return self

    def updateUser(self,user_json,expectedCode,outVariableList, outJsonPathList,id=None,emailid=None,loginId=None,externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.patchRequest(url + '/ems/api/v5/users/' + id,user_json, currentApiFuncName(), expectedCode,
                            outVariableList, outJsonPathList)
        elif emailid != None:
            self.patchRequest(url + '/ems/api/v5/users/emailid=' + emailid,user_json, currentApiFuncName(), expectedCode,
                            outVariableList, outJsonPathList)
        elif loginId != None:
            self.patchRequest(url + '/ems/api/v5/users/loginId=' + loginId, user_json,currentApiFuncName(), expectedCode,
                            outVariableList, outJsonPathList)
        elif externalId != None:
            self.patchRequest(url + '/ems/api/v5/users/externalId=' + externalId,user_json, currentApiFuncName(), expectedCode,
                            outVariableList, outJsonPathList)
        if self.patchApiresponse[1] == expectedCode:
                for i, resvar in enumerate(outVariableList):
                    LOGGER.info(outVariableList[i])
                    LOGGER.info(self.emsVariableList[outVariableList[i]])
        return self

    def replaceUser(self, user_json, expectedCode, outVariableList, outJsonPathList, id=None, emailid=None, loginId=None, externalId=None):
         utility = UtilityClass()
         currentApiFuncName = utility.currentApiName()
         LOGGER.info(currentApiFuncName())
         if id != None:
             self.putRequest(url + '/ems/api/v5/users/' + id, user_json, currentApiFuncName(), expectedCode,
                                outVariableList, outJsonPathList)
         elif emailid != None:
               self.putRequest(url + '/ems/api/v5/users/emailid=' + emailid, user_json, currentApiFuncName(),
                                expectedCode,outVariableList, outJsonPathList)
         elif loginId != None:
               self.putRequest(url + '/ems/api/v5/users/loginId=' + loginId, user_json, currentApiFuncName(),
                                expectedCode, outVariableList, outJsonPathList)
         elif externalId != None:
               self.putRequest(url + '/ems/api/v5/users/externalId=' + externalId, user_json, currentApiFuncName(),
                                expectedCode,outVariableList, outJsonPathList)
         if self.putApiresponse[1] == expectedCode:
             for i, resvar in enumerate(outVariableList):
                 LOGGER.info(outVariableList[i])
                 LOGGER.info(self.emsVariableList[outVariableList[i]])
         return self

    def deleteUser(self, expectedCode,outVariableList=None, outJsonPathList=None, id=None, emailId=None, loginId=None, externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.deleteRequest(url + '/ems/api/v5/users/' + id, "", currentApiFuncName(), expectedCode,outVariableList, outJsonPathList)
        elif emailId != None:
            self.deleteRequest(url + '/ems/api/v5/users/emailId=' + emailId, "", currentApiFuncName(), expectedCode,outVariableList, outJsonPathList)
        elif loginId != None:
            self.deleteRequest(url + '/ems/api/v5/users/loginId=' + loginId, "", currentApiFuncName(), expectedCode,outVariableList, outJsonPathList)
        elif externalId != None:
            self.deleteRequest(url + '/ems/api/v5/users/externalId=' + externalId, "", currentApiFuncName(),
                               expectedCode,outVariableList, outJsonPathList)
        if self.deleteApiresponse[0] == expectedCode:
            if (self.deleteApiresponse[0] == 204):
                LOGGER.info("User deleted successfully")
            else:
                for i, resvar in enumerate(outVariableList):
                    LOGGER.info(outVariableList[i])
                    LOGGER.info(self.emsVariableList[outVariableList[i]])
        return self
