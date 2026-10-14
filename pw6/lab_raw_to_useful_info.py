import pandas as pd

students = pd.read_csv("students.csv")
scores = pd.read_csv("scores.csv")

print("So gia tri thieu trong students.csv")
print(students.isnull().sum())
print()
print("So gia tri thieu trong scores.csv")
print(scores.isnull().sum())
print()

students["age"] = students["age"].fillna(students["age"].median())

students["gpa"] = students.groupby("major")["gpa"].transform(
    lambda g: g.fillna(g.mean())
)

for col in ["python", "math", "database"]:
    scores[col] = scores[col].fillna(scores[col].mean())

print("Sau khi xu ly")
print("students:", students.isnull().sum().sum(), "gia tri thieu con lai")
print("scores:", scores.isnull().sum().sum(), "gia tri thieu con lai")
print()

merged = pd.merge(students, scores, on="student_id", how="inner")
print("Du lieu sau khi merge (5 dong dau)")
print(merged.head())
print()

merged["avg_score"] = merged[["python", "math", "database"]].mean(axis=1).round(2)

print("Top 5 sinh vien diem trung binh cao nhat")
top5 = merged.sort_values("avg_score", ascending=False).head(5)
print(top5[["student_id", "name", "major", "avg_score"]])
print()

print("Diem trung binh theo nganh")
avg_score_by_major = merged.groupby("major")["avg_score"].mean().round(2)
print(avg_score_by_major)
