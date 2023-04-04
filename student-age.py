def is_student_adult():
    name = input("input your name: ")
    date_of_birth = int(input("date of birth: "))
    current_year = 2023  
    age = current_year - date_of_birth
    if age >= 18:
       print(age, "years is etucTrue") 
    else:
        print(age,"years is False" )
# birth_year = 2005  # Change this to the student's actual birth year.
# if is_student_adult(birth_year):
#     print("The student is an adult.")
# else:
#     print("The student is not an adult.")


is_student_adult()
