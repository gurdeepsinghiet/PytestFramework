import json
import requests
from jsonpath_ng.ext import parse
import Constant
import pytest
import logging
from pathlib import Path
import sys
from customHtmlFileGenerator import CustomeReportGenerator

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class NameSpacefactory(CustomeReportGenerator):

    def addNameSpace(self, nameSpaceJsonPath, nameSpaceNamegenerator):
        currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
        LOGGER.info(currentFuncName())
        nameSpaceReportPorps = {}
        nameSpaceReportPorps["Api_Name"] = currentFuncName()
        my_file = Path(nameSpaceJsonPath)
        if my_file.is_file():
            nameSpaceFile = open(nameSpaceJsonPath, 'r')
            nameSpaceFileData = nameSpaceFile.read()
            json_object = json.loads(nameSpaceFileData)
            nameSpaceFile.close()
            nameSpaceName=nameSpaceNamegenerator + self.Upper_Lower_string(9)
            json_object["namespace"]["name"] = nameSpaceName
            namceSpace_json = json.dumps(json_object)
            LOGGER.info(namceSpace_json)
            responseNameSpace = requests.post(url + '/ems/api/v5/namespaces', namceSpace_json, auth=(username, password))
            nameSpaceReportPorps["inputs"] = namceSpace_json
            nameSpaceReportPorps["Expected_Code"] = "201"
            nameSpaceReportPorps["actual_Code"] = responseNameSpace.status_code
            nameSpaceReportPorps["Response_time"] = responseNameSpace.elapsed.total_seconds()
            if responseNameSpace.status_code == 201 or responseNameSpace.status_code == 204 or responseNameSpace.status_code == 200:
                response_nameSpace = json.loads(responseNameSpace.text)
                LOGGER.info(response_nameSpace)
                nameSpace_name = response_nameSpace["namespace"]["name"]
                nameSpace_id = response_nameSpace["namespace"]["id"]
                self.nameSpaceProperties = [nameSpace_name, nameSpace_id]
                nameSpaceReportPorps["Status"] = "Pass"
                self.data.append(nameSpaceReportPorps)
                LOGGER.info(self.data)
                LOGGER.info(self.nameSpaceProperties)

            else:
                LOGGER.error(responseNameSpace.text)
                nameSpaceReportPorps["Status"] = "Failed"
                self.data.append(nameSpaceReportPorps)
                LOGGER.info(self.data)
                pytest.fail("Problem with creating nameSpace")
        else:
            LOGGER.error("File is not found in the system")
            nameSpaceReportPorps["Status"] = "Failed"
            self.data.append(nameSpaceReportPorps)
            LOGGER.info(self.data)
            pytest.fail("failed")
        LOGGER.info(self.data)
        return self

    def getNamespaceProps(self) -> list:
        return self.nameSpaceProperties