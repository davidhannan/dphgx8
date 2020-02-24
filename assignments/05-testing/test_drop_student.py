import System
import Professor
import json
import pytest

def test_drop_student(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.drop_student('hdjsr7', 'software_engineering')

    with open('Data/users.json') as f:
        data = json.load(f)

    assert "software_engineering" not in data['hdjsr7']['courses']

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
