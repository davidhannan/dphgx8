import pytest
import System

def test_login(grading_system):
    username = "calyam"
    password= "#Yeet"
    assert grading_system.check_password(username, password) == False
    password = "#yeet"
    assert grading_system.check_password(username, password) == True
    password= "#ye3t"
    assert grading_system.check_password(username, password) == False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
