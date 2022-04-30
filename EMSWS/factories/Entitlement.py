import json
import os
import requests
import  EMSWS.Constant as Constant
import logging
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class Entitlementfacory(object):

    def createEntitlementNONLVH(self,productNmae, productVesrion, customerName, entitlementJsonPath):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        entitlementFile = open(entitlementJsonPath, 'r')
        entitlemenetFileData = entitlementFile.read()
        entitlement_json_object = json.loads(entitlemenetFileData)
        entitlementFile.close()
        entitlement_json_object["entitlement"]["customer"]["name"] = customerName
        entitlement_json_object["entitlement"]["productKeys"]["productKey"][0]["item"]["itemProduct"]["product"][
            "nameVersion"]["name"] = productNmae
        entitlement_json_object["entitlement"]["productKeys"]["productKey"][0]["item"]["itemProduct"]["product"][
            "nameVersion"]["version"] = productVesrion
        json_object1 = json.dumps(entitlement_json_object)
        LOGGER.info('===============start====================')
        LOGGER.info(json_object1)
        LOGGER.info('================end===================')
        responseEntitlement = requests.post(url + '/ems/api/v5/entitlements', json_object1, auth=(username, password))
        response_entitlement = json.loads(responseEntitlement.text)
        eid = response_entitlement["entitlement"]["eId"]
        id = response_entitlement["entitlement"]["id"]
        self.entitlementProperties = [id, eid]
        LOGGER.info(eid)
        LOGGER.info(id)
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

