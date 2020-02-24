import System
import pytest
import Staff
import json

def test_create_assignment(grading_system):
    staff = Staff.Staff()
    staff.all_courses = grading_system.courses

    staff.create_assignment("testAssignment", "3/3/20", "software_engineering")

    with open('Data/courses.json') as f:
        data = json.load(f)

    assert data["software_engineering"]["assignments"]["testAssignment"]["due_date"] == "3/3/20"

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
