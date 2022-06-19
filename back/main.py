from src.domain.students import get_student_list
from src.domain.recruiter import get_recruiter_list
from src.domain.prematch import *
# from data import recruiters_orig



hours=['10:10','10:20','10:30','10:40','10:50','11:00',"11:20","11:30","11:40","11:50","12:00","12:10","12:30","12:40","12:50"]
	

forced_positions=[['Merkatu','10:10','Perla'],['Merkatu','11:00','Ainara'],
                  ['Ibermatica','11:00','DESCANSO'],['Merkatu','10:20','Ainara']]


def main():
    student_list=get_student_list()
    recruiter_list=get_recruiter_list()
    
    student_list=fill_skills_and_recruiters_in_students(recruiter_list,student_list)
    matrix=generate_matrix(recruiter_list,hours)
    matrix_no_available_hours=fill_recruiter_no_available_spaces(matrix,recruiter_list)
    
    # rellena matriz con las posiciones forzadas
    matrix_prefilled=fill_matrix_with_forced_positions(matrix_no_available_hours,forced_positions)
    # en student_list rellena los horarios y empresa con que se vio el estudiante de los forzados
    student_list_blocked_hours=forced_matches(forced_positions,student_list)
    matrix_filled=match_students(matrix_prefilled,student_list_blocked_hours)
    print(matrix_filled)

    matrix_final=fill_empties(matrix_filled)

    #check
    final_json=fill_data_to_json(matrix_final,recruiters_orig)
    print(final_json)

if __name__=="__main__":
    main()
