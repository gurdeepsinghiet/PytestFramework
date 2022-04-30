import json
import requests
import os
import EMSWS.Constant as Constant
import pytest
import logging
from pathlib import Path
import sys

LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class NameSpacefactory():

    def addNameSpace(self, nameSpaceJsonPath, nameSpaceNamegenerator):
        #getting the name of Current Running Test cases
        running_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        LOGGER.info(running_testcases)
        # getting the name of Current exectuting Function
        currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
        LOGGER.info(currentFuncName())
        #Dictionary object for crearing NameSpace Report
        nameSpaceReportPorps = {}
        my_file = Path(nameSpaceJsonPath)
        if my_file.is_file():
            nameSpaceFile = open(nameSpaceJsonPath, 'r')
            nameSpaceFileData = nameSpaceFile.read()
            json_object = json.loads(nameSpaceFileData)
            nameSpaceFile.close()
            nameSpaceName=nameSpaceNamegenerator + self.RandomString(9)
            json_object["namespace"]["name"] = nameSpaceName
            namceSpace_json = json.dumps(json_object)
            LOGGER.info(namceSpace_json)
            nameSpaceReportPorps["Api_Name"] = currentFuncName()
            nameSpaceReportPorps["inputs"] = namceSpace_json
            nameSpaceReportPorps["Expected_Code"] = "201"
            try:
                responseNameSpace = requests.post(url + '/ems/api/v5/namespaces', namceSpace_json, auth=(username, password))
                #Collectin data for Report
                if responseNameSpace.status_code == 201 or responseNameSpace.status_code == 204 or responseNameSpace.status_code == 200:
                    response_nameSpace = json.loads(responseNameSpace.text)
                    LOGGER.info(response_nameSpace)
                    nameSpace_name = response_nameSpace["namespace"]["name"]
                    nameSpace_id = response_nameSpace["namespace"]["id"]
                    #List Object for Namespace Response
                    self.nameSpaceProperties = [nameSpace_name, nameSpace_id,responseNameSpace]
                    # Collecting data for Report Status if Test step Pass
                    nameSpaceReportPorps["actual_Code"] = responseNameSpace.status_code
                    nameSpaceReportPorps["Response_time"] = responseNameSpace.elapsed.total_seconds()
                    nameSpaceReportPorps["Act_Response"] = responseNameSpace.text
                    nameSpaceReportPorps["Status"] = "Pass"
                    nameSpaceReportPorps["Expected_Response"] = ""
                    self.data.append(nameSpaceReportPorps)
                    #self.tableGenerator(self.data)
                    LOGGER.info(self.data)
                    LOGGER.info(self.nameSpaceProperties)
                else:
                    nameSpaceReportPorps["Act Response"] = responseNameSpace.text
                    nameSpaceReportPorps["Expected_Response"] = ""
                    LOGGER.error(responseNameSpace.text)
                    nameSpaceReportPorps["actual_Code"] = responseNameSpace.status_code
                    nameSpaceReportPorps["Response_time"] = responseNameSpace.elapsed.total_seconds()
                    # Collecting data for Report Status if Test step fail
                    nameSpaceReportPorps["Status"] = "Failed"
                    self.data.append(nameSpaceReportPorps)
                    LOGGER.info(self.data)
                    pytest.fail("Problem with creating nameSpace")
            except requests.exceptions.RequestException as e:  # This is the correct syntax
                LOGGER.error(e)
        else:
            LOGGER.error("File is not found in the system")
            nameSpaceReportPorps["Status"] = "Failed"
            self.data.append(nameSpaceReportPorps)
            LOGGER.info(self.data)
            pytest.fail("failed")
        LOGGER.info(self.data)
        return self

    def createNameSpace(self):
        run_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        # getting the name of Current exectuting Function
        currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name
        LOGGER.info(run_testcases)
        nameSpaceFile = open(Constant.nameSpaceJsonPath, 'r')
        nameSpaceFileData = nameSpaceFile.read()
        json_object = json.loads(nameSpaceFileData)
        nameSpaceFile.close()
        nameSpaceReportPorps={}
        nameDataFrameFile = open(Constant.emsDataFramePath + run_testcases + '.json', 'r')
        namespaceData = nameDataFrameFile.read()
        nameDataFrameFile.close()
        print(namespaceData)

        #loads convert json data to dictionary object
        nameSpace_dic = json.loads(namespaceData)
        nameSpaceName = run_testcases[0:8] + self.RandomString(9)
        json_object["namespace"]["name"] = nameSpaceName
        json_namespace = json.dumps(json_object)
        nameSpaceReportPorps["Api_Name"] = currentFuncName()
        nameSpaceReportPorps["inputs"] = json_namespace
        nameSpaceReportPorps["Expected_Code"] = "201"
        nameSpaceReportPorps["Expected_Response"] = ""
        responseNameSpace = requests.post(url + '/ems/api/v5/namespaces',json_namespace, auth=(username, password))
        if responseNameSpace.status_code == 201 or responseNameSpace.status_code == 204 or responseNameSpace.status_code == 200:
            response_nameSpace = json.loads(responseNameSpace.text)
            LOGGER.info(response_nameSpace)
            nameSpace_name = response_nameSpace["namespace"]["name"]
            nameSpace_id = response_nameSpace["namespace"]["id"]
            nameSpaceReportPorps["actual_Code"] = responseNameSpace.status_code
            nameSpaceReportPorps["Response_time"] = responseNameSpace.elapsed.total_seconds()
            nameSpaceReportPorps["Act_Response"] = responseNameSpace.text
            nameSpaceReportPorps["Expected_Response"] = ""
            nameSpaceReportPorps["Status"] = "Pass"
            self.nameSpaceProps = [nameSpace_name, nameSpace_id, responseNameSpace]
            assert nameSpaceName == self.nameSpaceProps[0]
        else:
            LOGGER.error(responseNameSpace.text)
        self.data.append(nameSpaceReportPorps)
        return self

    def getNamespaceProps(self) -> list:
        return self.nameSpaceProperties