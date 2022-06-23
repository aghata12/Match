from src.domain.prematch import *

def test_should_empty_spaces_on_matrix():
    matrix=[{"EMPRESA":"AST-ABAMobile",
               "NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ",
               "HORARIO":"10:10","ESTUDIANTE":"AST Alba Azcano Crespo"},
              {"EMPRESA":"AST-ABAMobile",
               "NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ",
               "HORARIO":"10:20"}]

    expected=[{"EMPRESA":"AST-ABAMobile",
               "NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ",
               "HORARIO":"10:10","ESTUDIANTE":"AST Alba Azcano Crespo"},
              {"EMPRESA":"AST-ABAMobile",
               "NOMBRE DEL RECRUITER":"Laura Selina SÁNCHEZ",
               "HORARIO":"10:20","ESTUDIANTE":""}]

    result=fill_empties(matrix)
    assert result == expected