import json


def validate_age(age):
    try:
        age = int(age)
        if age <= 0:
            raise ValueError("Age must be positive.")
        return age
    except ValueError as e:
        raise ValueError(f"Invalid age: {e}")


def validate_score(score):
    try:
        score = float(score)
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")
        return score
    except ValueError as e:
        raise ValueError(f"Invalid score: {e}")


def add_student(students):
    try:
        name = input("Enter student name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")
        if name in students:
            raise ValueError("Student already exists.")

        age = validate_age(input("Enter age: "))

        scores = []
        for i in range(1, 4):
            score = validate_score(input(f"Enter score for subject {i}: "))
            scores.append(score)

        students[name] = (age, scores)
        print(f"Student '{name}' added successfully.\n")

    except Exception as e:
        print(f"Error: {e}\n")


def calculate_averages(students):
    averages = {}
    for name, (age, scores) in students.items():
        avg = sum(scores) / len(scores)
        averages[name] = avg
    return averages


def list_above_average(averages):
    try:
        limit = validate_score(input("Enter minimum average score to filter: "))
        result = {name: avg for name, avg in averages.items() if avg >= limit}

        if not result:
            print("No students found above this average.\n")
        else:
            print("\nStudents above the average:")
            for name, avg in result.items():
                print(f"- {name}: {avg:.2f}")
            print()

    except Exception as e:
        print(f"Error: {e}\n")


def save_to_file(students, filename="students.txt"):
    try:
        with open(filename, "w") as file:
            json.dump(students, file)
        print(f"Data saved to {filename}\n")

    except Exception as e:
        print(f"Error saving file: {e}\n")


def read_from_file(filename="students.txt"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        print(f"Data loaded from {filename}\n")
        return data

    except FileNotFoundError:
        print(f"No file named {filename} found.\n")
        return {}

    except Exception as e:
        print(f"Error reading file: {e}\n")
        return {}


def main():
    students = {}

    while True:
        print("=== Student Exam Manager ===")
        print("1. Add Student")
        print("2. Calculate Averages")
        print("3. List Students Above Average")
        print("4. Save to File")
        print("5. Load from File")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            averages = calculate_averages(students)
            print("\nAverages:")
            for name, avg in averages.items():
                print(f"- {name}: {avg:.2f}")
            print()

        elif choice == "3":
            averages = calculate_averages(students)
            list_above_average(averages)

        elif choice == "4":
            save_to_file(students)

        elif choice == "5":
            students = read_from_file()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()