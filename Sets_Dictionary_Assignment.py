''' 
 Q1) Create a dictionary named student_info with the following keys:          student_name, age, roll_no, class, section, percentage, college_name.

          a) Print all the keys and values from the dictionary.
          b) Add a new key-value pair: 'email': 'student@example.com' to the dictionary.
          c) Delete the section key from the dictionary.
          d) Use a loop to print all key-value pairs in the dictionary in the format:
Key --> Value
          e) Check if the key 'college_name' exists in the dictionary or not.
 
'''

student_info = {"Ramesh" : {"age":18, "roll_no":411, "class": "1st", "section": "A", "percentage":89.25, "college_name":"CBIT"},
"Rajesh" : {"age":19, "roll_no":451, "class": "2nd", "section": "C", "percentage":91.15, "college_name":"VBIT"},
"Rakesh" : {"age":19, "roll_no":345, "class": "3rd", "section": "B", "percentage":98.75, "college_name":"NRIT"},
"Rakesh" : {"age":20, "roll_no":310, "class": "4th", "section": "A", "percentage":96.68, "college_name":"SRIT"}
}

#a) Print all the keys and values from the dictionary.
for key,value in student_info.items():
    print(key,value)
print()

#b) Add a new key-value pair: 'email': 'student@example.com' to the dictionary.
for stu in student_info.keys():
    student_info[stu]["email"]=stu+"@gmail.com"
    
for info in student_info.items():
    print(info)
print()

#c) Delete the section key from the dictionary.
for stu in student_info.keys():
    student_info[stu].pop("section")
for info in student_info.items():
    print(info)
print()

#d) Use a loop to print all key-value pairs in the dictionary in the format: Key --> Value
for stu in student_info.keys():
    print("==============",stu,"==============")
    for key,value in student_info[stu].items():
        print(key,"---->",value)
print("===============================")

#e) Check if the key 'college_name' exists in the dictionary or not.
student_info["Rajesh"].pop("college_name")
for stu in student_info.keys():
    if "college_name" in student_info[stu].keys():
        print("college_name is available for",stu)
    else:
        print("college_name is not available for",stu)
        


'''
Q2) You are given three sets representing students enrolled in different courses:
 
python_students = {"Alice", "Bob", "Charlie", "David"}
java_students = {"Bob", "Eve", "Frank", "David"}
cpp_students = {"Charlie", "George", "Eve", "Henry"}
Find students who are enrolled in all three courses.
Find students who are enrolled in only Python course.
Find students who are enrolled in both Python and Java.
Find students who are enrolled in either Python or Java but not both.
Find the list of all unique students enrolled in any course.
Find students who are in Java or C++, but not in Python.
Check if all Python students are also Java students.
Add a new student "Jones" to the Python set.
Remove "Frank" from the Java set.
Clear the cpp_students set.
'''
print("================================================")
print("==================== Q2 ========================")
print("================================================")
print()

python_students = {"Alice", "Bob", "Charlie", "David"}
java_students = {"Bob", "Eve", "Frank", "David"}
cpp_students = {"Charlie", "George", "Eve", "Henry"}

#Find students who are enrolled in all three courses.
common = python_students & java_students  & cpp_students
if common:
    print(common)
else:
    print("No one enrolled in all three courses")

#Find students who are enrolled in only Python course.
print(python_students.difference(java_students).difference(cpp_students))

#Find students who are enrolled in both Python and Java.
print(python_students & java_students )

#Find students who are enrolled in either Python or Java but not both.
print(java_students^python_students)
#Find the list of all unique students enrolled in any course.
print(java_students^python_students ^ cpp_students)

#Find students who are in Java or C++, but not in Python.
print((java_students & cpp_students).difference(python_students))

#Check if all Python students are also Java students.
print(python_students.issubset(java_students))

#Add a new student "Jones" to the Python set.
python_students.add("Jones")
print(python_students)

#Remove "Frank" from the Java set.
java_students.remove("Frank") 
# (or)
java_students.discard("Frank") 
print(java_students)

#Clear the cpp_students set.
cpp_students.clear()
print(cpp_students)
