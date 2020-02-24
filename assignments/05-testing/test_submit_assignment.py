import System
import json
import pytest

def test_submit_assignment(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.submit_assignment('cloud_computing', 'assignment1','Blahhhhh', '03/01/20')

    with open('Data/users.json') as f:
        data = json.load(f)

    assert data['hdjsr7']['courses']['cloud_computing']['assignment1']['submission'] == 'Blahhhhh'
    assert data['hdjsr7']['courses']['cloud_computing']['assignment1']['submission_date'] == '03/01/20'

    grading_system.login('yted91', 'imoutofpasswordnames')
    grading_system.usr.submit_assignment('cloud_computing', 'assignment1','Blahhhhh', '03/01/20')

    assert data['yted91']['courses']['cloud_computing']['assignment1']['submission'] == 'Blahhhhh'
    assert data['yted91']['courses']['cloud_computing']['assignment1']['submission_date'] == '03/01/20'

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
