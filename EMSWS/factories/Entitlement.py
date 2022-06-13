import json
from EMSWS.Utilities import UtilityClass
import requests
import  EMSWS.Constant as Constant
import logging
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class Entitlementfacory(object):

    def addEntitlementNONLVHEAWON(self,entitlementjsonPath,product_name,product_version,customerName,expectedCode,variableList=None,xPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        self.UpdateJsonFile(entitlementjsonPath, ['$..customer.name', '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.name',
                                            '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.version','$.entitlement.entitlementAsWhole'], [customerName, product_name, product_version,True], ["entitlementRes"],
                        ['$'])
        if expectedCode == Constant.HTTP201 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/entitlements', self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,["eid","entitelementid","entRes","pkId"],['$.entitlement.eId','$.entitlement.id','$','$.entitlement.productKeys.productKey[0].pkId'])
            LOGGER.info(self.emsVariableList["eid"])
            LOGGER.info(self.emsVariableList["entitelementid"])
            LOGGER.info(self.emsVariableList["entRes"])
            LOGGER.info(self.emsVariableList["pkId"])
        if expectedCode != None and variableList !=None and xPathList !=None:
            self.PostRequest(url + '/ems/api/v5/entitlements', self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,
                             variableList, xPathList)
        return self

    def createEntitlementNONLVHEAWON(self, entitlement_json, expectedCode, variableList=None, xPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()

        if expectedCode == Constant.HTTP201 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/entitlements', entitlement_json, currentApiFuncName(), expectedCode,["eid", "entitelementid", "entRes", "pkId"], ['$.entitlement.eId', '$.entitlement.id', '$',
                                                                           '$.entitlement.productKeys.productKey[0].pkId'])
            LOGGER.info(self.emsVariableList["eid"])
            LOGGER.info(self.emsVariableList["entitelementid"])
            LOGGER.info(self.emsVariableList["entRes"])
            LOGGER.info(self.emsVariableList["pkId"])
        if expectedCode != None and variableList != None and xPathList != None:
            self.PostRequest(url + '/ems/api/v5/entitlements', entitlement_json, currentApiFuncName(), expectedCode,
                             variableList, xPathList)
        return self

    def addEntitlementNONLVHEAWOFF(self,entitlementjsonPath,product_name,product_version,customerName,expectedCode,variableList=None,xPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        self.UpdateJsonFile(entitlementjsonPath, ['$..customer.name',
                                                           '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.name',
                                                           '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.version',
                                                           '$.entitlement.entitlementAsWhole'],
                            [customerName, product_name, product_version, False], ["entitlementRes"],
                            ['$'])
        if expectedCode == Constant.HTTP201 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/entitlements', self.UpdateJsonFileResponse, currentApiFuncName(),
                             expectedCode, ["eid", "entitelementid", "entRes", "pkId"],
                             ['$.entitlement.eId', '$.entitlement.id', '$',
                              '$.entitlement.productKeys.productKey[0].pkId'])
            LOGGER.info(self.emsVariableList["eid"])
            LOGGER.info(self.emsVariableList["entitelementid"])
            LOGGER.info(self.emsVariableList["entRes"])
            LOGGER.info(self.emsVariableList["pkId"])
        if expectedCode != None and variableList != None and xPathList != None:
            self.PostRequest(url + '/ems/api/v5/entitlements', self.UpdateJsonFileResponse, currentApiFuncName(),
                             expectedCode,
                             variableList, xPathList)
        return self

    def createEntitlementNONLVHEAWOFF(self, entitlement_json, expectedCode,
                                      variableList=None, xPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedCode == 201 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/entitlements', entitlement_json, currentApiFuncName(), expectedCode,
                             ["eid", "entitelementid", "entRes", "pkId"],
                             ['$.entitlement.eId', '$.entitlement.id', 'S', '$.entitlement',
                              '$.entitlement.productKeys.productKey[0].pkId'])
            LOGGER.info(self.emsVariableList["eid"])
            LOGGER.info(self.emsVariableList["entitelementid"])
            LOGGER.info(self.emsVariableList["entRes"])
        if expectedCode != None and variableList != None and xPathList != None:
            self.PostRequest(url + '/ems/api/v5/entitlements', entitlement_json, currentApiFuncName(), expectedCode,
                             variableList, xPathList)
        return self

    def addProductKeyEntitlment(productName, productVersion, eId, productKeyJsonPath,variableList=None,xPathList=None,expectedCode=None):
        productKeyFile = open(productKeyJsonPath, 'r')
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


    def partialUpdateEntitlement(self,entitlement_json,expectedCode,resvariableList, resxPathList,id=None,eId=None,externalId=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.patchRequest(url + '/ems/api/v5/entitlements/' + id, entitlement_json, currentApiFuncName(), expectedCode,
                                         resvariableList, resxPathList)
        elif eId != None:
            self.patchRequest(url + '/ems/api/v5/entitlements/eId=' + eId, entitlement_json,currentApiFuncName(), 200, resvariableList, resxPathList)
        elif externalId != None:
            self.patchRequest(url + '/ems/api/v5/entitlements/externalId =' + externalId , entitlement_json,currentApiFuncName(), 200, resvariableList, resxPathList)
        if self.patchApiResponse[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def getEntitlement(self,resvariableList,resxPathList,expectedCode,entitlementId=None, id=None, eId=None, externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if entitlementId != None:
            self.getRequest(url + '/ems/api/v5/entitlements/' + entitlementId, "",
                                           currentApiFuncName(), 200, resvariableList, resxPathList)
        elif id != None:
            self.getRequest(url + '/ems/api/v5/entitlements/' + id, "",
                                           currentApiFuncName(), 200, resvariableList, resxPathList)
        elif eId != None:
            self.getApiresponse = self.getRequest(url + '/ems/api/v5/entitlements/eId=' + eId, "",
                                           currentApiFuncName(), 200, resvariableList, resxPathList)
        elif externalId != None:
            self.getRequest(url + '/ems/api/v5/entitlements/externalId=' + externalId, "",currentApiFuncName(),200,resvariableList,resxPathList)
        if self.getApiresponse[1] == expectedCode and resvariableList !=None and resxPathList !=None:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def deleteEntitlement(self, expectedCode,resvariableList=None, resxPathList=None, id=None, eId=None, externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.deleteRequest(url + '/ems/api/v5/entitlements/' + id, "",currentApiFuncName(), expectedCode,resvariableList, resxPathList)
        elif eId != None:
            self.deleteRequest(url + '/ems/api/v5/entitlements/eId=' + eId,"", currentApiFuncName(), expectedCode,resvariableList, resxPathList)
        elif externalId != None:
            self.deleteRequest(url + '/ems/api/v5/entitlements/externalId =' + externalId,"",currentApiFuncName(), expectedCode,resvariableList, resxPathList)
        if self.deleteApiresponse[0] == expectedCode:
            if (self.deleteApiresponse[0] == Constant.HTTP204):
                LOGGER.info("Contact deleted successfully")
            else:
                for i, resvar in enumerate(resvariableList):
                    LOGGER.info(resvariableList[i])
                    LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def replaceEntitlement(self, entitlement_json, expectedCode, resvariableList, resxPathList, id=None, eId=None,
                           externalId=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.putRequest(url + '/ems/api/v5/entitlements/' + id, entitlement_json, currentApiFuncName(),
                                       expectedCode, resxPathList)
        elif eId != None:
            self.putRequest(url + '/ems/api/v5/entitlements/eId=' + eId, entitlement_json,
                                       currentApiFuncName(), expectedCode, resxPathList)
        elif externalId != None:
            self.putRequest(url + '/ems/api/v5/entitlements/externalId =' + externalId, entitlement_json,
                                       currentApiFuncName(), expectedCode, resxPathList)
        if self.putApiResponse[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

