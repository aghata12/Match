from src.domain.prematch import *

def test_should_fill_the_matrix_with_students():

    matrix=[{"EMPRESA":"AST-ABAMobile",
               "NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ",
               "HORARIO":"10:10"},
              {"EMPRESA":"AST-ABAMobile",
               "NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ",
               "HORARIO":"10:20"}]
    
    student_list=[{"NOMBRE Y APELLIDOS": "AST Alba Azcano Crespo",
                       "PROMOCION": "AST",
                       "LOCATIONS":["AST"],
                       "SKILLS":["JAVASCRIPT","VUE"],
                       "PMATCH":["Laura Selina SÁNCHEZ"],
                       "DONE":[],
                       "BLOCKEDH":[]}]

    expected=[{"EMPRESA":"AST-ABAMobile",
               "NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ",
               "HORARIO":"10:10","ESTUDIANTE":"AST Alba Azcano Crespo"},
              {"EMPRESA":"AST-ABAMobile",
               "NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ",
               "HORARIO":"10:20"}]
               
    result=match_students(matrix,student_list)

    assert result == expected