def is_student_adult():
    name = input("input your name: ")
    date_of_birth = int(input("date of birth: "))
    current_year = 2023  
    age = current_year - date_of_birth
    if age >= 18:
       print(age, "years is True") 
    else:
        print(age,"years is False" )


is_student_adult()
