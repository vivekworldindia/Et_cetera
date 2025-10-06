# def meow(n: int) -> str :
#     return "meow\n"*n
        
# number: int  =  int(input("Number: "))
# meows: str = meow(number)
# print(meows,end="")


# import sys 

# if len(sys.argv) ==1:
#     print("meow")
# elif  len(sys.argv) == 3 and sys.argv[1] =="-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
    
# else:
#     print("usage:meow.py")


import argparse

parser = argparse.ArgumentParser(description="I am founder of vivekworld ")
parser.add_argument("-n",default=1,help="i am founder of vivekworld ",type=int)
args = parser.parse_args()


for _ in range(int(args.n)):
    print("meow")