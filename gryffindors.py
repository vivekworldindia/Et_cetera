students = [
    {"name":"vivek","house":"vivekworld"},
    {"name":"vivek_one","house":"vivekworld"},
    {"name":"ranjeet","house":"umraha"}
]


def is_gryffindor(s):
   return   s["house"] == "vivekworld"

gryffindors = filter(is_gryffindor,students)

for gryffindor in sorted(gryffindors,key=lambda s: s["name"]):
    print(gryffindor["name"])