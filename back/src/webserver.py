
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.lib.utils import object_to_json

from src.domain.students import get_student_list
from src.domain.recruiter import get_recruiter_list, format_recruiter
from src.domain.prematch import *


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"


    @app.route("/api/prematch", methods=["POST"])
    def post_coders():
        body = request.json
        if not("CODERS" or "RECRUITERS") in body.keys():
            return jsonify({"error":"Entrada incorrecta"}), 400
        else:
            students = body["CODERS"]
            recruiters_origen = body["RECRUITERS"]
            recruiters_orig= format_recruiter(recruiters_origen)
            recruiters_copy=recruiters_orig[:]
            
            student_list=get_student_list(students)
            recruiter_list=get_recruiter_list(recruiters_copy)
            hours=get_total_hours_for_interviews(recruiters_copy[0])

            coincidences_st_rec_st_list=fill_skills_and_recruiters_in_students(recruiter_list,student_list)
            matrix=generate_matrix(recruiter_list,hours)
            matrix_no_available_hours=fill_recruiter_no_available_spaces(matrix,recruiter_list)
            #--------------------------------------------------
            #2 segmento que se puede implementar para posiciones forzadas--->ver abajo
            #--------------------------------------------------
            matrix_filled=match_students(matrix_no_available_hours,coincidences_st_rec_st_list)

            matrix_final=fill_empties(matrix_filled)
            final_json=fill_data_to_recruiter_list(matrix_final,recruiters_orig)
            
            return jsonify(final_json), 200

    return app





    


            #--------------------------------------------------
            #2- rellena matriz con las posiciones forzadas
            #matrix_prefilled=fill_matrix_with_forced_positions(matrix_no_available_hours,forced_positions)

            # en student_list rellena los horarios y empresa con los forzados
            #student_list_blocked_hours=forced_matches(forced_positions,coincidences_st_rec_st_list)
            # matrix_filled=match_students(matrix_prefilled,student_list_blocked_hours)
            #--------------------------------------------------