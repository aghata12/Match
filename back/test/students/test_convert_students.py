from src.domain.students import *

def test_should_return_empty_list():
    students=[]
    result=get_student_list(students)
    expected=[]
    assert result == expected

def test_should_return_a_list_of_students():
    students=[{ "L-AST": "x",
                "L-BCN": "",
                "L-BIO": "",
                "NOMBRE Y APELLIDOS": "AST Alba Azcano Crespo",
                "PROMOCION": "AST",
                "S-JAVA": "",
                "S-JAVASCRIPT": "x",
                "S-PHP": "",
                "S-PYTHON": "",
                "S-VUE": "x"
                }]

    expected=[{"NOMBRE Y APELLIDOS": "AST Alba Azcano Crespo",
                "PROMOCION": "AST",
                "LOCATIONS":["AST"],
                "SKILLS":["JAVASCRIPT","VUE"],
                "PMATCH":[],
                "DONE":[],
                "BLOCKEDH":[]}]

    assert get_student_list(students) == expected



