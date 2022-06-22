from src.domain.recruiter import *

def test_should_return_empty_list_of_recruiters():
    recruiters=[]
    result=get_recruiter_list(recruiters)
    expected=[]
    assert result == expected

def test_convert_to_recruiters_list():
    recruiter=[{"EMPRESA": "AST-ABAMobile",
                "NOMBRE DEL RECRUITER": "Laura Selina SÁNCHEZ",
                "EMAIL": "-",
                "CARGO": "Administracion y RRHH",
                "LINKEDIN": "https://www.linkedin.com/in/laura-selina-s-6ab10120a/",
                "L-BCN": "",
                "L-AST": "X",
                "L-BIO": "",
                "S-PHP": "X",
                "S-JAVA": "X",
                "S-PYTHON": "X",
                "10:10": "x",
                "10:20": "x",
                "10:30": "x",
                "10:40": "x",
                "10:50": "x",
                "11:00": "x",
                "11:20": "x",
                "11:30": "x",
                "11:40": "x",
                "11:50": "x",
                "12:00": "x",
                "12:10": "x",
                "12:30": "x",
                "12:40": "x",
                "12:50": "x"}]

    expected= [{"EMPRESA": "AST-ABAMobile",
            "NOMBRE DEL RECRUITER": "Laura Selina SÁNCHEZ",
            "EMAIL": "-",
            "CARGO": "Administracion y RRHH",
            "LINKEDIN": "https://www.linkedin.com/in/laura-selina-s-6ab10120a/",
            "LOCATIONS":["AST"],
            "SKILLS":["PHP", "JAVA", "PYTHON"],
            "HOURS_DISP":["10:10","10:20","10:30","10:40","10:50",
                          "11:00","11:20","11:30","11:40","11:50",
                          "12:00","12:10","12:30","12:40","12:50"]}]

    assert get_recruiter_list(recruiter) == expected