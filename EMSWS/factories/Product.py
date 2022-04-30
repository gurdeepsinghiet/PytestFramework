import json
import requests
import  EMSWS.Constant as Constant
import logging
import os
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class ProductFactory(object):

    def addProductNonLVH(self,productJsonPath, productNameGenerator, nameSpace_name, feature_name, feature_version):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        productFile = open(productJsonPath, 'r')
        productFileData = productFile.read()
        product_json_object = json.loads(productFileData)
        productFile.close()
        product_json_object["product"]["namespace"]["name"] = nameSpace_name
        product_json_object["product"]["nameVersion"]["name"] = productNameGenerator + self.RandomString(9)
        product_json_object["product"]["nameVersion"]["version"] = feature_version
        product_json_object["product"]["productFeatures"]["productFeature"][0]["feature"]["nameVersion"][
            "name"] = feature_name
        product_json_object["product"]["productFeatures"]["productFeature"][0]["feature"]["nameVersion"][
            "version"] = feature_version
        productFile = open(productJsonPath, "w")
        json.dump(product_json_object, productFile)
        productFile.close()
        productFile = open(productJsonPath, 'r')
        productUpdated_json = productFile.read()
        responseProduct = requests.post(url + '/ems/api/v5/products', productUpdated_json, auth=(username, password))
        responseTextProduct = json.loads(responseProduct.text)
        LOGGER.info(responseTextProduct)
        product_name = responseTextProduct["product"]["nameVersion"]["name"]
        product_version = responseTextProduct["product"]["nameVersion"]["version"]
        feature_name = responseTextProduct["product"]["productFeatures"]["productFeature"][0]["feature"]["nameVersion"][
            "name"]
        feature_version = responseTextProduct["product"]["productFeatures"]["productFeature"][0]["feature"]["nameVersion"]["version"]
        self.ProductProperties= [product_name,product_version,feature_name, feature_version]
        return self


    def getProductProperties(self) -> list:
        return self.ProductProperties