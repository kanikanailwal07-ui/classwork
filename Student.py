# Create Nested Dictionary
students = {
    "Rahul": {"Math": 85, "Science": 90, "English": 88},
    "Priya": {"Math": 78, "Science": 95, "English": 82},
    "Ankit": {"Math": 91, "Science": 89, "English": 94}
}

# Initialize variables
topper = ""
highest_total = 0

subject_highest = {
    "Math": ("", 0),
    "Science": ("", 0),
    "English": ("", 0)
}

# Calculate total, average and topper
for name in students:

    total = 0

    for subject in students[name]:
        total = total + students[name][subject]

        # Check subject-wise highest marks
        if students[name][subject] > subject_highest[subject][1]:
            subject_highest[subject] = (name, students[name][subject])

    average = total / 3

    print(name)
    print("Total Marks =", total)
    print("Average Marks =", average)

    # Check topper
    if total > highest_total:
        highest_total = total
        topper = name

print("\nTopper =", topper, "with", highest_total, "marks")

# Display subject-wise highest marks
print("\nSubject-wise Highest Marks:")
for subject in subject_highest:
    print(subject, ":", subject_highest[subject][0], "-", subject_highest[subject][1])

# Display students whose average is greater than or equal to 85
print("\nStudents with average >= 85:")
for name in students:

    total = 0
    for subject in students[name]:
        total = total + students[name][subject]

    average = total / 3

    if average >= 85:
        print(name)
