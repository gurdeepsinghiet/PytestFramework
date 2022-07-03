import json
from EMSWS.Utilities import UtilityClass
import requests
import  EMSWS.EMSConfig as Constant
import  EMSWS.ErrorCode as ErrorCode
import logging
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class Entitlementfacory(object):

    def addEntitlementNonLVHEawOnJsonPath(self,entitlementjsonPath,product_name,product_version,customerName,expectedCode,outParameterList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        self.UpdateJsonFile(entitlementjsonPath, ['$..customer.name', '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.name',
                                            '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.version','$.entitlement.entitlementAsWhole'], [customerName, product_name, product_version,True], ["entitlementRes"],
                        ['$'])
        if expectedCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/entitlements', self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,["eid","entitelementid","entRes","pkId"],['$.entitlement.eId','$.entitlement.id','$','$.entitlement.productKeys.productKey[0].pkId'])
            LOGGER.info(self.out_param_List["eid"])
            LOGGER.info(self.out_param_List["entitelementid"])
            LOGGER.info(self.out_param_List["entRes"])
            LOGGER.info(self.out_param_List["pkId"])
        if expectedCode != None and outParameterList !=None and outJsonPathList !=None:
            self.PostRequest(url + '/ems/api/v5/entitlements', self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,
                             outParameterList, outJsonPathList)
        return self

    def addEntitlementNonLvhEawOnJson(self, entitlement_json, expectedCode, outParameterList=None, outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()

        if expectedCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/entitlements', entitlement_json, currentApiFuncName(), expectedCode,["eid", "entitelementid", "entRes", "pkId"], ['$.entitlement.eId', '$.entitlement.id', '$',
                                                                           '$.entitlement.productKeys.productKey[0].pkId'])
            LOGGER.info(self.out_param_List["eid"])
            LOGGER.info(self.out_param_List["entitelementid"])
            LOGGER.info(self.out_param_List["entRes"])
            LOGGER.info(self.out_param_List["pkId"])
        if expectedCode != None and outParameterList != None and outJsonPathList != None:
            self.PostRequest(url + '/ems/api/v5/entitlements', entitlement_json, currentApiFuncName(), expectedCode,
                             outParameterList, outJsonPathList)
        return self

    def addEntitlementNonLvhEawOffJsonPath(self,entitlementjsonPath,product_name,product_version,customerName,expectedCode,outParameterList=None,outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        self.UpdateJsonFile(self.getModulePath()+entitlementjsonPath, ['$..customer.name',
                                                           '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.name',
                                                           '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.version',
                                                           '$.entitlement.entitlementAsWhole'],
                            [customerName, product_name, product_version, False], ["entitlementRes"],
                            ['$'])
        if expectedCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/entitlements', self.UpdateJsonFileResponse, currentApiFuncName(),
                             expectedCode, ["eid", "entitelementid", "entRes", "pkId"],
                             ['$.entitlement.eId', '$.entitlement.id', '$',
                              '$.entitlement.productKeys.productKey[0].pkId'])
            LOGGER.info(self.out_param_List["eid"])
            LOGGER.info(self.out_param_List["entitelementid"])
            LOGGER.info(self.out_param_List["entRes"])
            LOGGER.info(self.out_param_List["pkId"])
        if expectedCode != None and outParameterList != None and outJsonPathList != None:
            self.PostRequest(url + '/ems/api/v5/entitlements', self.UpdateJsonFileResponse, currentApiFuncName(),
                             expectedCode,
                             outParameterList, outJsonPathList)
        return self

    def addEntitlementNonLvhEawOffJson(self, entitlement_json, expectedReturnCode,
                                      outParameterList=None, outJsonPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedReturnCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/entitlements', entitlement_json, currentApiFuncName(), expectedReturnCode,
                             ["eid", "entitelementid", "entRes", "pkId"],
                             ['$.entitlement.eId', '$.entitlement.id', 'S', '$.entitlement',
                              '$.entitlement.productKeys.productKey[0].pkId'])
            LOGGER.info(self.out_param_List["eid"])
            LOGGER.info(self.out_param_List["entitelementid"])
            LOGGER.info(self.out_param_List["entRes"])
        if expectedReturnCode != None and outParameterList != None and outJsonPathList != None:
            self.PostRequest(url + '/ems/api/v5/entitlements', entitlement_json, currentApiFuncName(), expectedReturnCode,
                             outParameterList, outJsonPathList)
        return self

    def addProductKeyEntitlment(self,productName, productVersion, eId, productKeyJsonPath,outParameterList=None,outJsonPathList=None,expectedCode=None):
        productKeyFile = open(self.getModulePath()+productKeyJsonPath, 'r')
        productKeyFileData = productKeyFile.read()
        productKey_json_object = json.loads(productKeyFileData)
        productKey_json_object["productKey"]["item"]["itemProduct"]["product"]["nameVersion"]["name"] = productName
        productKey_json_object["productKey"]["item"]["itemProduct"]["product"]["nameVersion"][
            "version"] = productVersion
        productKeyFile.close()
        json_object1 = json.dumps(productKey_json_object)
        responseEntitlement = requests.post(url + '/ems/api/v5/entitlements/eId=' + eId + '/productKeys', json_object1,
                                            auth=(username, password))
        print(responseEntitlement.text)


    def partialUpdateEntitlement(self,entitlement_json,expectedReturnCode,outParameterList, outJsonPathList,id=None,eId=None,externalId=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.patchRequest(url + '/ems/api/v5/entitlements/' + id, entitlement_json, currentApiFuncName(), expectedReturnCode,
                                         outParameterList, outJsonPathList)
        elif eId != None:
            self.patchRequest(url + '/ems/api/v5/entitlements/eId=' + eId, entitlement_json,currentApiFuncName(), expectedReturnCode, outParameterList, outJsonPathList)
        elif externalId != None:
            self.patchRequest(url + '/ems/api/v5/entitlements/externalId =' + externalId , entitlement_json,currentApiFuncName(), expectedReturnCode, outParameterList, outJsonPathList)
        if self.patchApiResponse[1] == expectedReturnCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def getEntitlement(self,outParameterList,outJsonPathList,expectedReturnCode,entitlementId=None, id=None, eId=None, externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if entitlementId != None:
            self.getRequest(url + '/ems/api/v5/entitlements/' + entitlementId, "",
                                           currentApiFuncName(), expectedReturnCode, outParameterList, outJsonPathList)
        elif id != None:
            self.getRequest(url + '/ems/api/v5/entitlements/' + id, "",
                                           currentApiFuncName(), expectedReturnCode, outParameterList, outJsonPathList)
        elif eId != None:
            self.getApiresponse = self.getRequest(url + '/ems/api/v5/entitlements/eId=' + eId, "",
                                           currentApiFuncName(), expectedReturnCode, outParameterList, outJsonPathList)
        elif externalId != None:
            self.getRequest(url + '/ems/api/v5/entitlements/externalId=' + externalId, "",currentApiFuncName(),200,outParameterList,outJsonPathList)
        if self.getApiresponse[1] == expectedReturnCode and outParameterList !=None and outJsonPathList !=None:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def deleteEntitlement(self, expectedReturnCode,outParameterList=None, outJsonPathList=None, id=None, eId=None, externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.deleteRequest(url + '/ems/api/v5/entitlements/' + id, "",currentApiFuncName(), expectedReturnCode,outParameterList, outJsonPathList)
        elif eId != None:
            self.deleteRequest(url + '/ems/api/v5/entitlements/eId=' + eId,"", currentApiFuncName(), expectedReturnCode,outParameterList, outJsonPathList)
        elif externalId != None:
            self.deleteRequest(url + '/ems/api/v5/entitlements/externalId =' + externalId,"",currentApiFuncName(), expectedReturnCode,outParameterList, outJsonPathList)
        if self.deleteApiresponse[0] == expectedReturnCode:
            if (self.deleteApiresponse[0] == ErrorCode.HTTP204):
                LOGGER.info("Entitlement deleted successfully")
            else:
                for i, resvar in enumerate(outParameterList):
                    LOGGER.info(outParameterList[i])
                    LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def replaceEntitlement(self, entitlement_json, expectedReturnCode, outParameterList, outJsonPathList, id=None, eId=None,
                           externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.putRequest(url + '/ems/api/v5/entitlements/' + id, entitlement_json, currentApiFuncName(),
                                       expectedReturnCode, outJsonPathList)
        elif eId != None:
            self.putRequest(url + '/ems/api/v5/entitlements/eId=' + eId, entitlement_json,
                                       currentApiFuncName(), expectedReturnCode, outJsonPathList)
        elif externalId != None:
            self.putRequest(url + '/ems/api/v5/entitlements/externalId =' + externalId, entitlement_json,
                                       currentApiFuncName(), expectedReturnCode, outJsonPathList)
        if self.putApiResponse[1] == expectedReturnCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

