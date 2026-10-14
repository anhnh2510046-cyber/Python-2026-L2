import pandas as pd

df = pd.read_csv("students.csv")

print("5 dong dau tien")
print(df.head())
print()

rows, cols = df.shape
print(f"Kich thuoc bang")
print(f"So dong: {rows}, So cot: {cols}")
print()

print("Cot name va gpa")
name_gpa = df[["name", "gpa"]]
print(name_gpa)
print()

print("Sinh vien co GPA >= 3.5")
high_gpa = df[df["gpa"] >= 3.5]
print(high_gpa)
print()

print("Sap xep theo GPA giam dan")
sorted_by_gpa = df.sort_values("gpa", ascending=False)
print(sorted_by_gpa)
print()

print("GPA trung binh theo nganh")
avg_gpa_by_major = df.groupby("major")["gpa"].mean().round(3)
print(avg_gpa_by_major)
