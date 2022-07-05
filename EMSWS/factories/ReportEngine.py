import logging
import os
import EMSWS
import  EMSWS.EMSConfig as Constant
LOGGER = logging.getLogger(__name__)
class ReportGenerator():
    testsummaryData=[]
    def __init__(self):
        pass
    def reportGenerator(self):
        running_testcases = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        preExistingTemplete="<html>"+"<head>"+"<style>"
        preExistingTemplete +="td {vertical-align: middle;font-size: 15px;word-wrap:break-word;}"
        preExistingTemplete += "td div { max-height:350px;overflow-x: hidden;overflow-y:auto}"
        preExistingTemplete += "th {vertical-align: top;background: #2C2F73;color: #fff;}"
        preExistingTemplete += ".topcorner{position:absolute;top:0;right:0;width: 3%;cursor:pointer;z-index: +1;}"
        preExistingTemplete += ".black_overlay{display: none;position: fixed;top: 0%;left: 0%;width: 100%;height: 100%;background-color: grey;z-index:1001;-moz-opacity: 0.8;opacity:.80;filter: alpha(opacity=80);}"
        preExistingTemplete += " .white_content {display: none;position: fixed;top: 0%;left:20px;width: 97%;height: 80%;padding: 16px;border: 2px solid ged;background-color: white;z-index:1002;overflow: auto;}"
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
        preExistingTemplete += "</style>"
        preExistingTemplete += "</head>"
        preExistingTemplete += "<body>"
        preExistingTemplete += "<div id='Puytest' class='white_content' style='display: block;'>"
        preExistingTemplete += "<div style='background-color:#2C2F73;color:#fff;text-align:center'><p style='font-size: 34px;' id='testSummaryheader'>"+running_testcases+"</p></div>"
        preExistingTemplete += "<table border='1' cellpadding='8' cellspacing='0'>"
        preExistingTemplete += "<tbody>"
        preExistingTemplete += "<tr>"
        preExistingTemplete += "<th width='15%'>API Name</th>"
        preExistingTemplete += "<th width='20%'>Request Inputs</th>"
        preExistingTemplete += "<th width='10%'>Exp. Ret. Code</th>"
        preExistingTemplete += "<th width='10%'>Act Ret. Code</th>"
        preExistingTemplete += "<th width='25%'>Exp Response</th>"
        preExistingTemplete += "<th width='25%'>Act Response</th>"
        #preExistingTemplete += "<th width='10%'>Response Time</th>"
        preExistingTemplete += "<th width='10%'>Status</th>"
        preExistingTemplete += "<th width='15%'>Comments</th>"
        preExistingTemplete += "</tr>"
        preExistingTemplete += self.tableGenerator()
        preExistingTemplete += "</tbody>"
        preExistingTemplete += "</table>"
        preExistingTemplete += "</div>"
        preExistingTemplete += "</div>"
        preExistingTemplete += "<script src = '../../assets/main.js'> </script>"
        preExistingTemplete += "</body>"
        preExistingTemplete += "</html>"
        openHtmlFile = open(self.getModulePath()+Constant.emsReportPath+running_testcases+".html","w")
        openHtmlFile.write(preExistingTemplete)
        openHtmlFile.close()

    def getModulePath(self):
        path = os.path.dirname(EMSWS.__file__)
        return path

    def tableGenerator(self):
        reportDataDic=self.getReportData()
        preExistingTempleteData = ""
        for data in reportDataDic:
            preExistingTempleteData += "<tr>"
            preExistingTempleteData += "<td>"+data["Api_Name"]+"</td>"
            preExistingTempleteData += "<td width='150px'>"
            preExistingTempleteData += "<div>"+str(data["inputs"])+"</div>"
            preExistingTempleteData += "</td>"
            preExistingTempleteData += "<td>"+str(data["Expected_Code"])+"</td>"
            preExistingTempleteData += "<td>"+str(data["actual_Code"])+"</td>"
            preExistingTempleteData += "<td width='150px'><div>"+str(data["Expected_Response"])+"<div></div></div></td>"
            preExistingTempleteData += "<td width='150px'>"
            preExistingTempleteData += "<div style='max-width:350px'>"+str(data["Act_Response"])+"</div>"
            preExistingTempleteData += "</td>"
            #preExistingTempleteData += "<td>"+str(data["Response_time"])+"</td>"
            preExistingTempleteData += "<td>"+data["Status"]+"</td>"
            preExistingTempleteData += "<td><div><div></div></div></td>"
            preExistingTempleteData += "</tr>"
        return preExistingTempleteData

    def getReportData(self)->list:
        LOGGER.info(self.data)
        return self.data


    def ConsolidatedReport(self):
        f = open('abc.txt', 'w')
