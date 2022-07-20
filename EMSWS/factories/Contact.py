import EMSWS.EMSConfig as Constant
import logging
from EMSWS.Utilities import UtilityClass
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword


class ContactFactory:

    def add_standard_contact_json_path(self,contact_json_file_path,contact_name,contact_email_id,
                                       expected_return_code,out_parameter_list=None,out_json_path_list=None, output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.UpdateJsonFile(contact_json_file_path, ['$.contact.name', '$.contact.password','$.contact.contactType','$.contact.emailId'],
                            [contact_name,"Thales@123", "Standard",contact_email_id])
        self.ems_api_auth_request_wrapper("POST", url + '/ems/api/v5/contacts', self.UpdateJsonFileResponse, "",
                                          current_api_name(), username, password,expected_return_code, out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self

    def add_standard_contact_json(self,contact_json,expected_return_code,out_parameter_list=None,out_json_path_list=None,
                                  output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        self.ems_api_auth_request_wrapper("POST", url + '/ems/api/v5/contacts', contact_json, "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self

    def get_contact(self, expected_return_code, out_parameter_list, out_json_path_list,id=None,email_id=None ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/contacts/' + id
        elif email_id is not None:
            request_url = url + '/ems/api/v5/contacts/emailId=' + email_id
        self.ems_api_auth_request_wrapper("GET", request_url, "", "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self

    def partial_update_contact(self, contact_json, expected_return_code,
                               out_parameter_list, out_json_path_list, id=None, emailId=None ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/contacts/' + id
        elif emailId is not None:
            request_url = url + '/ems/api/v5/contacts/emailId=' + emailId
        self.ems_api_auth_request_wrapper("PATCH", request_url, contact_json, "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self

    def delete_contact(self, expected_return_code,out_parameter_list=None, out_json_path_list=None, id=None, emailId=None
                       ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/contacts/' + id
        elif emailId is not None:
            request_url = url + '/ems/api/v5/contacts/emailId=' + emailId
        self.ems_api_auth_request_wrapper("DELETE", request_url, "", "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)

        return self

    def replace_contact(self, contact_json, expected_return_code, out_parameter_list, out_json_path_list, id=None,
                        emailId=None ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        request_url = ""
        if id is not None:
            request_url = url + '/ems/api/v5/contacts/' + id
        elif emailId is not None:
            request_url = url + '/ems/api/v5/contacts/emailId=' + emailId
        self.ems_api_auth_request_wrapper("PUT", request_url, contact_json, "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self

    def search_contact(self, expected_return_code, out_parameter_list, out_json_path_list, id=None, name=None, ref_id1=None, ref_id2=None,
                      email_id=None, phone_number=None, state=None, customer_name=None, customer_id=None,
                      market_group_id=None, market_group_name=None ,output_res_xml_parameter=None):
        utility = UtilityClass()
        current_api_name = utility.currentApiName()
        LOGGER.info(current_api_name())
        request_url = ""
        if id is not None:
            request_url += "id=" + id + "&"
        if name is not None:
            request_url += "name=" + name + "&"
        if ref_id1 is not None:
            request_url += "refId1=" + ref_id1 + "&"
        if ref_id2 is not None:
            request_url += "refId2=" + ref_id2 + "&"
        if email_id is not None:
            request_url += "emailId=" + email_id + "&"
        if phone_number is not None:
            request_url += "phoneNumber" + phone_number + "&"
        if state is not None:
            request_url += "state" + state + "&"
        if customer_id is not None:
            request_url += "customerId" + customer_id + "&"
        if customer_name is not None:
            request_url += "customerName" + customer_name + "&"
        if market_group_id is not None:
            request_url += "marketGroupId" + market_group_id + "&"
        if market_group_name is not None:
            request_url += "marketGroupName" + market_group_name + "&"
        request_url = url + "/ems/api/v5/contacts?" + request_url[0:-1]
        LOGGER.info(request_url)
        self.ems_api_auth_request_wrapper("GET", request_url, "", "",
                                          current_api_name(), username, password, expected_return_code,
                                          out_parameter_list, out_json_path_list,
                                          output_res_xml_parameter, bearerAuth=None)
        return self

