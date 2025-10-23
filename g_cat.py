# def main():
#    n = int(input("What's n? "))
#    for c in cat(n):
#        print(c)
      
# def cat(n):
#     flock = []
#     for n in range(n):
#         flock.append("🐈"*n)
#     return flock
    
# if __name__ == "__main__":
#     main()


def main():
   n = int(input("What's n? "))
   for c in cat(n):
       print(c)
      
def cat(n):
   for i in range(n):
       yield "🐈"*i
if __name__ == "__main__":
    main()