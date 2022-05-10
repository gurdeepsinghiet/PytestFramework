import  pytest
import logging
from pathlib import Path
import os
from EMSWS import EMSWS
import EMSWS.Constant as Constant
from EMSWS.factories.EMSFuntions import EMSFactory
LOGGER = logging.getLogger(__name__)
@pytest.fixture(autouse=True)
def emsObjectFixture():
    ems = EMSFactory()
    return locals()

@pytest.fixture(autouse=True)
def getReportPytestHook(emsObjectFixture):
    v=emsObjectFixture['ems']
    yield v
    v.reportGenerator()

def pytest_sessionstart(session):
    session.results = dict()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == 'call':
        item.session.results[item] = result
def pytest_sessionfinish(session, exitstatus):
    print('run status code:', exitstatus)
    nm=[result for result in session.results.values()]
    testcasename=nm[0].nodeid.split("::")[1]
    passed_amount = sum(1 for result in session.results.values() if result.passed)
    failed_amount = sum(1 for result in session.results.values() if result.failed)
    totalCase=passed_amount+failed_amount
    print(f'there are {passed_amount} passed and {failed_amount} failed tests in {totalCase} test cases')
    summary=[]
    for result in session.results.values():
        summaryPram = {}
        if result.passed:
            summaryPram["testcasename"]=result.nodeid.split("::")[1]
            summaryPram["status"] = "Passed"
            summary.append(summaryPram)
        elif result.failed:
            summaryPram["testcasename"] = result.nodeid.split("::")[1]
            summaryPram["status"] = "Failed"
            summary.append(summaryPram)

    summaryreportGenerator(summary,passed_amount,failed_amount,totalCase)

def testSummaryData(summaryData):
        preExistingTempleteData = ""
        for data in summaryData:
            preExistingTempleteData += "<tr>"
            preExistingTempleteData += "<td width='150px'>"
            preExistingTempleteData += "<div><a href='"+data["testcasename"]+".html'>"+data["testcasename"]+"</a></div>"
            preExistingTempleteData += "</td>"
            preExistingTempleteData += "<td>"+data["status"]+"</td>"
            preExistingTempleteData += "<td>"+"P1"+"</td>"
            preExistingTempleteData += "</tr>"
        return preExistingTempleteData

