import  EMSWS.Constant as Constant
import logging
from EMSWS.Utilities import UtilityClass
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class ProductFactory(object):
    def addProductNonLVH(self,productjsonFilePath,productName,productVersion,nameSpaceName,featureName,featureVersion,expectedCode,variableList=None,xPathList=None):
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(productjsonFilePath, ['$.product.nameVersion.name', '$.product.nameVersion.version', '$..namespace.name',
                        '$..productFeature[0].feature.nameVersion.name',
                        '$..productFeature[0].feature.nameVersion.version'], [productName, productVersion, nameSpaceName, featureName, featureVersion], ["productRes"], ['$'])
        if expectedCode == 201 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/products',  self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,
                             ["product_name", "product_version", "productRes","product_feature_name","product_feature_version","productRes"],
                             ['$.product.nameVersion.name', '$.product.nameVersion.version','$..productFeatures.productFeature[0].feature.nameVersion.name',
                              '$..productFeatures.productFeature[0].feature.nameVersion.version', '$'])
            LOGGER.info(self.emsVariableList["product_name"])
            LOGGER.info(self.emsVariableList["product_version"])
            LOGGER.info(self.emsVariableList["product_feature_name"])
            LOGGER.info(self.emsVariableList["product_feature_version"])
            LOGGER.info(self.emsVariableList["productRes"])
        elif (expectedCode != None and expectedCode != None and xPathList != None):
            self.PostRequest(url + '/ems/api/v5/features',  self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,
                             variableList, xPathList)

        return self

    def createProductNonLVH(self,product_json,expectedCode,variableList=None,xPathList=None):
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())

        if expectedCode == 201 and variableList == None and xPathList == None:
            self.PostRequest(url + '/ems/api/v5/products', product_json, currentApiFuncName(), expectedCode,
                             ["product_name", "product_version", "productRes","product_feature_name","product_feature_version","productRes"],
                             ['$.product.nameVersion.name', '$.product.nameVersion.version','$..productFeatures.productFeature[0].feature.nameVersion.name',
                              '$..productFeatures.productFeature[0].feature.nameVersion.version', '$'])
            LOGGER.info(self.emsVariableList["product_name"])
            LOGGER.info(self.emsVariableList["product_version"])
            LOGGER.info(self.emsVariableList["product_feature_name"])
            LOGGER.info(self.emsVariableList["product_feature_version"])
            LOGGER.info(self.emsVariableList["productRes"])
        elif (expectedCode != None and expectedCode != None and xPathList != None):
            self.PostRequest(url + '/ems/api/v5/features', product_json, currentApiFuncName(), expectedCode,
                             variableList, xPathList)

        return self




    def getProductProperties(self) -> list:
        return self.ProductProperties