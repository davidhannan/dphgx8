import pytest
import System
import json
import os
import Staff


def test_grade_change(grading_system):
    staff = Staff.Staff()
    staff.users = grading_system.users

    staff.change_grade("yted91", "software_engineering", "assignment1", 40)


    path = os.getcwd()+"/Data/users.json"
    with open(path) as f:
        data = json.load(f)

    assert data["yted91"]["courses"]["software_engineering"]["assignment1"]["grade"] == 40

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
