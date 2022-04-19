import json
import numpy as np
import requests
from jsonpath_ng.ext import parse
import Constant
import logging
LOGGER = logging.getLogger(__name__)
url = Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

class NameSpacefactory:

    def addNameSpace(self, nameSpaceJsonPath, nameSpaceNamegenerator):
        nameSpaceFile = open(nameSpaceJsonPath, 'r')
        nameSpaceFileData = nameSpaceFile.read()
        json_object = json.loads(nameSpaceFileData)
        nameSpaceFile.close()
        json_object["namespace"]["name"] = nameSpaceNamegenerator + self.Upper_Lower_string(9)
        json_object1 = json.dumps(json_object)
        responseNameSpace = requests.post(url + '/ems/api/v5/namespaces', json_object1, auth=(username, password))
        response_nameSpace = json.loads(responseNameSpace.text)
        LOGGER.info(response_nameSpace)
        nameSpace_name = response_nameSpace["namespace"]["name"]
        nameSpace_id = response_nameSpace["namespace"]["id"]
        self.nameSpaceProperties = [nameSpace_name, nameSpace_id]
        return self


    def getNamespaceProps(self) -> list:
        return self.nameSpaceProperties