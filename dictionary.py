'''
Create an empty dictionary called bird
Add name, color, breed, legs, age to the bird dictionary
'''

bird = {}
li = ["name", "color", "breed", "legs", "age"]
for x in li:
    bird.setdefault(x)


for x in bird:
    temp = input(f"please Enter { x} :=")
    
    if temp.isdecimal():
        bird[x] = int(temp)
    else:
        bird[x] = temp
        
print(bird)
print()    
'''
Create a student dictionary and add first_name, last_name, gender, age, marital_status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries
'''
student= {"first_name":"Rakesh", "last_name":"Nagaram", "gender":"Male", "age":30, "marital_status":"Married", "skills":[], "country":"india", "city":"Benguluru","address":"Mahadevpura"}

print("student dictionary length = ", len(student))


print("Type of student skills = ",type(student["skills"]))
student["skills"].append("c")
student["skills"].append("c++")
student["skills"].append("python")

print(student["skills"])
print()

print(list(student.keys()))
print()

print(list(student.values()))
print()

print(list(student.items()))
print()

#removes particular item
print(student.pop("marital_status"))
print(student)
print()

#removes any of the item
student.popitem()

#clears the dictionary
student.clear()
print(student)
print()

#Deletes entire dictionary
del student 
