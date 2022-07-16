from EMSWS.Utilities import UtilityClass
import  EMSWS.EMSConfig as Constant
import  EMSWS.ErrorCode as ErrorCode
import logging
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class RoleManagementFactory(object):
    def addRoleJsonFilePath(self,roleJsonFilePath,roleName,expectedCode,outParameterList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(roleJsonFilePath,['$.role.name'],[roleName])

        if expectedCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url+'/ems/api/v5/roles', self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,
                             ["resvar", "roleName"],["$", "$.role.name"])

        elif expectedCode != None and outParameterList != None and outJsonPathList != None:
            self.PostRequest(url + '/ems/api/v5/roles', self.UpdateJsonFileResponse, currentApiFuncName(),
                             expectedCode, outParameterList, outJsonPathList)
        return self

    def addRoleJson(self,role_Json,expectedCode,outParameterList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/roles', role_Json, currentApiFuncName(), expectedCode,
            ["resvar", "roleName",],["$", "$.role.name"])
        elif (expectedCode != None and outParameterList != None and outJsonPathList != None):
            self.PostRequest(url + '/ems/api/v5/roles', self.UpdateJsonFileResponse, currentApiFuncName(),
                             expectedCode, outParameterList, outJsonPathList)
        return self


    def getRole(self, outParameterList, outJsonPathList, expectedCode, id=None, name=None):
            utility = UtilityClass()
            currentApiFuncName = utility.currentApiName()
            LOGGER.info(currentApiFuncName())
            if id != None:
                self.getRequest(url + '/ems/api/v5/roles/' + id, "", currentApiFuncName(), expectedCode,
                                outParameterList, outJsonPathList)
            elif name != None:
                self.getRequest(url + '/ems/api/v5/roles/name=' + name, "", currentApiFuncName(), expectedCode,
                                outParameterList, outJsonPathList)
            if self.getApiresponse[1] == expectedCode:
                for i, resvar in enumerate(outParameterList):
                    LOGGER.info(outParameterList[i])
                    LOGGER.info(self.out_param_List[outParameterList[i]])
            return self

    def searchRole(self,expectedCode, outParameterList, outJsonPathList,  id=None, name=None,description=None,creationDateFrom=None,creationDateTo=None,pageStartIndex=None,pageSize=None,searchPattern=None,sortByAsc=None ,sortByDesc=None):
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
                        outParameterList, outJsonPathList)
        if self.getApiresponse[1] == expectedCode:
               for i, resvar in enumerate(outParameterList):
                   LOGGER.info(outParameterList[i])
                   LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def updateRole(self,role_json,expectedCode,outParameterList, outJsonPathList,id=None,name=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.patchRequest(url + '/ems/api/v5/roles/' + id, role_json, expectedCode,outParameterList, outJsonPathList)
        elif name != None:
            self.patchRequest(url + '/ems/api/v5/roles/name=' + name, role_json,
                              expectedCode,outParameterList, outJsonPathList)
        if self.patchApiResponse[1] == expectedCode:
                for i, resvar in enumerate(outParameterList):
                    LOGGER.info(outParameterList[i])
                    LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def replaceRole(self,role_json,expectedCode,outParameterList, outJsonPathList,id=None,name=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.putRequest(url + '/ems/api/v5/roles/' + id, role_json,currentApiFuncName(), expectedCode,
                              outParameterList, outJsonPathList)
        elif name != None:
            self.putRequest(url + '/ems/api/v5/roles/name=' + name, role_json,currentApiFuncName(),
                              expectedCode,outParameterList, outJsonPathList)
        if self.putApiResponse[1] == expectedCode:
                for i, resvar in enumerate(outParameterList):
                    LOGGER.info(outParameterList[i])
                    LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def deleteRole(self, expectedCode,outParameterList=None, outJsonPathList=None, id=None, name=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.deleteRequest(url + '/ems/api/v5/roles/' + id, "", currentApiFuncName(), expectedCode,outParameterList,outJsonPathList)
        elif name != None:
            self.deleteRequest(url + '/ems/api/v5/roles/name=' + name, "", currentApiFuncName(), expectedCode,outParameterList,outJsonPathList)
        if self.deleteApiresponse[0] == expectedCode:
            if (self.deleteApiresponse[0] == ErrorCode.HTTP204):
                LOGGER.info("Role deleted successfully")
            else:
                for i, resvar in enumerate(outParameterList):
                    LOGGER.info(outParameterList[i])
                    LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

