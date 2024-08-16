#initialize a global counter for registration 10s
registration_counter = 5000

def student_registration():
global registration_counter #use the global counter

#generate the registration id using the current counter value
registration_id = registration_counter
registration_counter += 1 #increment the counter for the next registration

#collecting information from the user
date = input("Enter the registration date (dd/mm/yyyy):")
student_id= input("Enter the student id:")
student_name = input("Enter the student name:")
course_name = input("Enter the course name:")

# Return the collected information and registration id
return date, student_id, student_name, course_name, registration_id

#call the function and get the data:
date, student_id, student_name, course_name, registrtation id

#print the information outside the function
print("/nprinting student registration information:")
print(f"date: {date}")
print(f"Student ID: {student_id}")
print(f"Student Name: {student_name}")
print(f"Course Name: {Course_name}")
print(f"Registration ID: {registration_id}")
