import json
import logging
import os
import sys
import yaml
import pytest
import datetime
import EMSWS
import base64
LOGGER = logging.getLogger(__name__)


class UtilityClass(object):

    def readFile(self, path):
        try:
            with open(path) as f_obj:
                contents = f_obj.read()
                return contents
        except FileExistsError as error:
            LOGGER.error(error)
        except FileNotFoundError as error:
            LOGGER.error(error)
            pytest.fail()

    def deleteFile(self, path):
        try:
            if os.path.exists(path):
                os.remove(path)
        except:
            LOGGER.error("error in deleting file")

    def convertJsontoDictinary(self, jsonData):
        try:
            dic_object = json.loads(jsonData)
            return dic_object
        except json.decoder.JSONDecodeError as error:
            LOGGER.error(error)

    def convertDictinarytoJson(self, dictionaryData):
        try:
            json_object = json.dumps(dictionaryData)
            return json_object
        except TypeError as error:
            LOGGER.error("Type error with Dictionay object")
        except KeyError as error:
            LOGGER.error("Key error with Dictionay object")

    def runningPytestCaseName(self):
        return os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]

    def currentApiName(self):
        return lambda n=0: sys._getframe(n + 1).f_code.co_name

    def decodeJsonFile(self, jsonFilePath):
        try:
            with open(jsonFilePath) as file_object:
                data = json.load(file_object)
                return data
        except ValueError:
            LOGGER.error("Error parsing json data")

    def read_yaml_file(self,yaml_path, api_name):
        with open(yaml_path) as file:
            data_yml_obj = yaml.load(file, Loader=yaml.FullLoader)["API"]
        for data in data_yml_obj:
            if data['name'] == api_name:
                yml_data = data
        return yml_data

    def getModulePath(self):
        path = os.path.dirname(EMSWS.__file__)
        return path

    def date_time_now_to_epoch(self,no_of_days):
        nowb = datetime.datetime.now()
        my_date_days = nowb + datetime.timedelta(days=0)
        date_time = my_date_days.strftime("%m/%d/%Y %H:%M:%S")
        print(my_date_days)
        date_split = date_time.split("/")
        time_split=date_split[2].split(":")
        yh=time_split[0].split(" ")
        full=date_split[0:2]+yh+time_split[1:3]
        full = [int(x) for x in full ]
        epoch = int(datetime.datetime(full[2], full[0], full[1], full[3], full[4], full[5]).timestamp())
        return epoch


    def base64Ecoding(self,sample_string):
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
        return base64_string

u = UtilityClass()
print(u.date_time_now_to_epoch(6))