import  EMSWS.EMSConfig as Constant
import  EMSWS.ErrorCode as ErrorCode
import logging
from EMSWS.Utilities import UtilityClass
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class ProductFactory(object):

    def addProductNonLvh(self,nameSpaceName,featureName,featureVersion,expectedCode,outParameterList=None,outJsonPathList=None):
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(Constant.productJsonPath, ['$.product.nameVersion.name', '$.product.nameVersion.version', '$..namespace.name',
                        '$..productFeature[0].feature.nameVersion.name',
                        '$..productFeature[0].feature.nameVersion.version'], ["ptr"+self.RandomString(9), "1.0", nameSpaceName, featureName, featureVersion], ["productRes"], ['$'])
        if expectedCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/products',  self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,
                             ["product_name", "product_version", "productRes","product_feature_name","product_feature_version","productRes"],
                             ['$.product.nameVersion.name', '$.product.nameVersion.version','$..productFeatures.productFeature[0].feature.nameVersion.name',
                              '$..productFeatures.productFeature[0].feature.nameVersion.version', '$'])
            LOGGER.info(self.out_param_List["product_name"])
            LOGGER.info(self.out_param_List["product_version"])
            LOGGER.info(self.out_param_List["product_feature_name"])
            LOGGER.info(self.out_param_List["product_feature_version"])
            LOGGER.info(self.out_param_List["productRes"])
        elif (expectedCode != None and outParameterList != None and outJsonPathList != None):
            self.PostRequest(url + '/ems/api/v5/products',  self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,
                             outParameterList, outJsonPathList)

        return self

    def addProductNonLvhJsonPath(self,productjsonFilePath,productName,productVersion,nameSpaceName,featureName,featureVersion,expectedCode,outParameterList=None,outJsonPathList=None):
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        self.UpdateJsonFile(productjsonFilePath, ['$.product.nameVersion.name', '$.product.nameVersion.version', '$..namespace.name',
                        '$..productFeature[0].feature.nameVersion.name',
                        '$..productFeature[0].feature.nameVersion.version'], [productName, productVersion, nameSpaceName, featureName, featureVersion], ["productRes"], ['$'])
        if expectedCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/products',  self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,
                             ["product_name", "product_version", "productRes","product_feature_name","product_feature_version","productRes"],
                             ['$.product.nameVersion.name', '$.product.nameVersion.version','$..productFeatures.productFeature[0].feature.nameVersion.name',
                              '$..productFeatures.productFeature[0].feature.nameVersion.version', '$'])
            LOGGER.info(self.out_param_List["product_name"])
            LOGGER.info(self.out_param_List["product_version"])
            LOGGER.info(self.out_param_List["product_feature_name"])
            LOGGER.info(self.out_param_List["product_feature_version"])
            LOGGER.info(self.out_param_List["productRes"])
        elif (expectedCode != None and outParameterList != None and outJsonPathList != None):
            self.PostRequest(url + '/ems/api/v5/products',  self.UpdateJsonFileResponse, currentApiFuncName(), expectedCode,
                             outParameterList, outJsonPathList)

        return self

    def addProductNonLvhJson(self,product_json,expectedCode,outParameterList=None,outJsonPathList=None):
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if expectedCode == ErrorCode.HTTP201 and outParameterList == None and outJsonPathList == None:
            self.PostRequest(url + '/ems/api/v5/products', product_json, currentApiFuncName(), expectedCode,
                             ["product_name", "product_version", "productRes","product_feature_name","product_feature_version","productRes"],
                             ['$.product.nameVersion.name', '$.product.nameVersion.version','$..productFeatures.productFeature[0].feature.nameVersion.name',
                              '$..productFeatures.productFeature[0].feature.nameVersion.version', '$'])
            LOGGER.info(self.out_param_List["product_name"])
            LOGGER.info(self.out_param_List["product_version"])
            LOGGER.info(self.out_param_List["product_feature_name"])
            LOGGER.info(self.out_param_List["product_feature_version"])
            LOGGER.info(self.out_param_List["productRes"])
        elif (expectedCode != None and outParameterList != None and outJsonPathList != None):
            self.PostRequest(url + '/ems/api/v5/products', product_json, currentApiFuncName(), expectedCode,
                             outParameterList, outJsonPathList)

        return self

    def partialUpdateProduct(self, product_json,expectedCode,outParameterList, outJsonPathList,id=None,nameVersion=None,identifierNamespace =None,identifier =None,externalId =None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id !=None:
            self.patchRequest(url + '/ems/api/v5/products/'+id, product_json, currentApiFuncName(), expectedCode,outParameterList,outJsonPathList)
        elif nameVersion !=None:
            self.patchRequest(url + '/ems/api/v5/products/nameVersion='+nameVersion, product_json, currentApiFuncName(), expectedCode,outParameterList,outJsonPathList)
        elif identifier != None:
            self.patchRequest(url + '/ems/api/v5/products/identifier=' + identifier, product_json,
                                             currentApiFuncName(), expectedCode, outParameterList,outJsonPathList)
        elif externalId != None:
            self.patchRequest(url + '/ems/api/v5/products/externalId=' + externalId, product_json,
                                             currentApiFuncName(), expectedCode,outParameterList,outJsonPathList)
        if self.patchApiresponse[1] == expectedCode:
            for i,resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def getProduct(self, outParameterList, outJsonPathList, expectedCode, productId=None, nameVersion=None, identifier=None, externalId=None, id=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if productId != None:
            self.getRequest(url + '/ems/api/v5/products/productId=' + productId, "", currentApiFuncName(),
                                       expectedCode, outParameterList, outJsonPathList)
        elif id != None:
            self.getRequest(url + '/ems/api/v5/products/' + id, "", currentApiFuncName(), expectedCode,
                                       outParameterList, outJsonPathList)
        elif nameVersion != None:
            self.getRequest(url + '/ems/api/v5/products/nameVersion=' + nameVersion, "",
                                       currentApiFuncName(), expectedCode, outParameterList, outJsonPathList)
        elif identifier != None:
            self.getRequest(url + '/ems/api/v5/products/identifier=' + identifier, "", currentApiFuncName(),
                                       expectedCode, outParameterList, outJsonPathList)
        elif externalId != None:
            self.getRequest(url + '/ems/api/v5/products/externalId=' + externalId, "", currentApiFuncName(),
                                       expectedCode, outParameterList, outJsonPathList)
        if self.getApiresponse[1] == expectedCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def searchProduct(self, expectedCode, outParameterList, outJsonPathList, id=None, identifier=None, version=None,
                      namespaceId=None,
                      namespaceName=None, name=None, description=None, externalId=None, productType=None, refId1=None,
                      refId2=None, licenseModelName=None, licenseModelId=None, featureId=None, featureName=None,
                      state=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        responseurl = ""
        if id != None:
            responseurl = "id=" + id + "&"
        if (identifier != None):
            responseurl = "identifier=" + identifier + "&"
        if (licenseModelName != None):
            responseurl = "licenseModelName=" + licenseModelName + "&"
        if (licenseModelId != None):
            responseurl = "licenseModelId=" + licenseModelId + "&"
        if (namespaceId != None):
            responseurl = "namespaceId=" + namespaceId + "&"
        if (namespaceName != None):
            responseurl = "namespaceName=" + namespaceName + "&"
        if (name != None):
            responseurl = "name=" + name + "&"
        if (description != None):
            responseurl = "description=" + description + "&"
        if (version != None):
            responseurl = "version=" + version + "&"
        if (externalId != None):
            responseurl = "externalId=" + externalId + "&"
        if (productType != None):
            responseurl = "productType=" + productType + "&"
        if (refId1 != None):
            responseurl = "refId1=" + refId1 + "&"
        if (refId2 != None):
            responseurl = "refId2=" + refId2 + "&"
        if (featureName != None):
            responseurl = "featureName=" + featureName + "&"
        if (featureId != None):
            responseurl = "featureId" + featureId + "&"
        if (state != None):
            responseurl = "state=" + state + "&"
        LOGGER.info(url + "/ems/api/v5/products?" + responseurl[0:-1])
        self.getRequest(url + "/ems/api/v5/products?" + responseurl[0:-1], "", currentApiFuncName(),
                                   expectedCode, outParameterList, outJsonPathList)
        if self.getApiresponse[1] == expectedCode:
            for i, resvar in enumerate(outParameterList):
                LOGGER.info(outParameterList[i])
                LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def replaceProduct(self, product_json, expectedCode, outParameterList, outJsonPathList, id=None, nameVersion=None,
                       externalId=None, identifier=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.putRequest(url + '/ems/api/v5/products/' + id, product_json, currentApiFuncName(),
                                       expectedCode,outParameterList, outJsonPathList)
        elif externalId != None:
            self.putRequest(url + '/ems/api/v5/products/externalId=' + externalId, product_json,
                                       currentApiFuncName(), expectedCode,outParameterList, outJsonPathList)
        elif nameVersion != None:
            self.putRequest(url + '/ems/api/v5/products/nameVersion=' + nameVersion, product_json,
                                       currentApiFuncName(), expectedCode,outParameterList, outJsonPathList)
        elif identifier != None:
            self.putRequest(url + '/ems/api/v5/products/identifier=' + identifier, product_json,
                                       currentApiFuncName(), expectedCode,outParameterList, outJsonPathList)
            if self.putApiResponse[1] == expectedCode:
                for i, resvar in enumerate(outParameterList):
                    LOGGER.info(outParameterList[i])
                    LOGGER.info(self.out_param_List[outParameterList[i]])
        return self

    def deleteProduct(self, expectedCode,outParameterList=None, outJsonPathList=None, id=None, nameVersion=None, externalId=None, identifier=None):
        utility = UtilityClass()
        currentApiFuncName = utility.currentApiName()
        LOGGER.info(currentApiFuncName())
        if id != None:
            self.deleteRequest(url + '/ems/api/v5/products/' + id,"", currentApiFuncName(),
                            expectedCode,outParameterList,outJsonPathList)
        elif externalId != None:
            self.deleteRequest(url + '/ems/api/v5/products/externalId=' + externalId,"",
                            currentApiFuncName(), expectedCode,outParameterList,outJsonPathList)
        elif nameVersion != None:
            self.deleteRequest(url + '/ems/api/v5/products/nameVersion=' + nameVersion,"",
                            currentApiFuncName(), expectedCode,outParameterList,outJsonPathList)
        elif identifier != None:
            self.deleteRequest(url + '/ems/api/v5/products/identifier=' + identifier,"",
                            currentApiFuncName(), expectedCode,outParameterList,outJsonPathList)
        if self.deleteApiresponse[0] == expectedCode:
            if (self.deleteApiresponse[0] == ErrorCode.HTTP204):
                LOGGER.info("Product deleted successfully")
            else:
                for i, resvar in enumerate(outParameterList):
                    LOGGER.info(outParameterList[i])
                    LOGGER.info(self.out_param_List[outParameterList[i]])

        return self