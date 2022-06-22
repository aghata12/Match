from src.domain.prematch import *

def test_should_return_matrix_with_no_availability_for_the_recruiter_schedule():
    recruiter_list= [{"EMPRESA": "AST-ABAMobile",
            "NOMBRE DEL RECRUITER": "Laura Selina SÁNCHEZ",
            "EMAIL": "-",
            "CARGO": "Administracion y RRHH",
            "LINKEDIN": "https://www.linkedin.com/in/laura-selina-s-6ab10120a/",
            "LOCATIONS":["AST"],
            "SKILLS":["PHP", "JAVA", "VUE"],
            "HOURS_DISP":["10:10"]}]

    matrix=[{"EMPRESA":"AST-ABAMobile" ,"NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ","HORARIO":"10:10"},
            {"EMPRESA":"AST-ABAMobile" ,"NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ","HORARIO":"10:20"}]                  

    expected=[{"EMPRESA":"AST-ABAMobile" ,"NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ","HORARIO":"10:10"},
            {"EMPRESA":"AST-ABAMobile" ,"NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ","HORARIO":"10:20","ESTUDIANTE":"N/D"}]

    result=fill_recruiter_no_available_spaces(matrix,recruiter_list)

    assert result == expected
