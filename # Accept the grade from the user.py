# Accept the grade from the user
grade = float(input("Enter the grade: "))

# Display the grade according to the given criteria
if grade < 25:
    print("Grade: D")
elif 25 <= grade <= 45:
    print("Grade: C")
elif 45 < grade <= 50:
    print("Grade: B")
elif 50 < grade <= 60:
    print("Grade: B+")
elif 60 < grade <= 80:
    print("Grade: A")
else:
    print("Grade: A")
