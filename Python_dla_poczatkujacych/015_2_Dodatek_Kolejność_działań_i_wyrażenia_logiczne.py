but = 45
print(((but * 5 + 50) * 20 + 1020) - 1993)

nieujemnaCalkowita = 77
print((nieujemnaCalkowita + 10/ 2 - nieujemnaCalkowita))

print(2+2*2)
print(7+7/7+7*7-7)

student1Presence = 0.85
student1Average = 3.5
student1SemesterPaper = False

student1FailOrNot = student1Presence >= 0.80 and student1Average >= 3.0 or student1SemesterPaper
print(student1FailOrNot)
updateStudent1FailOrNot = student1Presence >= 0.80 and student1Average >= 3.0 and student1SemesterPaper
print(updateStudent1FailOrNot)

student2Presence = 0.40
student2Average = 2.5
student2SemesterPaper = True

student2FailOrNot = student2Presence >= 0.80 and student2Average >= 3.0 or student2SemesterPaper
print(student2FailOrNot)
updateStudent2FailOrNot = student2Presence >= 0.80 and student2Average >= 3.0 and student2SemesterPaper
print(updateStudent2FailOrNot)