

filename = input("Enter filename:") 

lines = []

try: 
    with open (filename,"r") as f: 
        lines = f.readlines()
    
except FileNotFoundError:
    print("File not found, check name of input file")

else: 
        
    # removing the "\n" so we can work with the data
    lines_cleaned = []
    for l in lines:
        cleaned = l.replace("\n","")
        lines_cleaned.append(cleaned)

    # number of students 
    num_students = len(lines_cleaned)

    # getting the grades of the students as numbers
    grades = []
    for v in lines_cleaned: 
        split = v.split(",")
        grades.append(split)

    number_grade = []
    non_numeric_grade_error=False
    
    for s in grades:     
        try:
            grade_value = float(s[1])
        except ValueError: 
            print("grade values must be numeric") # this would catch empty grades and non-numeric grades
            non_numeric_grade_error=True
        else:
            number_grade.append(grade_value)    
    try: 
        student_ids = []
        for id in lines_cleaned: 
            split = id.split(",")
            ids = split[0] 
            student_ids.append(ids)

        for i in student_ids: 
            if i.isdigit()==False: 
                print('student id must be numeric')
    except ValueError:
        print('student id must be numberic') 
    
    if non_numeric_grade_error==False:
        # average grade  
        total_grades = sum(number_grade)
        avg_grade = total_grades/num_students

        # highest and lowest grade 
        highest_grade = max(number_grade)
        lowest_grade = min(number_grade)

        # stats to ouput
        num_students_output = f'Number of students in file: {num_students}'
        avg_grade_output = f'Average of grades: {avg_grade}'
        highest_grade_output = f'Highest grade: {highest_grade}'
        lowest_grade_output = f'Lowest grade: {lowest_grade}'

        # Output to screen 
        print(num_students_output)
        print(avg_grade_output)
        print(highest_grade_output)
        print(lowest_grade_output) 

        stats = [num_students_output+"\n",avg_grade_output+"\n",highest_grade_output+"\n",lowest_grade_output+"\n"]

        # write data to file 
        with open("results.txt", 'w') as f:
            for s in stats: 
                f.writelines(s)






