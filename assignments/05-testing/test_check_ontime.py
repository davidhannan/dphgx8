import System
import json
import pytest

def test_check_ontime(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    assert grading_system.usr.check_ontime('3/1/20','3/2/20') == True
    assert grading_system.usr.check_ontime('3/3/20','3/2/20') == False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
