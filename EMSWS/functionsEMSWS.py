import json
import numpy as np
import requests
from jsonpath_ng.ext import parse
import Constant
import logging
import random
import string

LOGGER = logging.getLogger(__name__)
url=Constant.EMSURL
username = Constant.EMSUserName
password = Constant.EMSPassword

def Upper_Lower_string(length):  # define the function and pass the length as argument
    # Print the string in Lowercase
    result = ''.join(
        (random.choice(string.ascii_lowercase) for x in range(length)))  # run loop until the define length
    return result

def createNameSpace(nameSpaceJsonPath,nameSpaceNamegenerator):
    nameSpaceFile = open(nameSpaceJsonPath, 'r')
    nameSpaceFileData = nameSpaceFile.read()
    json_object = json.loads(nameSpaceFileData)
    nameSpaceFile.close()
    json_object["namespace"]["name"] = nameSpaceNamegenerator + str(np.random.randint(1000000, 7000000))
    #nameSpaceFile = open(nameSpaceJsonPath, "w")
    #json.dump(json_object, nameSpaceFile)
    #nameSpaceFile.close()
    #nameSpaceFile = open(nameSpaceJsonPath, 'r')
    #nameSpace_json1 = nameSpaceFile.read()
    json_object1=json.dumps(json_object)
    responseNameSpace = requests.post(url + '/ems/api/v5/namespaces', json_object1, auth=(username, password))
    response_nameSpace = json.loads(responseNameSpace.text)
    LOGGER.info(response_nameSpace)
    nameSpace_name = response_nameSpace["namespace"]["name"]
    nameSpace_id = response_nameSpace["namespace"]["id"]
    return [nameSpace_name, nameSpace_id]


