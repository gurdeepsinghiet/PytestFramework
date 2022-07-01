from EMSWS.Utilities import UtilityClass
import  EMSWS.EMSConfig as Constant
import logging
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class RoleManagementFactory(object):
    def addRole(self,roleJsonFilePath,roleName,expectedCode,outVariableList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(roleJsonFilePath,['$.role.name'],[roleName])

        if expectedCode == Constant.HTTP201 and outVariableList == None and outJsonPathList == None:
            self.PostRequest(url+'/ems/api/v5/roles', self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,
                             ["resvar", "roleName"],["$", "$.role.name"])

        elif (expectedCode != None and outVariableList != None and outJsonPathList != None):
            self.PostRequest(url + '/ems/api/v5/roles', self.UpdateJsonFileResponse, currentApiFuncName(),
                             expectedCode, outVariableList, outJsonPathList)
        return self

    def createRole(self,role_Json,expectedCode,outVariableList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedCode == Constant.HTTP201 and outVariableList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/roles', role_Json, currentApiFuncName(), expectedCode,
            ["resvar", "roleName",],["$", "$.role.name"])
        elif (expectedCode != None and outVariableList != None and outJsonPathList != None):
            self.PostRequest(url + '/ems/api/v5/roles', self.UpdateJsonFileResponse, currentApiFuncName(),
                             expectedCode, outVariableList, outJsonPathList)
        return self


    def getRole(self, outVariableList, outJsonPathList, expectedCode, id=None, name=None):
            utility = UtilityClass()
            currentApiFuncName = utility.currentApiName()
            LOGGER.info(currentApiFuncName())
            if id != None:
                self.getRequest(url + '/ems/api/v5/roles/' + id, "", currentApiFuncName(), expectedCode,
                                outVariableList, outJsonPathList)
            elif name != None:
                self.getRequest(url + '/ems/api/v5/roles/name=' + name, "", currentApiFuncName(), expectedCode,
                                outVariableList, outJsonPathList)
            if self.getApiresponse[1] == expectedCode:
                for i, resvar in enumerate(outVariableList):
                    LOGGER.info(outVariableList[i])
                    LOGGER.info(self.emsVariableList[outVariableList[i]])
            return self

    def searchRole(self,expectedCode, outVariableList, outJsonPathList,  id=None, name=None,description=None,creationDateFrom=None,creationDateTo=None,pageStartIndex=None,pageSize=None,searchPattern=None,sortByAsc=None ,sortByDesc=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        responeurl = ""
        if (id != None):
            responeurl +="id="+id+"&"
        if (name !=None):
            responeurl +="name="+name+"&"
        if (description != None):
            responeurl +="description="+description+"&"
        if (creationDateFrom !=None):
            responeurl +="creationDateFrom"+creationDateFrom+"&"
        if (creationDateTo !=None):
            responeurl +="creationDateTo"+creationDateTo+"&"
        if (pageStartIndex !=None):
            responeurl +="pageStartIndex"+pageStartIndex+"&"
        if (pageSize !=None):
            responeurl +="pageSize"+pageSize+"&"
        if (searchPattern !=None):
            responeurl +="searchPattern"+searchPattern+"&"
        if (sortByAsc !=None):
            responeurl +="sortByAsc"+sortByAsc+"&"
        if (sortByDesc !=None):
            responeurl +="sortByDesc"+sortByDesc+"&"
        self.getRequest(url + "/ems/api/v5/roles?" + responeurl[0:-1], "", currentApiFuncName(), expectedCode,
                        outVariableList, outJsonPathList)
        if self.getApiresponse[1] == expectedCode:
               for i, resvar in enumerate(outVariableList):
                   LOGGER.info(outVariableList[i])
                   LOGGER.info(self.emsVariableList[outVariableList[i]])
        return self

    def updateRole(self,role_json,expectedCode,outVariableList, outJsonPathList,id=None,name=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.patchRequest(url + '/ems/api/v5/roles/' + id, role_json, expectedCode,outVariableList, outJsonPathList)
        elif name != None:
            self.patchRequest(url + '/ems/api/v5/roles/name=' + name, role_json,
                              expectedCode,outVariableList, outJsonPathList)
        if self.patchApiResponse[1] == expectedCode:
                for i, resvar in enumerate(outVariableList):
                    LOGGER.info(outVariableList[i])
                    LOGGER.info(self.emsVariableList[outVariableList[i]])
        return self

    def replaceRole(self,role_json,expectedCode,outVariableList, outJsonPathList,id=None,name=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.putRequest(url + '/ems/api/v5/roles/' + id, role_json,currentApiFuncName(), expectedCode,
                              outVariableList, outJsonPathList)
        elif name != None:
            self.putRequest(url + '/ems/api/v5/roles/name=' + name, role_json,currentApiFuncName(),
                              expectedCode,outVariableList, outJsonPathList)
        if self.putApiResponse[1] == expectedCode:
                for i, resvar in enumerate(outVariableList):
                    LOGGER.info(outVariableList[i])
                    LOGGER.info(self.emsVariableList[outVariableList[i]])
        return self

    def deleteRole(self, expectedCode,outVariableList=None, outJsonPathList=None, id=None, name=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.deleteRequest(url + '/ems/api/v5/roles/' + id, "", currentApiFuncName(), expectedCode,outVariableList,outJsonPathList)
        elif name != None:
            self.deleteRequest(url + '/ems/api/v5/roles/name=' + name, "", currentApiFuncName(), expectedCode,outVariableList,outJsonPathList)
        if self.deleteApiresponse[0] == expectedCode:
            if (self.deleteApiresponse[0] == Constant.HTTP204):
                LOGGER.info("Role deleted successfully")
            else:
                for i, resvar in enumerate(outVariableList):
                    LOGGER.info(outVariableList[i])
                    LOGGER.info(self.emsVariableList[outVariableList[i]])
        return self

