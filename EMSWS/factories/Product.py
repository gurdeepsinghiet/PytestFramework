import EMSWS.EMSConfig as Constant
import EMSWS.ErrorCode as ErrorCode
import EMSWS.JsonPath as JsonPath
import logging
from EMSWS.Utilities import UtilityClass

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class ProductFactory(object):

    def add_product_non_lvh(self, namespace_name, feature_name, feature_version, expected_return_code,
                            out_parameter_list=None, out_json_path_list=None):
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(JsonPath.productJsonPath,
                            ['$.product.nameVersion.name', '$.product.nameVersion.version', '$..namespace.name',
                             '$..productFeature[0].feature.nameVersion.name',
                             '$..productFeature[0].feature.nameVersion.version'],
                            ["ptr" + self.RandomString(9), "1.0", namespace_name, feature_name, feature_version],
                            ["productRes"], ['$'])
        if expected_return_code == ErrorCode.HTTP201 and out_parameter_list is None and out_json_path_list is None:
            self.PostRequest(url + '/ems/api/v5/products', self.UpdateJsonFileResponse, current_api_name(),
                             expected_return_code,
                             ["product_name", "product_version", "productRes", "product_feature_name",
                              "product_feature_version", "productRes"],
                             ['$.product.nameVersion.name', '$.product.nameVersion.version',
                              '$..productFeatures.productFeature[0].feature.nameVersion.name',
                              '$..productFeatures.productFeature[0].feature.nameVersion.version', '$'])
            LOGGER.info(self.out_param_List["product_name"])
            LOGGER.info(self.out_param_List["product_version"])
            LOGGER.info(self.out_param_List["product_feature_name"])
            LOGGER.info(self.out_param_List["product_feature_version"])
            LOGGER.info(self.out_param_List["productRes"])
        elif (expected_return_code is not None and out_parameter_list is not None and out_json_path_list is not None):
            self.PostRequest(url + '/ems/api/v5/products', self.UpdateJsonFileResponse, current_api_name(),
                             expected_return_code,
                             out_parameter_list, out_json_path_list)

        return self

    def add_product_non_lvh_json_file_path(self, product_json_file_path, product_name, product_version, namespace_name,
                                           feature_name,
                                           feature_version, expected_return_code, out_parameter_list=None,
                                           out_json_path_list=None):
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(product_json_file_path,
                            ['$.product.nameVersion.name', '$.product.nameVersion.version', '$..namespace.name',
                             '$..productFeature[0].feature.nameVersion.name',
                             '$..productFeature[0].feature.nameVersion.version'],
                            [product_name, product_version, namespace_name, feature_name, feature_version],
                            ["productRes"],
                            ['$'])
        if expected_return_code == ErrorCode.HTTP201 and out_parameter_list is None and out_json_path_list is None:
            self.PostRequest(url + '/ems/api/v5/products', self.UpdateJsonFileResponse, current_api_name(),
                             expected_return_code,
                             ["product_name", "product_version", "productRes", "product_feature_name",
                              "product_feature_version", "productRes"],
                             ['$.product.nameVersion.name', '$.product.nameVersion.version',
                              '$..productFeatures.productFeature[0].feature.nameVersion.name',
                              '$..productFeatures.productFeature[0].feature.nameVersion.version', '$'])
            LOGGER.info(self.out_param_List["product_name"])
            LOGGER.info(self.out_param_List["product_version"])
            LOGGER.info(self.out_param_List["product_feature_name"])
            LOGGER.info(self.out_param_List["product_feature_version"])
            LOGGER.info(self.out_param_List["productRes"])
        elif expected_return_code is not None and out_parameter_list is not None and out_json_path_list is not None:
            self.PostRequest(url + '/ems/api/v5/products', self.UpdateJsonFileResponse, current_api_name(),
                             expected_return_code,
                             out_parameter_list, out_json_path_list)

        return self

    def add_product_non_lvh_json(self, product_json, expected_return_code, out_parameter_list=None,
                                 out_json_path_list=None):
        utility = UtilityClass()
        running_testcases = utility.runningPytestCaseName()
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if expected_return_code == ErrorCode.HTTP201 and out_parameter_list is None and out_json_path_list is None:
            self.PostRequest(url + '/ems/api/v5/products', product_json, current_api_name(), expected_return_code,
                             ["product_name", "product_version", "productRes", "product_feature_name",
                              "product_feature_version", "productRes"],
                             ['$.product.nameVersion.name', '$.product.nameVersion.version',
                              '$..productFeatures.productFeature[0].feature.nameVersion.name',
                              '$..productFeatures.productFeature[0].feature.nameVersion.version', '$'])
            LOGGER.info(self.out_param_List["product_name"])
            LOGGER.info(self.out_param_List["product_version"])
            LOGGER.info(self.out_param_List["product_feature_name"])
            LOGGER.info(self.out_param_List["product_feature_version"])
            LOGGER.info(self.out_param_List["productRes"])
        elif expected_return_code is not None and out_parameter_list is not None and out_json_path_list is not None:
            self.PostRequest(url + '/ems/api/v5/products', product_json, current_api_name(), expected_return_code,
                             out_parameter_list, out_json_path_list)

        return self

    def partial_update_product(self, product_json, expected_return_code, out_parameter_list, out_json_path_list,
                               id=None,
                               name_version=None, identifier_namespace=None, identifier=None, external_id=None):
        # getting the name of Current Running Test cases
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if id is not None:
            self.patchRequest(url + '/ems/api/v5/products/' + id, product_json, current_api_name(),
                              expected_return_code,
                              out_parameter_list, out_json_path_list)
        elif name_version is not None:
            self.patchRequest(url + '/ems/api/v5/products/nameVersion=' + name_version, product_json,
                              current_api_name(),
                              expected_return_code, out_parameter_list, out_json_path_list)
        elif identifier is not None:
            self.patchRequest(url + '/ems/api/v5/products/identifier=' + identifier, product_json,
                              current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif external_id is not None:
            self.patchRequest(url + '/ems/api/v5/products/externalId=' + external_id, product_json,
                              current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        if self.patchApiresponse[1] == expected_return_code:
            for i, out_param in enumerate(out_parameter_list):
                LOGGER.info(out_parameter_list[i])
                LOGGER.info(self.out_param_List[out_parameter_list[i]])
        return self

    def get_product(self, out_parameter_list, out_json_path_list, expected_return_code, product_id=None,
                    name_version=None,
                    identifier=None, external_id=None, id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if product_id is not None:
            self.getRequest(url + '/ems/api/v5/products/productId=' + product_id, "", current_api_name(),
                            expected_return_code, out_parameter_list, out_json_path_list)
        elif id is not None:
            self.getRequest(url + '/ems/api/v5/products/' + id, "", current_api_name(), expected_return_code,
                            out_parameter_list, out_json_path_list)
        elif name_version is not None:
            self.getRequest(url + '/ems/api/v5/products/nameVersion=' + name_version, "",
                            current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif identifier is not None:
            self.getRequest(url + '/ems/api/v5/products/identifier=' + identifier, "", current_api_name(),
                            expected_return_code, out_parameter_list, out_json_path_list)
        elif external_id is not None:
            self.getRequest(url + '/ems/api/v5/products/externalId=' + external_id, "", current_api_name(),
                            expected_return_code, out_parameter_list, out_json_path_list)
        if self.getApiresponse[1] == expected_return_code:
            for i, out_param in enumerate(out_parameter_list):
                LOGGER.info(out_parameter_list[i])
                LOGGER.info(self.out_param_List[out_parameter_list[i]])
        return self

    def search_product(self, expected_return_code, out_parameter_list, out_json_path_list, id=None, identifier=None,
                       version=None,
                       namespace_id=None,
                       namespace_name=None, name=None, description=None, external_id=None, product_type=None, ref_id1=None,
                       ref_id2=None, license_model_name=None, license_model_id=None, feature_id=None, feature_name=None,
                       state=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url = "id=" + id + "&"
        if identifier is not None:
            request_url = "identifier=" + identifier + "&"
        if license_model_name is not None:
            request_url = "licenseModelName=" + license_model_name + "&"
        if license_model_id is not None:
            request_url = "licenseModelId=" + license_model_id + "&"
        if namespace_id is not None:
            request_url = "namespaceId=" + namespace_id + "&"
        if namespace_name is not None:
            request_url = "namespaceName=" + namespace_name + "&"
        if name is not None:
            request_url = "name=" + name + "&"
        if description is not None:
            request_url = "description=" + description + "&"
        if version is not None:
            request_url = "version=" + version + "&"
        if external_id is not None:
            request_url = "externalId=" + external_id + "&"
        if product_type is not None:
            request_url = "productType=" + product_type + "&"
        if ref_id1 is not None:
            request_url = "refId1=" + ref_id1 + "&"
        if ref_id2 is not None:
            request_url = "refId2=" + ref_id2 + "&"
        if feature_name is not None:
            request_url = "featureName=" + feature_name + "&"
        if feature_id is not None:
            request_url = "featureId" + feature_id + "&"
        if state is not None:
            request_url = "state=" + state + "&"
        LOGGER.info(url + "/ems/api/v5/products?" + request_url[0:-1])
        self.getRequest(url + "/ems/api/v5/products?" + request_url[0:-1], "", current_api_name(),
                        expected_return_code, out_parameter_list, out_json_path_list)
        if self.getApiresponse[1] == expected_return_code:
            for i, out_param in enumerate(out_parameter_list):
                LOGGER.info(out_parameter_list[i])
                LOGGER.info(self.out_param_List[out_parameter_list[i]])
        return self

    def replace_product(self, product_json, expected_return_code, out_parameter_list, out_json_path_list, id=None,
                        name_version=None,
                        external_id=None, identifier=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if id is not None:
            self.putRequest(url + '/ems/api/v5/products/' + id, product_json, current_api_name(),
                            expected_return_code, out_parameter_list, out_json_path_list)
        elif external_id is not None:
            self.putRequest(url + '/ems/api/v5/products/externalId=' + external_id, product_json,
                            current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif name_version is not None:
            self.putRequest(url + '/ems/api/v5/products/nameVersion=' + name_version, product_json,
                            current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif identifier is not None:
            self.putRequest(url + '/ems/api/v5/products/identifier=' + identifier, product_json,
                            current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
            if self.putApiResponse[1] == expected_return_code:
                for i, out_param in enumerate(out_parameter_list):
                    LOGGER.info(out_parameter_list[i])
                    LOGGER.info(self.out_param_List[out_parameter_list[i]])
        return self

    def delete_product(self, expected_return_code, out_parameter_list=None, out_json_path_list=None, id=None,
                       name_version=None, external_id=None, identifier=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        if id is not None:
            self.deleteRequest(url + '/ems/api/v5/products/' + id, "", current_api_name(),
                               expected_return_code, out_parameter_list, out_json_path_list)
        elif external_id is not None:
            self.deleteRequest(url + '/ems/api/v5/products/externalId=' + external_id, "",
                               current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif name_version is not None:
            self.deleteRequest(url + '/ems/api/v5/products/nameVersion=' + name_version, "",
                               current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        elif identifier is not None:
            self.deleteRequest(url + '/ems/api/v5/products/identifier=' + identifier, "",
                               current_api_name(), expected_return_code, out_parameter_list, out_json_path_list)
        if self.deleteApiresponse[0] == expected_return_code:
            if (self.deleteApiresponse[0] == ErrorCode.HTTP204):
                LOGGER.info("Product deleted successfully")
            else:
                for i, out_param in enumerate(out_parameter_list):
                    LOGGER.info(out_parameter_list[i])
                    LOGGER.info(self.out_param_List[out_parameter_list[i]])

        return self
