students = []
students.append({"firstname": "Ziba", "lastname": "Moradi", "sid": "40112678"})


def sort_students(key):
    return sorted(students, key=lambda x: x[key])

students.append({"firstname": "Nila", "lastname": "Heydari", "sid": "40112345"})
students.append({"firstname": "Fateme", "lastname": "Rahimi", "sid": "40112890"})
print("Initial list:")
print(students)

print("\nSorted by firstname:")
print(sort_students("firstname"))
# minor formatting fix by Ziba