students =[
    {"name":"vivek","age":19},
    {"name":"ranjeet","age":21},
    {"name":"shobit","age":25},
    {"name":"prince","age":16},
    {"name":"elon musk","age":55}
]

# ages =[
#     student["name"] for student in students if student["age"] == 19
# ]

# for age in sorted(ages):
#     print(age)
    
    ### use filter 
    
# students =[
#     {"name":"vivek","age":19},
#     {"name":"ranjeet","age":21},
#     {"name":"shobit","age":25},
#     {"name":"prince","age":16},
#     {"name":"elon musk","age":55}
# ]

# def is_ages(s):
#     return s["age"]==55

# ages = filter(is_ages, students)
# for age in sorted(ages, key=lambda s: s["name"]):
#     print(age["name"])


# students = ["Hermione","Harry","Ron"]

# gryffindors = [{"name":student,"house":"Gryffindor"} for student in students]

# for student in students:
#     gryffindors.append({"name":student, "house":"Gryffindor"})

### distionary comprehension
# gryffindors = {student:"Gryffindor" for student in students}


# print(gryffindors)

students = ["Hermione","Harry","Ron"]

# for i in range(len(students)):
#     print(i+1,students[i])

### enumerater

for i,student in enumerate(students):
    print(i+1,student)