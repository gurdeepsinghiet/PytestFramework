import psutil
import  pytest
import logging
import os
import EMSWS.EMSConfig as Constant
from EMSWS.factories.EMSFuntions import EMSFactory
LOGGER = logging.getLogger(__name__)

@pytest.fixture(autouse=True)
def reportFixture():
    ems = EMSFactory()
    return locals()

@pytest.fixture(autouse=True)
def getReportPytestHook(reportFixture):
    v=reportFixture['ems']
    yield v
    v.reportGenerator()


def pytest_sessionstart(session):
    session.results = dict()

LIMIT = 5
SHARED_MEMORY_USAGE_INFO = "memory_usage"


def pytest_configure(config):
    """
    Defined appropriate plugins selection in pytest_configure hook
    Parameters
    ----------
    config : _pytest.config.Config
    """
    plugin = Reporting(config)
    config.pluginmanager.register(plugin)


def is_master(config):
    """True if the code running the given pytest.config object is running in a xdist master
    node or not running xdist at all.
    """
    return not hasattr(config, 'workerinput')


def get_usage_memory():
    """
    Measures memory usage per Python process
    Returns
    -------
    memory_usage : float
    """
    process = psutil.Process(os.getpid())
    memory_use = process.memory_info()
    return memory_use.rss / 1024  # to KB

def testSummaryData(summaryData):
        preExistingTempleteData = ""
        for data in summaryData:
            preExistingTempleteData += "<tr>"
            preExistingTempleteData += "<td>" + data["testCaseFile"] + "</td>"
            preExistingTempleteData += "<td width='150px'>"
            preExistingTempleteData += "<div><a href='" + data["testcasename"] + ".html'>" + \
                                       data["testcasename"].split("[")[0] + "</a></div>"
            preExistingTempleteData += "</td>"
            preExistingTempleteData += "<td>" + data["status"] + "</td>"
            preExistingTempleteData += "<td>" + "P1" + "</td>"
            preExistingTempleteData += "</tr>"
        return preExistingTempleteData

def summaryreportGenerator(summaryData, passed, fail, total):
    passedPercentage = (passed / (total)) * 100
    failedPercenatge = (fail / (total)) * 100
    passedPercentage = round(passedPercentage, 2)
    failedPercenatge = round(failedPercenatge, 2)
    summaryreportData = testSummaryData(summaryData)
    preExistingTemplete = "<html>"
    preExistingTemplete += "<head>"
    preExistingTemplete += "<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC' crossorigin='anonymous'>"
    preExistingTemplete += "<style>"
    preExistingTemplete += "td {vertical-align: middle;font-size: 15px;word-wrap:break-word;border: 1px #000 solid}"
    preExistingTemplete += "td div { max-height:350px;overflow-x: hidden;overflow-y:auto}"
    preExistingTemplete += "th {vertical-align: top;background: #2C2F73;color: #fff;}"
    preExistingTemplete += ".topcorner{position:absolute;top:0;right:0;width: 3%;cursor:pointer;z-index: +1;}"
    preExistingTemplete += ".black_overlay{display: none;position: fixed;top: 0%;left: 0%;width: 100%;height: 100%;background-color: grey;z-index:1001;-moz-opacity: 0.8;opacity:.80;filter: alpha(opacity=80);}"
    preExistingTemplete += " .white_content {display: none;top: 10%;left:20px;width: 85%;height: 100%;padding: 16px;border: 2px solid ged;background-color: white;z-index:1002;overflow: auto;}"
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
    preExistingTemplete += "<div style='background-color:#2C2F73;color:#fff;text-align:center'><p style='font-size: 34px;'>Demo Test Suite :Test Summary Report</p></div>"
    preExistingTemplete += "<div class='container'>"
    preExistingTemplete += "<div class='row'>"
    preExistingTemplete += "<div class='col-md-12'>"
    preExistingTemplete += "<div class='main_features'>"
    preExistingTemplete += "<svg id='pie1' class='chart'>"
    preExistingTemplete += "<g>"
    preExistingTemplete += "<rect x='382' y='58' width='136' height='37' stroke='none' stroke-width='0' fill-opacity='0' fill='#ffffff'></rect>"
    preExistingTemplete += "<g column-id='Failed - 1'>"
    preExistingTemplete += "<rect x='382' y='58' width='136' height='14' stroke='none' stroke-width='0' fill-opacity='0' fill='#ffffff'></rect>"
    preExistingTemplete += "<g>"
    preExistingTemplete += "<text text-anchor='start' x='401' y='69.9' font-family='Arial' font-size='14' stroke='none' stroke-width='0' fill='#222222'>Failed - " + str(
        failedPercenatge) + "% Failed</text>"
    preExistingTemplete += "</g>"
    preExistingTemplete += "</g>"
    preExistingTemplete += "<circle cx='389' cy='65' r='7' stroke='none' stroke-width='0' fill='#ff0000'></circle>"
    preExistingTemplete += "</g>"
    preExistingTemplete += "<g column-id='Skipped - 3'>"
    preExistingTemplete += "<rect x='382' y='81' width='136' height='14' stroke='none' stroke-width='0' fill-opacity='0' fill='#ffffff'></rect>"
    preExistingTemplete += "<g>"
    preExistingTemplete += "<text text-anchor='start' x='401' y='92.9' font-family='Arial' font-size='14' stroke='none' stroke-width='0' fill='#222222'>Passed -" + str(
        passedPercentage) + "% Passed</text>"
    preExistingTemplete += "</g>"
    preExistingTemplete += "<circle cx='389' cy='88' r='7' stroke='none' stroke-width='0' fill='#3ad32c'></circle>"
    preExistingTemplete += "</g>"
    preExistingTemplete += "</g>"
    preExistingTemplete += "</svg>"
    preExistingTemplete += "</div>"
    preExistingTemplete += "</div>"
    preExistingTemplete += "<div class='col-md-12'>"
    preExistingTemplete += "<div class='main_features'>"
    preExistingTemplete += "<ul>"
    preExistingTemplete += "<li style='background:#3ad32c;'>"
    preExistingTemplete += "<img src='../../assets/img/pass.png' />"
    preExistingTemplete += "<h6 id='pass'>" + str(passed) + "</h6>"
    preExistingTemplete += "<p>Passed Test Cases</p>"
    preExistingTemplete += "</li>"
    preExistingTemplete += "<li class='bg-danger'>"
    preExistingTemplete += "<img src='../../assets/img/fail.png' />"
    preExistingTemplete += "<h6 id='fail'>" + str(fail) + "</h6>"
    preExistingTemplete += "<p>Failed Test Cases</p>"
    preExistingTemplete += "</li>"
    preExistingTemplete += "<li class='bg-primary'>"
    preExistingTemplete += "<img src='../../assets/img/test.png' />"
    preExistingTemplete += "<h6 id='total'>" + str(total) + "</h6>"
    preExistingTemplete += "<p>Total Test Cases</p>"
    preExistingTemplete += "</li>"
    preExistingTemplete += "</ul>"
    preExistingTemplete += "</div>"
    preExistingTemplete += "</div>"
    preExistingTemplete += "</div>"
    preExistingTemplete += "<table border='1' cellpadding='8' cellspacing='0'>"
    preExistingTemplete += "<tbody>"
    preExistingTemplete += "<tr>"
    preExistingTemplete += "<th width='15%'>TestFile</th>"
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

    openHtmlFile = open(getModulePath() + Constant.emsReportPath + "Testsummary.html", "w")
    openHtmlFile.write(preExistingTemplete)


