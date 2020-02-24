import System
import json
import pytest


def test_check_grades(grading_system):
    grading_system.login('akend3', '123454321')

    with open('Data/users.json') as f:
        data = json.load(f)

    grades = grading_system.usr.check_grades('comp_sci')

    grade = data['akend3']['courses']['comp_sci']['assignment1']['grade']

    assert grade == grades[0][1]
    grade = data['akend3']['courses']['comp_sci']['assignment2']['grade']
    assert grade == grades[1][1]
    grades = grading_system.usr.check_grades('databases')
    grade = data['akend3']['courses']['databases']['assignment1']['grade']
    assert grade == grades[0][1]
    grade = data['akend3']['courses']['databases']['assignment2']['grade']
    assert grade == grades[1][1]

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
