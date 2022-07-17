import logging
from EMSWS.Utilities import UtilityClass
import EMSWS.EMSConfig as Constant
import  EMSWS.ErrorCode as ErrorCode
import EMSWS.JsonPath as JsonPath
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class CustomerFactory(object):

    def add_customer_json_file_path(self, customerJsonFilePath,CustomerName,contact_id,
                                    expected_return_code,out_parameter_list=None,out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(customerJsonFilePath, ['$.customer.name','$.customer.identifier','$..contacts.contact[0].id'],
                            [CustomerName,CustomerName,contact_id],["custRes"],['$'])
        self.ems_api_request_wrapper(url + '/ems/api/v5/customers', self.UpdateJsonFileResponse, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def add_customer_json(self, customer_json, expected_return_code, out_parameter_list=None, out_json_path_list=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.ems_api_request_wrapper(url + '/ems/api/v5/customers',customer_json, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def partial_update_customer(self, customer_json, expected_return_code, out_parameter_list, out_json_path_list, id=None, email_id=None,
                              identifier=None, external_id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/customers/' + id
        elif email_id is not None:
            request_url = url + '/ems/api/v5/customers/emailId=' + email_id
        elif identifier is not None:
            request_url = url + '/ems/api/v5/customers/identifier=' + identifier
        elif external_id is not None:
            request_url = url + '/ems/api/v5/customers/externalId=' + external_id
        self.ems_api_request_wrapper(request_url, customer_json, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def delete_customer(self, expected_return_code,out_parameter_list=None, out_json_path_list=None,
                        id=None, email_id=None, identifier=None,external_id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/customers/' + id
        elif email_id is not None:
            request_url = url + '/ems/api/v5/customers/emailId=' + email_id
        elif identifier is not None:
            request_url = url + '/ems/api/v5/customers/identifier=' + identifier
        elif external_id is not None:
            request_url = url + '/ems/api/v5/customers/externalId=' + external_id
        self.ems_api_request_wrapper(request_url, "", expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def replace_customer(self, customer_json, expected_return_code, out_parameter_list, out_json_path_list,
                        id=None, email_id=None,identifier=None, external_id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        request_url = ""
        if id is not None:
            request_url=url + '/ems/api/v5/customers/' + id
        elif email_id is not None:
            request_url = url + '/ems/api/v5/customers/emailId=' + email_id
        elif identifier is not None:
            request_url = url + '/ems/api/v5/customers/identifier=' + identifier
        elif external_id is not None:
            request_url = url + '/ems/api/v5/customers/externalId=' + external_id
        self.ems_api_request_wrapper(request_url, customer_json, expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self

    def search_customer(self, expected_return_code, out_parameter_list, out_json_path_list, id=None, name=None, identifier=None,
                       external_id=None, ref_id=None, crm_id=None, description=None, market_group_id=None,
                       market_group_name=None, state=None, contact_email_id=None, contact_id=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url += "id=" + id + "&"
        if name is not None:
            request_url += "name=" + name + "&"
        if identifier is not None:
            request_url += "identifier=" + identifier + "&"
        if external_id is not None:
            request_url += "externalId=" + external_id + "&"
        if ref_id is not None:
            request_url += "refId=" + ref_id + "&"
        if crm_id is not None:
            request_url += "crmId=" + crm_id + "&"
        if description is not None:
            request_url += "description=" + description + "&"
        if market_group_id is not None:
            request_url += "marketGroupId=" + market_group_id + "&"
        if market_group_name is not None:
            request_url += "marketGroupName=" + market_group_name + "&"
        if state is not None:
            request_url += "state=" + state + "&"
        if contact_email_id is not None:
            request_url += "contactEmailId=" + contact_email_id + "&"
        if contact_id is not None:
            request_url += "contactId=" + contact_id + "&"
        request_url = url + "/ems/api/v5/customers?" + request_url[0:-1]
        self.ems_api_request_wrapper(request_url, "", expected_return_code,
                                     current_api_name(), out_parameter_list, out_json_path_list)
        return self