def summaryreportGenerator(summaryData,passed,fail,total):
    summaryreportData=testSummaryData(summaryData)
    preExistingTemplete = "<html>"
    preExistingTemplete += "<head>"
    preExistingTemplete += "<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC' crossorigin='anonymous'>"
    preExistingTemplete += "<style>"
    preExistingTemplete += "td {vertical-align: middle;font-size: 15px;word-wrap:break-word;border: 1px #000 solid}"
    preExistingTemplete += "td div { max-height:350px;overflow-x: hidden;overflow-y:auto}"
    preExistingTemplete += "th {vertical-align: top;background: #3ad32c;color: black;}"
    preExistingTemplete += ".topcorner{position:absolute;top:0;right:0;width: 3%;cursor:pointer;z-index: +1;}"
    preExistingTemplete += ".black_overlay{display: none;position: fixed;top: 0%;left: 0%;width: 100%;height: 100%;background-color: grey;z-index:1001;-moz-opacity: 0.8;opacity:.80;filter: alpha(opacity=80);}"
    preExistingTemplete += " .white_content {display: none;position: fixed;top: 10%;left:20px;width: 85%;height: 100%;padding: 16px;border: 2px solid ged;background-color: white;z-index:1002;overflow: auto;}"
    preExistingTemplete += "table td > div > table{width:100%;table-layout:fixed;}"
    preExistingTemplete += "table td > div > table td > div{overflow-y:auto; min-height: 10px; max-height: 200px;}"
    preExistingTemplete += "pre {box-sizing: border-box;width: 100%;padding: 0;margin: 0;overflow: auto;overflow-y: hidden;font-size: 14px;line-height: 20px;background: #efefef;border: 1px solid #777;padding: 10px;color: #333;}"
    preExistingTemplete += "div.beta{top: 25%;position: absolute;text-align: center;width: 100%;justify-content: center;background-color: #ffc;opacity: 0.3;transform: rotate(-10deg) skew(-10deg);word-break: break-all;font-size: 100px;font-weight: bold;z-index:+1;pointer-events:none;}"
    preExistingTemplete += "div#screenshot{z-index:2002;height: auto;top: auto;left:10%;padding:0px;width:80%;}"
    preExistingTemplete += "div#screenshotoverlay{z-index:2001;}"
    preExistingTemplete += "img#the-image{width:100%;cursor:pointer;}"
    preExistingTemplete += "div.image-text{top: 20%;position: absolute;text-align: center;width: 100%;justify-content: center;background-color: #ffc;opacity: 0.2;transform: rotate(-10deg) skew(-10deg);word-break: break-all;font-size: 40px;font-weight: bold;}"
    preExistingTemplete += "div.image-text:hover{display: none;}"
    preExistingTemplete += "button.prev, button.next{position:absolute;top:50%;padding-top:20px;padding-bottom:20px;opacity: 0.7;}"
    preExistingTemplete += "button.prev:hover, button.next:hover{opacity: 1;}"
    preExistingTemplete += "button.prev{left: 0;}"
    preExistingTemplete += "button.next{right:0;}"
    preExistingTemplete += ".main_features {display:flex;justify-content:center;}"
    preExistingTemplete += ".main_features p{font-size: 18px;font-weight: 700;color: #917f7f;color:#fff}"
    preExistingTemplete += ".main_features h6{margin-top: 15px;color:#fff}"
    preExistingTemplete += ".main_features img{width:70px:flex;height:70px}"
    preExistingTemplete += ".main_features ul li { border: 1px solid #dcd9d9;float: left;list-style: outside none none;margin: 0 17px 0 0;min-height: 160px;min-width: 184px;padding: 10px;text-align: center;margin: 15px}"
    preExistingTemplete += "</style>"
    preExistingTemplete += "</head>"
    preExistingTemplete += "<body>"
    preExistingTemplete += "<div id='Puytest' class='white_content' style='display: block;'>"
    preExistingTemplete += "<div style='background-color:#3ad32c;text-align:center'><p style='font-size: 34px;'>Python Test Suite :Test Summary Report</p></div>"
    preExistingTemplete += "<div class='container'>"
    preExistingTemplete += "<div class='row'>"
    preExistingTemplete += "<div class='col-md-12'>"
    preExistingTemplete += "<div class='main_features'>"
    preExistingTemplete += "<ul>"
    preExistingTemplete += "<li class='bg-success'>"
    preExistingTemplete += "<img src='../../assets/img/pass-test.png' />"
    preExistingTemplete += "<h6>"+str(passed)+"</h6>"
    preExistingTemplete += "<p>Passed Test Cases</p>"
    preExistingTemplete += "</li>"
    preExistingTemplete += "<li class='bg-danger'>"
    preExistingTemplete += "<img src='../../assets/img/fail.png' />"
    preExistingTemplete += "<h6>"+str(fail)+"</h6>"
    preExistingTemplete += "<p>Failed Test Cases</p>"
    preExistingTemplete += "</li>"
    preExistingTemplete += "<li class='bg-primary'>"
    preExistingTemplete += "<img src='../../assets/img/test.png' />"
    preExistingTemplete += "<h6>"+str(total)+"</h6>"
    preExistingTemplete += "<p>Total Test Cases</p>"
    preExistingTemplete += "</li>"
    preExistingTemplete += "</ul>"
    preExistingTemplete += "</div>"
    preExistingTemplete += "</div>"
    preExistingTemplete += "</div>"
    preExistingTemplete += "<table border='1' cellpadding='8' cellspacing='0'>"
    preExistingTemplete += "<tbody>"
    preExistingTemplete += "<tr>"
    preExistingTemplete += "<th width='15%'>Testcase</th>"
    preExistingTemplete += "<th width='20%'>Status</th>"
    preExistingTemplete += "<th width='20%'>Priority</th>"
    preExistingTemplete += "</tr>"
    preExistingTemplete += summaryreportData
    preExistingTemplete += "</tbody>"
    preExistingTemplete += "</table>"
    preExistingTemplete += "</div>"
    preExistingTemplete += "</div>"
    preExistingTemplete += "</div>"
    preExistingTemplete += "<script src = '../../assets/main.js'> </script>"
    preExistingTemplete += "<script src='https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js' integrity='sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p' crossorigin='anonymous'></script>"
    preExistingTemplete += "<script src='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js' integrity='sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF' crossorigin='anonymous'></script>"
    preExistingTemplete += "</body>"
    preExistingTemplete += "</html>"

    openHtmlFile = open(getModulePath()+Constant.emsReportPath+"Testsummary.html", "w")
    openHtmlFile.write(preExistingTemplete)
def getModulePath():
    path = os.path.dirname(EMSWS.__file__)
    return path

