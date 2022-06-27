from src.webserver import create_app
from src.domain.prematch import *


def test_should_return_match_if_coincidence_in_location():
    app = create_app(repositories={})
    client = app.test_client()
    coder=[{"NOMBRE Y APELLIDOS": "AST Alba Azcano Crespo",
        "PROMOCION": "AST",
        "L-BIO": "",
        "L-AST": "x",
        "L-BCN": ""}]
    recruiter=[{"EMPRESA": "AST-ABAMobile",
        "NOMBRE DEL RECRUITER": "Laura Selina SÁNCHEZ",
        "EMAIL": "-",
        "CARGO": "Administracion y RRHH",
        "LINKEDIN": "https://www.linkedin.com/in/laura-selina-s-6ab10120a/",
        "L-BCN": "",
        "L-AST": "X",
        "L-BIO": "",
        "10:10": "x",
        "10:20": ""}]

    expected=[{"EMPRESA": "AST-ABAMobile",
        "NOMBRE DEL RECRUITER": "Laura Selina SÁNCHEZ",
        "EMAIL": "-",
        "CARGO": "Administracion y RRHH",
        "LINKEDIN": "https://www.linkedin.com/in/laura-selina-s-6ab10120a/",
        "L-BCN": "",
        "L-AST": "X",
        "L-BIO": "",
        "10:10": "AST Alba Azcano Crespo",
        "10:20": "N/D"}]

    prematch=client.post("/api/prematch",json={"CODERS":coder,"RECRUITERS":recruiter})
    result=prematch.json

    assert prematch.status_code == 200
    assert result == expected

#----------------------------------------------------------------------

def test_should_return_result_even_when_some_keys_LI_CARGO_are_empty():
    app = create_app(repositories={})
    client = app.test_client()
    coder=[{"NOMBRE Y APELLIDOS": "AST Alba Azcano Crespo",
        "PROMOCION": "AST",
        "L-BIO": "",
        "L-AST": "x",
        "L-BCN": ""}]
    recruiter=[{"EMPRESA": "AST-ABAMobile",
        "NOMBRE DEL RECRUITER": "Laura Selina SÁNCHEZ",
        "EMAIL": "",
        "CARGO": "",
        "LINKEDIN": "",
        "L-BCN": "",
        "L-AST": "X",
        "L-BIO": "",
        "10:10": "x",
        "10:20": ""}]

    expected=[{"EMPRESA": "AST-ABAMobile",
        "NOMBRE DEL RECRUITER": "Laura Selina SÁNCHEZ",
        "EMAIL": "",
        "CARGO": "",
        "LINKEDIN": "",
        "L-BCN": "",
        "L-AST": "X",
        "L-BIO": "",
        "10:10": "AST Alba Azcano Crespo",
        "10:20": "N/D"}]

    prematch=client.post("/api/prematch",json={"CODERS":coder,"RECRUITERS":recruiter})
    result=prematch.json

    assert prematch.status_code == 200
    assert result == expected