from src.webserver import create_app
from src.domain.prematch import *

def test_should_return_error_if_spreadsheet_name_is_incorrect():
    app = create_app(repositories={})
    client = app.test_client()
    coder=[{"NOMBRE Y APELLIDOS": "AST Alba Azcano Crespo",
        "PROMOCION": "AST",
        "L-BIO": "",
        "L-AST": "x",
        "L-BCN": "",
        "S-JAVASCRIPT": "x",
        "S-VUE": "x",
        "S-JAVA": "x",
        "S-PHP": "",
        "S-PYTHON": ""}]
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
        "10:20": "x"}]

    expected={"error":"Entrada incorrecta"}

    prematch=client.post("/api/prematch",json={"coders":coder,"RECRUITERS":recruiter})
    result=prematch.json

    assert prematch.status_code == 400
    assert result == expected


def test_no_returns_match_because_recruiter_does_not_have_hours_selected():
    app = create_app(repositories={})
    client = app.test_client()
    coder=[{"NOMBRE Y APELLIDOS": "AST Alba Azcano Crespo",
        "PROMOCION": "AST",
        "L-BIO": "",
        "L-AST": "x",
        "L-BCN": "",
        "S-JAVASCRIPT": "x",
        "S-VUE": "x",
        "S-JAVA": "x",
        "S-PHP": "",
        "S-PYTHON": ""}]

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
        "S-PYTHON": "X"}]

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
        "S-PYTHON": "X"}]

    

    prematch=client.post("/api/prematch",json={"CODERS":coder,"RECRUITERS":recruiter})
    result=prematch.json

    assert result == expected