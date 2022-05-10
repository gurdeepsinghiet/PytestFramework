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

    def createEntitlementNONLVH(self,productName, productVersion, customerName, entitlementJsonPath):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        entitlement_json = self.UpdateJsonPath(entitlementJsonPath,
                                           ['$..customer.name', '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.name',
                                            '$..productKeys.productKey[0].item.itemProduct.product.nameVersion.version'],
                                           [customerName, productName, productVersion])
        responseEntitlement = self.PostRequest(url + '/ems/api/v5/entitlements', entitlement_json, currentApiFuncName(), 201)
        if responseEntitlement[1] == 201:
            entitlementDictinary = utility.convertJsontoDictinary(responseEntitlement[0])
            eid = entitlementDictinary["entitlement"]["eId"]
            id = entitlementDictinary["entitlement"]["id"]
            self.entitlementProperties = [id, eid,responseEntitlement[0]]
        return self

    def addProductKeyEntitlment(productName, productVersion, eId, productKeyJsonPath):
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

