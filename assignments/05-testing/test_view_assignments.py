import System
import json
import pytest

def test_view_assignments(grading_system):
    grading_system.login('akend3', '123454321')

    with open('Data/users.json') as f:
        data = json.load(f)

    assignments = grading_system.usr.view_assignments('comp_sci')

    assignment = data['akend3']['courses']['comp_sci']['assignment1']['submission_date']

    assert assignment == assignments[0][1]
    assignment = data['akend3']['courses']['comp_sci']['assignment2']['submission_date']
    assert assignment == assignments[1][1]
    assignments = grading_system.usr.view_assignments('databases')
    assignment = data['akend3']['courses']['databases']['assignment1']['submission_date']
    assert assignment == assignments[0][1]
    assignment = data['akend3']['courses']['databases']['assignment2']['submission_date']
    assert assignment == assignments[1][1]

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
