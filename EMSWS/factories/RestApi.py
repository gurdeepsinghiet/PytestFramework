import requests
import logging
import EMSWS.Constant as Constant
import pytest
import json

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class RestApiUtilityFactory(object):

    def PostRequest(self, requestUrl, requestBody, ApiName,expectedresCode):
        ReportParameters = {}
        try:
            ReportParameters["Api_Name"] = ApiName
            ReportParameters["inputs"] = requestBody
            ReportParameters["Expected_Code"] = expectedresCode
            postapiResponse = requests.post(requestUrl, requestBody,auth=(username, password))
            # Collectin data for Report
            if postapiResponse.status_code == 201 or postapiResponse.status_code == 204 or postapiResponse.status_code == 200:
                response_dictionary = json.loads(postapiResponse.text)
                LOGGER.info(response_dictionary)
                # Collecting data for Report Status if Test step Pass
                ReportParameters["actual_Code"] = postapiResponse.status_code
                ReportParameters["Response_time"] = postapiResponse.elapsed.total_seconds()
                ReportParameters["Act_Response"] = postapiResponse.text
                ReportParameters["Status"] = "Pass"
                ReportParameters["Expected_Response"] = ""

            else:
                ReportParameters["Act Response"] = postapiResponse.text
                ReportParameters["Expected_Response"] = ""
                LOGGER.error(postapiResponse.text)
                ReportParameters["actual_Code"] = postapiResponse.status_code
                ReportParameters["Response_time"] = postapiResponse.elapsed.total_seconds()
                # Collecting data for Report Status if Test step fail
                ReportParameters["Status"] = "Failed"
                self.data.append(ReportParameters)
                pytest.fail("Problem with creating nameSpace")
        except requests.exceptions.RequestException as e:
            LOGGER.error(e)
        self.data.append(ReportParameters)
        LOGGER.info(self.data)
        return [postapiResponse.text,postapiResponse.status_code,ReportParameters]

    def getRequest(self):
        pass

    def deleteRequest(self):
        pass

    def patchRequest(self):
        pass

    def putRequest(self):
        pass