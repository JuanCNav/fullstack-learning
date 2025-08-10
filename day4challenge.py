students=[{"name":"Mayer", "grade":9}, 
          {"name":"Chevy", "grade":8}, 
          {"name":"Naldito","grade":4},
          {"name":"Julian","grade":10}]

while True:
    print("\n--- School List ----")
    print("1- Add a Student")
    print("2- View Students Grades")
    print("3- What is the class average grade?")
    print("4- Who is the Student with the highest grade in the class?")
    print("5- Exit")

    choice = input("Choose:")

    if choice == "1":
        name=input("Name:")
        grade=int(input("Grade:"))
        students.append({"name":name,"grade": grade})
        print("Student Added!")
    
    elif choice== "2":
        if not students:
            print("No students on database yet")
        else:
            for c in students:
                print(f"{c['name']}, → {c['grade']}")
    elif choice=="3":
        if not students:
            print("No students in the database yet.")
        else:
            total=0
            for k in students:
                total+=int(k['grade'])
            average=total /len(students)
            print(f'Class average for students is {average}')
    elif choice =="4":
        if not students:
            print("No students on database yet")
        else:
            top_student=max(students, key=lambda s: s["grade"])
            print(f"Top student: {top_student['name']} with a grade of {top_student['grade']}")
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")