data = [
    ("Sara", "Math", 12, "G1"),
    ("Sara", "Info", 14, "G1"),
    ("Ahmed", "Math", 9, "G2"),
    ("Adam", "Chimie", 18, "G1"),
    ("Sara", "Math", 11, "G1"),
    ("Bouchra", "Info", "abc", "G2"),
    ("", "Math", 10, "G1"),
    ("Yassine", "Info", 22, "G2"),
    ("Ahmed", "Info", 13, "G2"),
    ("Adam", "Math", None, "G1"),
    ("Sara", "Chimie", 16, "G1"),
    ("Adam", "Info", 7, "G1"),
    ("Ahmed", "Math", 9, "G2"),
    ("Hana", "Physique", 15, "G3"),
    ("Hana", "Math", 8, "G3"),
    # more data (par ai)
    ("Ines", "Math", 2, "G2"),
    ("Ines", "Info", 20, "G2"),
    ("Ines", "Chimie", 11, "G2"),
    ("Kenan", "Math", 15, "G1"),
    ("Kenan", "Math", 14, "G1"),
    ("Kenan", "Math", 16, "G1"),
    ("Kenan", "Info", 12, "G1"),
    ("Lamine", "Math", 5, "G4"),
    ("Lamine", "Info", 8, "G4"),
    ("Chloe", "Math", 7, "G4"),
    ("Chloe", "Info", 6, "G4"),
    ("Lina", "Math", 19, "G3"),
    ("Max", "Info", -5, "G1"),
    ("Max", "Math", 25, "G1"),
    ("Sami", "Physique", "N/A", "G3"),
    (None, "Math", 12, "G2"),
    ("Yanis", "", 15, "G2"),
]


#validation
def validate(record):
    if not record[0]:
        return False, "raison : nom vide"
    if record[2] not in range(0, 20):
        return False, "raison : note pas entre 0 et 20"
    if record[1] == "" or record[1] is None:
        return False, "raison : matiere vide"
    if record[3] == "" or record[3] is None:
        return False, "raison : groupe vide"

    return True, ""


valid_data = []
errors = []
exact_duplicates = set()
seen_records = []

for record in data:
    if data.count(record) > 1:
        exact_duplicates.add(record)

    record_check = validate(record)
    if record_check[0] and record:
        cleaned_record = (record[0], record[1], float(record[2]), record[3])
        valid_data.append(cleaned_record)
    else:
        errors.append({"ligne": record, "raison": record_check[1]})

print("-----------------------------------------")
print(f"valides : {len(valid_data)}")
print(f"erreurs : {len(errors)}")
print(f"doubles : {len(exact_duplicates)}")
print("-----------------------------------------\n")

#structure
all_subjects = set()
for record in valid_data:
    all_subjects.add(record[1])

students_tree = {}  #{ "Sara": {"Math": [12.0, 11.0], "Info": [14.0]} }
for record in valid_data:
    if record[0] not in students_tree:
        students_tree[record[0]] = {}
    if record[1] not in students_tree[record[0]]:
        students_tree[record[0]][record[1]] = []
    students_tree[record[0]][record[1]].append(record[2])

groups = {}  # { "G1": {"Sara", "Adam"} }
for record in valid_data:
    if record[3] not in groups:
        groups[record[3]] = set()
    groups[record[3]].add(record[0])


# calcul
def recursive_sum(numbers, index=0):
    if index == len(numbers):
        return 0
    return numbers[index] + recursive_sum(numbers, index + 1)


def calculate_average(numbers):
    return recursive_sum(numbers) / len(numbers)


print("\n------------------------------------------------------")
for student in students_tree:
    subjects = students_tree[student]

    all_grades = []
    print(f"\netudiant : {student}")

    for sub in subjects:
        grades = subjects[sub]
        avg_sub = calculate_average(grades)
        all_grades.append(avg_sub)
        print(f"moyenne de {sub} : {avg_sub}")

    overall_avg = calculate_average(all_grades)
    print(f"moyenne generale : {overall_avg}")


#analyse
alerts = []
#nombre de note > 1 pour une matiere
for student in students_tree:
    subjects = students_tree[student]
    for sub in subjects:
        grades = subjects[sub]
        if len(grades) > 1:
            alerts.append(
                {
                    "type": "nombre de notes > 1",
                    "info": f"{student} a {len(grades)} notes en {sub}",
                }
            )

#n'a pas toutes les matieres
for student in students_tree:
    student_data = students_tree[student]

    if len(student_data) < len(all_subjects):
        alerts.append(
            {"type": "manque des matieres", "info": f"{student} manque des matiere"}
        )

#groupes avec moyenne faible (< 10)
for group in groups:
    students_in_group = groups[group]
    group_grades = []

    for record in valid_data:
        if record[3] == group:
            group_grades.append(record[2])

    group_avg = calculate_average(group_grades)

    if group_avg < 10:
        alerts.append(
            {
                "type": "note de groupe est faible",
                "info": f"groupe {group} a une moyenne de {group_avg}",
            }
        )


#notes instables (max - min > 10)
for student in students_tree:
    subjects = students_tree[student]
    all_grades = []

    for sub in subjects:
        all_grades.extend(subjects[sub])

    diff = max(all_grades) - min(all_grades)

    if diff > 10:
        alerts.append(
            {
                "type": "notes instables",
                "info": f"{student} a un ecart de {diff}",
            }
        )

print("\nalerts :")
for alert in alerts:
    print(f"[{alert['type']}] : {alert['info']}")
