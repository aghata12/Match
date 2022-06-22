from src.domain.prematch import *

def test_should_generate_matrix_for_recruiters_and_hours():

    recruiter_list= [{"EMPRESA": "AST-ABAMobile",
            "NOMBRE DEL RECRUITER": "Laura Selina SÁNCHEZ",
            "EMAIL": "-",
            "CARGO": "Administracion y RRHH",
            "LINKEDIN": "https://www.linkedin.com/in/laura-selina-s-6ab10120a/",
            "LOCATIONS":["AST"],
            "SKILLS":["PHP", "JAVA", "VUE"],
            "HOURS_DISP":["10:10","10:20"]}]

    hours=["10:10","10:20"]                      

    expected=[{"EMPRESA":"AST-ABAMobile",
               "NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ",
               "HORARIO":"10:10"},
              {"EMPRESA":"AST-ABAMobile",
               "NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ",
               "HORARIO":"10:20"} ]

    result=generate_matrix(recruiter_list,hours)

    assert result == expected