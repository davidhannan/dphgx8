import System
import json
import pytest

#test that a professor should not be able to drop a student from a course they dont teach
def test_wrong_professor(grading_system):
    grading_system.login('calyam', '#yeet')
    grading_system.usr.drop_student('hdjsr7', 'databases')
    with open('Data/users.json') as f:
        data = json.load(f)
    assert "databases" in data['hdjsr7']['courses']

#test to make sure students cant create assignments
def test_student_create_assignment(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.create_assignment('testAssignment', '03/34/20', 'cloud_computing')

#test to make sure students cant see grades from a course they are not in
#user hdjsr7 gets dropped out of databases by the test_wrong_professor so this is accurate
def test_student_wrongcourse_grades(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grades = grading_system.usr.check_grades('databases')

#test to see if a student can make a submission to a course they are not in
#user hdjsr7 gets dropped out of databases by the test_wrong_professor so this is accurate
def test_submit_wrong_course(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.submit_assignment('databases', 'assignment1','testSubmission', '03/18/20')

#test to make sure a student cant drop another student
def test_student_drop_student(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.drop_student('akend3', 'databases')

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
