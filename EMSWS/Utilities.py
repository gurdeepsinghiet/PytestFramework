from pathlib import Path
import json
import logging
import os
import sys

import pytest

LOGGER = logging.getLogger(__name__)
class UtilityClass(object):

    def readFile(self,path):
        try:
            with open(path) as f_obj:
                contents = f_obj.read()
                return contents
        except FileExistsError as error:
            LOGGER.error(error)
        except FileNotFoundError as error:
            LOGGER.error(error)
            pytest.fail()


    def convertJsontoDictinary(self,jsonData):
        try:
            dic_object = json.loads(jsonData)
            return dic_object
        except json.decoder.JSONDecodeError as error:
            LOGGER.error(error)


    def convertDictinarytoJson(self,dictionaryData):
        try:
            json_object = json.dumps(dictionaryData)
            return json_object
        except TypeError as error:
            LOGGER.error(error)


    def runningPytestCaseName(self):
        return os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]


    def currentApiName(self):
        return lambda n=0: sys._getframe(n + 1).f_code.co_name