def getEnforcement():
    responseEnforcement = requests.get(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS :10.0',auth=(username, password))
    response_Enforcement = json.loads(responseEnforcement.text)
    LOGGER.info(response_Enforcement)
    enforcementId = response_Enforcement["enforcement"]["id"]
    return enforcementId

def searchFlexibleLicenseModel(enforcementId):
    responseFlexibleLicenseModel = requests.get(
        url + '/ems/api/v5/enforcements/'+enforcementId+'/licenseModels/name=Flexible License Model',
        auth=(username, password))
    response_LM_json = json.loads(responseFlexibleLicenseModel.text)
    LOGGER.info(response_LM_json)
    return response_LM_json

def updateLicencezModelAttribute(LM_ATTR_Name,value,response_LM_json):
    jsonpath_expression = parse('$.licenseModel.licenseModelAttributes.licenseModelAttribute[*]')
    for match in jsonpath_expression.find(response_LM_json):
        if(match.value["enforcementAttribute"] ["name"] == LM_ATTR_Name):
            match.value["value"]=value

def createFlexibleLicenceModelStandalone(LMNameGenerator,response_LM_json):
    updateLicencezModelAttribute("ENFORCE_CLOCK_TAMPERED", "FALSE", response_LM_json)
    updateLicencezModelAttribute("LICENSE_TYPE", "1", response_LM_json)
    updateLicencezModelAttribute("DEPLOYMENT_TYPE", "1", response_LM_json)
    response_LM_json["licenseModel"]["name"] = LMNameGenerator + str(np.random.randint(1000000, 9000000))
    response_LM_json1 = json.dumps(response_LM_json)
    responseLM1 = requests.post(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                                response_LM_json1, auth=(username, password))
    responseTextLM = json.loads(responseLM1.text)
    LOGGER.info(responseTextLM)
    LM_name = responseTextLM["licenseModel"]["name"]
    lmId = response_LM_json["licenseModel"]["id"]
    return [LM_name,lmId]

def createFlexibleLicenceModelNetwork(LMNameGenerator,response_LM_json):
    updateLicencezModelAttribute("ENFORCE_CLOCK_TAMPERED", "FALSE", response_LM_json)
    updateLicencezModelAttribute("LICENSE_TYPE", "0", response_LM_json)
    updateLicencezModelAttribute("DEPLOYMENT_TYPE", "1", response_LM_json)
    response_LM_json["licenseModel"]["name"] = LMNameGenerator + str(np.random.randint(1000000, 7000000))
    response_LM_json1 = json.dumps(response_LM_json)
    responseLM1 = requests.post(url + '/ems/api/v5/enforcements/nameVersion=Sentinel RMS:10.0/licenseModels',
                                response_LM_json1, auth=(username, password))
    responseTextLM = json.loads(responseLM1.text)
    LOGGER.info(responseTextLM)
    LM_name = responseTextLM["licenseModel"]["name"]
    lmId = response_LM_json["licenseModel"]["id"]
    return [LM_name,lmId]

def createFeature(FeatureNameGenerator,featureJsonPath,LM_name,nameSpace_name):
    featureFile = open(featureJsonPath, 'r')
    featureFileData = featureFile.read()
    feature_json_object = json.loads(featureFileData)
    featureFile.close()
    feature_json_object["feature"]["namespace"]["name"] = nameSpace_name
    feature_json_object["feature"]["nameVersion"]["name"] = FeatureNameGenerator + str(np.random.randint(1000000, 9000000))
    feature_json_object["feature"]["nameVersion"]["version"] = "1.0"
    feature_json_object["feature"]["featureLicenseModels"]["featureLicenseModel"][0]["licenseModel"]["name"] = LM_name
    featureFile = open(featureJsonPath, "w")
    json.dump(feature_json_object, featureFile)
    featureFile.close()
    featureFile = open(featureJsonPath, 'r')
    featureUpdated_json = featureFile.read()
    responseFeature = requests.post(url + '/ems/api/v5/features', featureUpdated_json, auth=(username, password))
    responseTextFeature = json.loads(responseFeature.text)
    LOGGER.info(responseTextFeature)
    feature_name = responseTextFeature["feature"]["nameVersion"]["name"]
    feature_version = responseTextFeature["feature"]["nameVersion"]["version"]
    return [feature_name,feature_version]


def createProductNonLVH(productJsonPath,productNameGenerator,nameSpace_name,feature_name,feature_version):
    productFile = open(productJsonPath, 'r')
    productFileData = productFile.read()
    product_json_object = json.loads(productFileData)
    productFile.close()
    product_json_object["product"]["namespace"]["name"] = nameSpace_name
    product_json_object["product"]["nameVersion"]["name"] = productNameGenerator + str(np.random.randint(1000000, 9000000))
    product_json_object["product"]["nameVersion"]["version"] = feature_version
    product_json_object["product"]["productFeatures"]["productFeature"][0]["feature"]["nameVersion"][
        "name"] = feature_name
    product_json_object["product"]["productFeatures"]["productFeature"][0]["feature"]["nameVersion"]["version"] = feature_version
    productFile = open(productJsonPath, "w")
    json.dump(product_json_object, productFile)
    productFile.close()
    productFile = open(productJsonPath, 'r')
    productUpdated_json = productFile.read()
    responseProduct = requests.post(url + '/ems/api/v5/products', productUpdated_json, auth=(username, password))
    responseTextProduct = json.loads(responseProduct.text)
    LOGGER.info(responseTextProduct)
    product_name = responseTextProduct["product"]["nameVersion"]["name"]
    product_version = responseTextProduct["product"]["nameVersion"]["version"]
    feature_name = responseTextProduct["product"]["productFeatures"]["productFeature"][0]["feature"]["nameVersion"]["name"]
    feature_version = responseTextProduct["product"]["productFeatures"]["productFeature"][0]["feature"]["nameVersion"]["version"]
    return [product_name,product_version,feature_name,feature_version]


def createStandardContact(contactJsonPath,contactNameGenerator,emailString):
    contactFile = open(contactJsonPath, 'r')
    contactFileData = contactFile.read()
    contact_json_object = json.loads(contactFileData)
    contactFile.close()
    contact_json_object["contact"]["name"] = contactNameGenerator + str(np.random.randint(1000000, 7000000))
    contact_json_object["contact"]["password"] = "Thales@123"
    contact_json_object["contact"]["contactType"] = "Standard"
    contact_json_object["contact"]["emailId"] = emailString + str(
        np.random.randint(1000000, 7000000)) + "@Thales.com"
    contactFile = open(contactJsonPath, "w")
    json.dump(contact_json_object, contactFile)
    contactFile.close()
    contactFile = open(contactJsonPath, 'r')
    contactupdated_json = contactFile.read()
    responseContact = requests.post(url + '/ems/api/v5/contacts', contactupdated_json, auth=(username, password))
    responseTextContact = json.loads(responseContact.text)
    contact_name=responseTextContact["contact"]["name"]
    conatct_id=responseTextContact["contact"]["id"]
    contact_emailId = responseTextContact["contact"]["emailId"]
    return [conatct_id,contact_name,contact_emailId]

def createCustomer(customerJsonPath,customerNameGenerator,contact_id):
    customerFile = open(customerJsonPath, 'r')
    customerFileData = customerFile.read()
    customer_json_object = json.loads(customerFileData)
    customerFile.close()
    customerName = customerNameGenerator + str(np.random.randint(1000000, 7000000))
    customer_json_object["customer"]["name"] = customerName
    customer_json_object["customer"]["identifier"] = customerName
    customer_json_object["customer"]["contacts"]["contact"][0]["id"] = contact_id
    customerFile = open(customerJsonPath, "w")
    json.dump(customer_json_object, customerFile)
    customerFile.close()
    customerFile = open(customerJsonPath, 'r')
    customerUpdate_json = customerFile.read()
    responseCustomer = requests.post(url + '/ems/api/v5/customers',customerUpdate_json, auth=(username, password))
    responseTextCustomer = json.loads(responseCustomer.text)
    customer_name = responseTextCustomer["customer"]["name"]
    customer_id = responseTextCustomer["customer"]["id"]
    return [customer_id,customer_name]


def createEntitlementNONLVH(productNmae,productVesrion,customerName,entitlementJsonPath):
    entitlementFile = open(entitlementJsonPath, 'r')
    entitlemenetFileData = entitlementFile.read()
    entitlement_json_object = json.loads(entitlemenetFileData)
    entitlementFile.close()
    entitlement_json_object["entitlement"]["customer"]["name"]=customerName
    entitlement_json_object["entitlement"]["productKeys"]["productKey"][0]["item"]["itemProduct"]["product"]["nameVersion"]["name"]= productNmae
    entitlement_json_object["entitlement"]["productKeys"]["productKey"][0]["item"]["itemProduct"]["product"]["nameVersion"]["version"] = productVesrion
    json_object1 = json.dumps(entitlement_json_object)
    LOGGER.info('===============start====================')
    LOGGER.info(json_object1)
    LOGGER.info('================end===================')
    responseEntitlement = requests.post(url + '/ems/api/v5/entitlements', json_object1, auth=(username, password))
    response_entitlement = json.loads(responseEntitlement.text)
    eid = response_entitlement["entitlement"]["eId"]
    id = response_entitlement["entitlement"]["id"]
    LOGGER.info(eid)
    return [eid, id]

def fun():
    return fun2()

def fun2():
    return fun1()

def fun1():
    return "c"







































#================create NameSpace===========================
#https://blogboard.io/blog/knowledge/jsonpath-python/
#================= https://medium.com/swlh/build-your-first-automated-test-integration-with-pytest-jenkins-and-docker-ec738ec43955  =====================