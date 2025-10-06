students = ["Hermione","Harry","Ron"]

gryffindors =[]

# for student in students:
#     gryffindors.append({"name":student,"house":"Gryffindor"})
    
#     print(gryffindors)

# gryffindors = [{"name":student,"house":'Gryffindor'} for student in students]

# gryffindors = {student:"Gryffindor" for student in students}
# print(gryffindors)

# for i in range(len(students)):
#     print(i+1, students[i])

for i , student in enumerate(students):
    print(i+1,students[i])