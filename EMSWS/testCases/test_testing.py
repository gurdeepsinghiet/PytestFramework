import pytest


def test_first(emsObjectFixture):
    ems = emsObjectFixture['ems']
    ems.verifyAssertions(11*2,22)


def test_second(emsObjectFixture):
    ems = emsObjectFixture['ems']
    ems.verifyAssertions(11*2,22)

def test_second4(emsObjectFixture):
    ems = emsObjectFixture['ems']
    ems.verifyAssertions(11*2,22)

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output,emsObjectFixture):
    ems = emsObjectFixture['ems']
    ems.verifyAssertions(11*num,output)

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_12(num, output,emsObjectFixture):
    ems = emsObjectFixture['ems']
    ems.verifyAssertions(11*num,output)
