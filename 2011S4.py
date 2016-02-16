__author__ = 'Daniel'


file = open('2011/s4/s4.5.in')
blood = [int(t) for t in file.readline().split()]
patients = [int(t) for t in file.readline().split()]

steps = ((7, 7),
        (6, 6),
        (6, 7),
        (5, 5),
        (5, 7),
        (3, 3),
        (3, 7),
        (4, 4),
        (4, 6),
        (4, 5),
        (4, 7),
        (2, 2),
        (2, 6),
        (2, 3),
        (2, 7),
        (1, 1),
        (1, 5),
        (1, 3),
        (1, 7),
        (0, 0),
        (0, 4),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 5),
        (0, 6),
        (0, 7))
patient_count = 0
for step in steps:
    s = min(patients[step[1]], blood[step[0]])
    patients[step[1]] -= s
    patient_count += s
    blood[step[0]] -= s
print(patient_count)