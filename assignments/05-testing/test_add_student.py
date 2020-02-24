import System
import Professor
import json
import pytest

def test_add_student(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.add_student('yted91', 'databases')


    with open('Data/users.json') as f:
        data = json.load(f)

    assert "databases" in data['yted91']['courses']

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
