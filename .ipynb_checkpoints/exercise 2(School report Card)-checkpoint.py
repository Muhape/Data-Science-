score1 = int(input("Enter your the first score: "))
score2 = int(input("Enter your the second score: "))
score3 = int(input("Enter your the third score: "))
score4 = int(input("Enter your the fourth score: "))
score5 = int(input("Enter your the five score: "))

student = [
    {"name": "Muhape", "score": score1},
    {"name": "David", "score": score2},
    {"name": "Jack", "score": score3},
    {"name": "Sarah", "score": score4},
    {"name": "John", "score": score5},
]
passed = 0
failed = 0

print("=====STUDENT REPORT CARD=======")
for grade in student:
    if grade["score"] >= 90:
        score_board ="A"
    elif grade["score"] >= 80:
        score_board = "B"
    elif grade["score"] >= 70:
        score_board = "C"
    elif grade["score"] >= 60:
        score_board = "D"
    else:
        score_board = "F"
    if grade["score"] >= 50:
       passed = passed + 1
    else:
        failed = failed + 1
    grade["Grade"] = score_board
    print(grade["name"], end=":")
    print(grade["score"], end=":")
    print(grade["Grade"], end="")
    print()
print("============")
print("Total students:5 ")
print(passed,"passed")
print(failed, "failed")