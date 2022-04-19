import logging
LOGGER = logging.getLogger(__name__)

class EMSAssertionFactory:

    def __init__(self):
        pass
    def getAssertions(self,expected,actual):

        try:
            LOGGER.info("Comparing "+expected+" Value with "+actual)
            assert expected == actual
        except AssertionError:
            LOGGER.error("expected value " + expected + " is not matched with "+actual)

        return self