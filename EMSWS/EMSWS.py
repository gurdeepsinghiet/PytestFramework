import functionsEMSWS
import Constant

def test_Product_Network_NONLVH():

    # ======================create NameSpace====================
    nameSpace_name, nameSpace_id = functionsEMSWS.createNameSpace(Constant.nameSpaceJsonPath, "nameSpacePytesting")

    # ======get Enforcement=============
    enforcementId = functionsEMSWS.getEnforcement()
    # ==================Search Flexible LicenceModel==========
    response_LM_json = functionsEMSWS.searchFlexibleLicenseModel(enforcementId)
    # ============================Update License Model attr===========================
    LM_name, lmId = functionsEMSWS.createFlexibleLicenceModelNetwork("FlexibleEMSPytestLMNetwork", response_LM_json)
    # =================create Feature================
    feature_name, feature_version = functionsEMSWS.createFeature("FeaturePytest", Constant.featureJsonPath, LM_name,
                                                                 nameSpace_name)
    # ==================create Product=====
    product_name, product_version,response_feature_name,response_feature_version = functionsEMSWS.createProductNonLVH(Constant.productJsonPath, "productEMSPytesting",
                                                                       nameSpace_name, feature_name, feature_version)

    assert response_feature_name==feature_name
    assert response_feature_version==feature_version

def test_Product_Standalone_NONLVH1():
    # ======================create NameSpace====================
    nameSpace_name, nameSpace_id = functionsEMSWS.createNameSpace(Constant.nameSpaceJsonPath, "nameSpacePytesting")

    # ======get Enforcement=============
    enforcementId = functionsEMSWS.getEnforcement()
    # ==================Search Flexible LicenceModel==========
    response_LM_json = functionsEMSWS.searchFlexibleLicenseModel(enforcementId)
    # ============================Update License Model attr===========================
    LM_name, lmId = functionsEMSWS.createFlexibleLicenceModelStandalone("FlexiblePytestLMNetwork", response_LM_json)
    # =================create Feature================
    feature_name, feature_version = functionsEMSWS.createFeature("FeaturePytest", Constant.featureJsonPath, LM_name,
                                                                 nameSpace_name)
    # ==================create Product=====
    product_name, product_version,response_feature_name,response_feature_version = functionsEMSWS.createProductNonLVH(Constant.productJsonPath, "productPytesting",
                                                                       nameSpace_name, feature_name, feature_version)
    # ==================create contact=================================================
    contact_id, contact_name, contact_emailId = functionsEMSWS.createStandardContact(Constant.contactJsonPath,
                                                                                     "contactStandardPytestingTest",
                                                                                     "thalesOrganisation")
    # ==================create Customer=================================================
    customer_id, customer_name = functionsEMSWS.createCustomer(Constant.customerJsonPath, "customerPyTestingTest",
                                                               contact_id)

    assert response_feature_name==feature_name
    assert response_feature_version==feature_version

def test_Entitlement_Standalone_NONLVH():
    # ======================create NameSpace====================
    nameSpace_name, nameSpace_id = functionsEMSWS.createNameSpace(Constant.nameSpaceJsonPath, "nameSpacePytesting")
    # ======get Enforcement=============
    enforcementId = functionsEMSWS.getEnforcement()
    # ==================Search Flexible LicenceModel==========
    response_LM_json = functionsEMSWS.searchFlexibleLicenseModel(enforcementId)
    # ============================Update License Model attr===========================
    LM_name, lmId = functionsEMSWS.createFlexibleLicenceModelStandalone("FlexiblePytestLMNetwork", response_LM_json)
    # =================create Feature================
    feature_name, feature_version = functionsEMSWS.createFeature("FeaturePytest", Constant.featureJsonPath, LM_name,
                                                             nameSpace_name)

    # ==================create Product=============
    product_name, product_version,response_feature_name,response_feature_version = functionsEMSWS.createProductNonLVH(Constant.productJsonPath, "productPytesting",
                                                                       nameSpace_name, feature_name, feature_version)
    # ==================create contact=================================================
    contact_id, contact_name, contact_emailId = functionsEMSWS.createStandardContact(Constant.contactJsonPath,
                                                                                     "contactStandardPytestingTest",
                                                                                     "thalesOrganisation")
    # ==================create Customer=================================================
    customer_id, customer_name = functionsEMSWS.createCustomer(Constant.customerJsonPath, "customerPyTestingTest",
                                                               contact_id)
    eid,id=functionsEMSWS.createEntitlementNONLVH(product_name,product_version,customer_name,Constant.entitlementJsonPath)
    print(eid,id)
    "llll".split(" ").pop()
    assert response_feature_name==feature_name
    assert response_feature_version==feature_version


def test_Entitlement_Network_NONLVH1000Products():
    # ======================create NameSpace====================
    #nameSpace_name, nameSpace_id = functionsEMSWS.createNameSpace(Constant.nameSpaceJsonPath, "nameSpacePytesting")
    # ======get Enforcement=============
    #enforcementId = functionsEMSWS.getEnforcement()
    # ==================Search Flexible LicenceModel==========
    #response_LM_json = functionsEMSWS.searchFlexibleLicenseModel(enforcementId)
    # ============================Update License Model attr===========================
    #LM_name, lmId = functionsEMSWS.createFlexibleLicenceModelNetwork("FlexiblePytestLMNetwork", response_LM_json)
    # =================create Feature================
    #feature_name, feature_version = functionsEMSWS.createFeature("FeaturePytest", Constant.featureJsonPath, LM_name,nameSpace_name)
    # ==================create contact=================================================
    #contact_id, contact_name, contact_emailId = functionsEMSWS.createStandardContact(Constant.contactJsonPath,"contactStandardPytestingTest","thalesOrganisation")
    # ==================create Customer=================================================
    #customer_id, customer_name = functionsEMSWS.createCustomer(Constant.customerJsonPath, "customerPyTestingTest",contact_id)

    #product_name, product_version, response_feature_name, response_feature_version = functionsEMSWS.createProductNonLVH(
        #Constant.productJsonPath, "productPytesting",
        #nameSpace_name, feature_name, feature_version)

    #eid, id = functionsEMSWS.createEntitlementNONLVH(product_name, product_version, customer_name,Constant.entitlementJsonPath)

    eid="48a5fec6-81d8-4638-beac-97c3c9e41dea"
    nameSpace_name="nameSpacePytesting6856557"
    feature_name="FeaturePytest2357967"
    feature_version="1.0"

    for i in range(403):

        product_name, product_version, response_feature_name, response_feature_version = functionsEMSWS.createProductNonLVH(
            Constant.productJsonPath, "productPytesting"+str(i),
            nameSpace_name, feature_name, feature_version)
        functionsEMSWS.addProductKeyEntitlment(product_name, product_version, eid, Constant.productKeyJsonPath)







# def test_LicDecode():
#     functionsEMSWS.lrsvrcDecoder()
#     getDecodeLicense = open("licdododer.txt", 'r')
#     print(getDecodeLicense)

