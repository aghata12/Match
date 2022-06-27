from src.domain.students import get_student_list
from src.domain.recruiter import get_recruiter_list
from src.domain.prematch import *
from test.prematch.setup_rec_st import coders,recruiters




def main():
    recruiters_orig=recruiters
    recruiters_copy=recruiters_orig[:]
    students=coders
    forced_positions=[['Merkatu','10:10','Perla'],['Merkatu','11:00','Ainara'],
                      ['Ibermatica','11:00','DESCANSO'],['Merkatu','10:20','Ainara']]
    student_list=get_student_list(students)
    recruiter_list=get_recruiter_list(recruiters_copy)
    student_list=fill_skills_and_recruiters_in_students(recruiter_list,student_list)
    
    hours=get_total_hours_for_interviews(recruiters_copy[0])
    print('student',hours)

    matrix=generate_matrix(recruiter_list,hours)

    matrix_no_available_hours=fill_recruiter_no_available_spaces(matrix,recruiter_list)
    
    # rellena matriz con las posiciones forzadas
    matrix_prefilled=fill_matrix_with_forced_positions(matrix_no_available_hours,forced_positions)
    # en student_list rellena los horarios y empresa con que se vio el estudiante de los forzados
    student_list_blocked_hours=forced_matches(forced_positions,student_list)

    matrix_filled=match_students(matrix_prefilled,student_list_blocked_hours)
    matrix_final=fill_empties(matrix_filled)
    
    #obtener dato de recruiters original de data!
    final_json=fill_data_to_recruiter_list(matrix_final,recruiters_orig)
    print(final_json)

if __name__=="__main__":
    main()
