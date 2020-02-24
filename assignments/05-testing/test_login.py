import pytest
import System
import os
import json

def test_login(grading_system):
    username = "calyam"
    password= "#yeet"
    grading_system.login(username, password)
    grading_system.usr.name = "calyam"

    path = os.getcwd()+"/Data/users.json"
    with open(path) as json_file:
        data = json.load(json_file)

    role = data[username]['role']

    assert role == "professor"

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
