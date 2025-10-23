students =[
    {"name":"vivek","age":19},
    {"name":"ranjeet","age":21},
    {"name":"shobit","age":25},
    {"name":"prince","age":16},
    {"name":"elon musk","age":55}
]

 ### list one
# ages = []
# for student in students:
#     if student["age"] not in ages:
#         ages.append(student["age"])
        

# for age in sorted(ages):
#     print(age)


### set methid 
ages = set()
for student in students:
    ages.add(student["age"])
        

for age in sorted(ages):
    print(age)