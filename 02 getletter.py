from itertools import count


print("Enter a string -:")
string = eval(input())

print("Enter position number you can get access-:")
s1 = eval(input())

length = len(string)
if(length < s1 or s1 < 0):
    print("invalid position enter :")
else:
    print(string[s1])
    
        