def getModulePath():
    path = os.path.dirname(__file__)
    return path


class Reporting:
    def __init__(self, config):
        """
        Defined appropriate plugins selection in pytest_configure hook
        Parameters
        ----------
        config : _pytest.config.Config
        """
        self.config = config
        self.is_master = is_master(config)
        self.stats = {}
        self.reportSet=set()

    def add(self, name):
        self.stats[name] = self.stats.get(name) or {}
        return self.stats[name]

    def pytest_runtest_setup(self, item):
        """Record maxrss for pre-setup."""
        self.add(item.nodeid)["setup"] = get_usage_memory()

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_call(self, item):
        """
        Track test memory
        Parameters
        ----------
        item : _pytest.main.Item
        """
        start = get_usage_memory()
        yield
        end = get_usage_memory()
        self.add(item.nodeid)["diff"] = end - start
        self.add(item.nodeid)["end"] = end
        self.add(item.nodeid)["start"] = start

    def pytest_terminal_summary(self, terminalreporter):
        tr = terminalreporter
        if self.stats:
            tr._tw.sep("=", "TOP {} tests which took most RAM".format(LIMIT), yellow=True)
            stats = sorted(self.stats.items(), key=lambda x: x[-1]["diff"], reverse=True)
            for test_name, info in stats[:LIMIT]:
                line = "setup({}KB) usage ({}KB) - {} ".format(info["setup"], info["diff"], test_name)
                tr._tw.line(line)

    def pytest_testnodedown(self, node, error):
        """
        Get statistic about memory usage for test cases from xdist nodes
        and merge to master stats
        """
        node_stats = node.workeroutput[SHARED_MEMORY_USAGE_INFO]
        self.stats.update(node_stats)

    def pytest_sessionstart(self,session):
        session.results = dict()

    def pytest_runtest_logreport(self,report):
        if report and report.when and report.when == 'call':
            self.reportSet.add(report.nodeid.split("::")[1]+"#" +report.outcome+"#"+report.nodeid.split("::")[0])
            print(self.reportSet)


    @pytest.hookimpl(hookwrapper=True, trylast=True)
    def pytest_sessionfinish(self, session, exitstatus):
        LOGGER.info(self.reportSet )
        passed_amount = sum(1 for result in self.reportSet if result.split("#")[1] == "passed")
        failed_amount = sum(1 for result in self.reportSet if result.split("#")[1] == "failed")
        totalCase = passed_amount + failed_amount
        print(f'there are {passed_amount} passed and {failed_amount} failed tests in {totalCase} Total test cases')
        summary = []
        for result in self.reportSet:
            summaryPram = {}
            if result.split("#")[1] == "passed":
                LOGGER.info((result.split("#")[2]))
                summaryPram["testCaseFile"] = result.split("#")[2]
                summaryPram["testcasename"] = result.split("#")[0]
                summaryPram["status"] = "Passed"
                summary.append(summaryPram)
            elif result.split("#")[1] == "failed":
                summaryPram["testCaseFile"] = result.split("#")[2]
                summaryPram["testcasename"] = result.split("#")[0]
                summaryPram["status"] = "Failed"
                summary.append(summaryPram)

        summaryreportGenerator(summary, passed_amount, failed_amount, totalCase)
        """
        Dump memory usage statistics to `workeroutput`
        Executed once per node if with xdist and will gen from mater node
        Parameters
        ----------
        session : _pytest.Session
        exitstatus : int
        """
        yield
        if not self.is_master:
            self.config.workeroutput[SHARED_MEMORY_USAGE_INFO] = self.stats