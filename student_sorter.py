students = []

def sort_students(key):
    return sorted(students, key=lambda x: x[key])

students.append({"firstname": "Nila", "lastname": "Heydari", "sid": "40112345"})

print("Initial list:")
print(students)

print("\nSorted by firstname:")
print(sort_students("firstname"))
