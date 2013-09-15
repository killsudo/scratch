lloyd = {
    "name": 'Lloyd',
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
    }
alice = {
    "name": 'Alice',
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
    }
tyler = {
    "name": 'Tyler',
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
    }

students = [lloyd, alice, tyler]


# Calcuate the students average by taking the student
# grades and calculating the average of the sum of the grades.


def average(lst):
    total = sum(lst)
    average = float(total) / len(lst)
    return average


# Calculating the students weighted average of
# all grade assignments.


def get_average(student):
    weighted_average = 0
    weighted_average += average(student['homework']) * 0.10
    weighted_average += average(student['quizzes']) * 0.30
    weighted_average += average(student['tests']) * 0.60
    return weighted_average


#Match the a point average to a grade letter


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score < 60:
        return "F"


# Generate a average grade point across all students in the class


def get_class_average(class_list):
    class_total = 0
    for student in class_list:
        class_total += get_average(student)
    average = float(class_total) / len(class_list)
    return average


for name in students:
    print "%s" % name['name']
    print "%s" % name["homework"]
    print "%s" % name["quizzes"]
    print "%s" % name["tests"]


print get_letter_grade(get_average(lloyd))
print get_class_average(students)
print get_letter_grade(get_class_average(students))
