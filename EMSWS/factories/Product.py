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

    def partialUpdateProduct(self, product_json,expectedCode,resvariableList, resxPathList,id=None,nameVersion=None,identifierNamespace =None,identifier =None,externalId =None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id !=None:
            response = self.patchRequest(url + '/ems/api/v5/products/'+id, product_json, currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        elif nameVersion !=None:
            response = self.patchRequest(url + '/ems/api/v5/products/nameVersion='+nameVersion, product_json, currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        elif identifier != None:
            response = self.patchRequest(url + '/ems/api/v5/products/identifier=' + identifier, product_json,
                                             currentApiFuncName(), expectedCode, resvariableList,resxPathList)
        elif externalId != None:
            response = self.patchRequest(url + '/ems/api/v5/products/externalId=' + externalId, product_json,
                                             currentApiFuncName(), expectedCode,resvariableList,resxPathList)
        if response[1] == expectedCode:
            for i,resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self

    def getProduct(self, resvariableList, resxPathList, expectedCode, productId=None, nameVersion=None, identifier=None, externalId=None, id=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if productId != None:
            response = self.getRequest(url + '/ems/api/v5/products/productId=' + productId, "", currentApiFuncName(),
                                       expectedCode, resvariableList, resxPathList)
        elif id != None:
            response = self.getRequest(url + '/ems/api/v5/products/' + id, "", currentApiFuncName(), expectedCode,
                                       resvariableList, resxPathList)
        elif nameVersion != None:
            response = self.getRequest(url + '/ems/api/v5/products/nameVersion=' + nameVersion, "",
                                       currentApiFuncName(), expectedCode, resvariableList, resxPathList)
        elif identifier != None:
            response = self.getRequest(url + '/ems/api/v5/products/identifier=' + identifier, "", currentApiFuncName(),
                                       expectedCode, resvariableList, resxPathList)
        elif externalId != None:
            response = self.getRequest(url + '/ems/api/v5/products/externalId=' + externalId, "", currentApiFuncName(),
                                       expectedCode, resvariableList, resxPathList)
        if response[1] == expectedCode:
            for i, resvar in enumerate(resvariableList):
                LOGGER.info(resvariableList[i])
                LOGGER.info(self.emsVariableList[resvariableList[i]])
        return self



