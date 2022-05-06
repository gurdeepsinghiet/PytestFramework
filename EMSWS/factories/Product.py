import  EMSWS.Constant as Constant
import logging
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
        product_json = self.UpdateJsonPath(productJsonPath, ['$.product.nameVersion.name', '$.product.nameVersion.version', '$..namespace.name', '$..productFeature[0].feature.nameVersion.name', '$..productFeature[0].feature.nameVersion.version'],
                                           [productNameGenerator + self.RandomString(9), "1.0", nameSpace_name, feature_name, feature_version])
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