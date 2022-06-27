from src.webserver import create_app
from src.domain.prematch import *


def test_should_return_match_if_coincidence_btw_recruiter_and_coder():
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
        "10:20": ""}]

    prematch=client.post("/api/prematch",json={"CODERS":coder,"RECRUITERS":recruiter})
    result=prematch.json

    assert prematch.status_code == 200
    assert result == expected

#2----------------------------------------------------------------------

def test_should_not_generate_match_if_no_coincidence_btw_coder_and_rec():
    app = create_app(repositories={})
    client = app.test_client()
    coder=[{"NOMBRE Y APELLIDOS": "AST Alba Azcano Crespo",
        "PROMOCION": "AST",
        "L-BIO": "",
        "L-AST": "x",
        "L-BCN": "",
        "S-JAVASCRIPT": "x",
        "S-VUE": "x",
        "S-JAVA": "",
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
        "10:10": "",
        "10:20": ""}]

    prematch=client.post("/api/prematch",json={"CODERS":coder,"RECRUITERS":recruiter})
    result=prematch.json

    assert prematch.status_code == 200
    assert result == expected

#3----------------------------------------------------------------------

def test_should_put_mark_on_result_if_recruiter_is_no_available_in_schedule():
    app = create_app(repositories={})
    client = app.test_client()
    coder=[{"NOMBRE Y APELLIDOS": "AST Alba Azcano Crespo",
        "PROMOCION": "AST",
        "L-BIO": "",
        "L-AST": "x",
        "L-BCN": "",
        "S-JAVASCRIPT": "x",
        "S-VUE": "x",
        "S-JAVA": "",
        "S-PHP": "",
        "S-PYTHON": "x"},
        {"NOMBRE Y APELLIDOS": "AST Vicky Pinero",
        "PROMOCION": "AST",
        "L-BIO": "",
        "L-AST": "x",
        "L-BCN": "",
        "S-JAVASCRIPT": "x",
        "S-VUE": "x",
        "S-JAVA": "",
        "S-PHP": "x",
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
        "10:20": "x",
        "10:30": ""}]

    prematch=client.post("/api/prematch",json={"CODERS":coder,"RECRUITERS":recruiter})
    result=prematch.json

    assert prematch.status_code == 200

    assert result[0]["10:10"] == "AST Alba Azcano Crespo" or "AST Vicky Pinero"
    assert result[0]["10:20"] == "AST Alba Azcano Crespo" or "AST Vicky Pinero"
    assert result[0]["10:30"] == "N/D"
    