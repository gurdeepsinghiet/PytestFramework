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

    def addEntitlementNONLVHEAWON(self,entitlement_json,product_name,product_version,customerName,expectedCode,variableList=None,xPathList=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        self.UpdateJsonFile(Constant.entitlementJsonPath, ['$..customer.name', '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.name',
                                            '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.version','$.entitlement.entitlementAsWhole'], [customerName, product_name, product_version,True], ["entitlementRes"],
                        ['$'])
        if expectedCode == 201 and variableList == None and xPathList == None:
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

        if expectedCode == 201 and variableList == None and xPathList == None:
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

    def addEntitlementNONLVHEAWOFF(self, entitlement_json, expectedCode,
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
        return

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


    def getEntitlementProperties(self)->list:
        return self.entitlementProperties


    def getDic(self)->dict:
        return {}

