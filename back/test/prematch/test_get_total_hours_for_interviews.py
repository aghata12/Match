from src.domain.prematch import *

def test_should_return_the_hours_for_interviews():
    recruiter = {
        "EMPRESA": "Merkatu",
        "NOMBRE DEL RECRUITER": "Andres",
        "EMAIL": "andres@merkatu.com",
        "CARGO": "Director",
        "U-BILBAO": "x",
        "S-PYTHON": "x",
        "10:10": "x",
        "10:20": "x",
        "13:00": "",
        "13:30": "x"}

    result=get_total_hours_for_interviews(recruiter)
    expected=["10:10","10:20","13:00","13:30"]

    assert result == expected