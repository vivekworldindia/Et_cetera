students = [
    {"name":"vivek","house":"vivekworld"},
    {"name":"ranjeet","house":"umraha"}
]



houses = set()
for student in students:
    houses.add(student["house"])
        
for house in sorted(houses):
    print(house)
    