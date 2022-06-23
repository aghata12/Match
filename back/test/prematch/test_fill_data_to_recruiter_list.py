from src.domain.prematch import *

def test_should_fill_student_in_hour_in_the_recruiter_list():
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
                "10:30": "x"}]

    matrix=[{"EMPRESA":"AST-ABAMobile",
               "NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ",
               "HORARIO":"10:10","ESTUDIANTE":"AST Alba Azcano Crespo"},
              {"EMPRESA":"AST-ABAMobile",
               "NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ",
               "HORARIO":"10:20","ESTUDIANTE":""},
               {"EMPRESA":"AST-ABAMobile",
               "NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ",
               "HORARIO":"10:30","ESTUDIANTE":""}]

    expected=[{"EMPRESA": "AST-ABAMobile",
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
                "10:10": "AST Alba Azcano Crespo",
                "10:20": "",
                "10:30": ""}]

    result=fill_data_to_recruiter_list(matrix,recruiter)

    assert result == expected