import json
import requests
import  EMSWS.Constant as Constant
import logging
import os
from EMSWS.Utilities import UtilityClass
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class ProductFactory(object):

    def addProductNonLVH(self,productJsonPath, productNameGenerator, nameSpace_name, feature_name, feature_version):
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        ProductFileData = utility.readFile(productJsonPath)
        LOGGER.info(ProductFileData)
        product_json_object = utility.convertJsontoDictinary(ProductFileData)
        product_json_object["product"]["namespace"]["name"] = nameSpace_name
        product_json_object["product"]["nameVersion"]["name"] = productNameGenerator + self.RandomString(9)
        product_json_object["product"]["nameVersion"]["version"] = feature_version
        product_json_object["product"]["productFeatures"]["productFeature"][0]["feature"]["nameVersion"][
            "name"] = feature_name
        product_json_object["product"]["productFeatures"]["productFeature"][0]["feature"]["nameVersion"][
            "version"] = feature_version
        product_json = utility.convertDictinarytoJson(product_json_object)
        LOGGER.info(product_json)
        response = self.PostRequest(url + '/ems/api/v5/products', product_json, currentApiFuncName(), "201")
        if response[1] == 201 or response[1] == 204 or response[1] == 200:
            productDictinary = utility.convertJsontoDictinary(response[0])
            product_name = productDictinary["product"]["nameVersion"]["name"]
            product_version = productDictinary["product"]["nameVersion"]["version"]
            feature_name = \
            productDictinary["product"]["productFeatures"]["productFeature"][0]["feature"]["nameVersion"][
                "name"]
            feature_version = \
            productDictinary["product"]["productFeatures"]["productFeature"][0]["feature"]["nameVersion"]["version"]
            self.ProductProperties = [product_name, product_version, feature_name, feature_version]
        return self



    def getProductProperties(self) -> list:
        return self.ProductProperties