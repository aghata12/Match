from src.domain.prematch import *

def test_should_return_a_student_list_filled_with_prematch_recruiters_with_same_skills():
    student_list=[{"NOMBRE Y APELLIDOS": "AST Alba Azcano Crespo",
                       "PROMOCION": "AST",
                       "LOCATIONS":["AST"],
                       "SKILLS":["JAVASCRIPT","VUE"],
                       "PMATCH":[],
                       "DONE":[],
                       "BLOCKEDH":[]}]

    recruiter_list= [{"EMPRESA": "AST-ABAMobile",
            "NOMBRE DEL RECRUITER": "Laura Selina SÁNCHEZ",
            "EMAIL": "-",
            "CARGO": "Administracion y RRHH",
            "LINKEDIN": "https://www.linkedin.com/in/laura-selina-s-6ab10120a/",
            "LOCATIONS":["AST"],
            "SKILLS":["PHP", "JAVA", "VUE"],
            "HOURS_DISP":["10:10","10:20","10:30","10:40","10:50",
                          "11:00","11:20","11:30","11:40","11:50",
                          "12:00","12:10","12:30","12:40","12:50"]}]

    expected=[{"NOMBRE Y APELLIDOS": "AST Alba Azcano Crespo",
                       "PROMOCION": "AST",
                       "LOCATIONS":["AST"],
                       "SKILLS":["JAVASCRIPT","VUE"],
                       "PMATCH":["Laura Selina SÁNCHEZ"],
                       "DONE":[],
                       "BLOCKEDH":[]}]

    result=fill_skills_and_recruiters_in_students(recruiter_list,student_list)
    assert result == expected
