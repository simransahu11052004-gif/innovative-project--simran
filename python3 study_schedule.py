def generate_schedule():
    print("AUTO STUDY SCHEDULE GENERATOR")
    n = int(input("Enter number of subjects: "))

    subjects = []
    for i in range(n):
        name = input(f"Enter subject {i+1} name: ")
        difficulty = int(input(f"Enter difficulty level for {name} (1=Easy, 2=Medium, 3=Hard): "))
        subjects.append({"name": name, "difficulty": difficulty})

    total_time = float(input("Enter total available study time (in hours): "))

    # Calculate total difficulty sum
    total_difficulty = sum(sub["difficulty"] for sub in subjects)

    print("\n------ GENERATED STUDY SCHEDULE ------")
    for sub in subjects:
        sub_time = (sub["difficulty"] / total_difficulty) * total_time
        print(f"{sub['name']:<15} | Difficulty: {sub['difficulty']} | Time: {sub_time:.2f} hours")

    print("\nSchedule successfully generated based on difficulty levels!")


# Run the function
generate_schedule()
