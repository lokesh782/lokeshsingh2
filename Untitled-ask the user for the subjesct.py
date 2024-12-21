# Input: Ask the user for the subject score
score = float(input("Enter your subject score: "))

# Check the score and give feedback accordingly
if score > 90:
    print("Congratulations! You have done an excellent job.")
elif 50 <= score <= 90:
    print("Good job! But there's room for improvement. Keep working hard.")
else:
    print("You need to retake the course. Don't give up, try again!")
