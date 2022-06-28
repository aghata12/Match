
def convert_locations(student):
    locations=[]
    for key, value in student.items():
        if key.startswith("L-") and (value == "x" or value=='X'):
            locations.append(key[2:])
    return locations

def convert_skills(student):
    skills=[]
    for key, value in student.items():
        if key.startswith("S-") and (value == "x" or value=='X'):
            skills.append(key[2:])
    return skills

def get_student_list(students):
    student_list=[]
    for student in students:
        locations=convert_locations(student)
        skills=convert_skills(student)

        to_add={
            "NOMBRE Y APELLIDOS": student['NOMBRE Y APELLIDOS'],
            "PROMOCION": student["PROMOCION"],
            "LOCATIONS":locations,
            "SKILLS":skills,
            "PMATCH":[],
            "DONE":[],
            "BLOCKEDH":[]
        }
        student_list.append(to_add)
    return student_list