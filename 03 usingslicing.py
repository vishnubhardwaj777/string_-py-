import string


print("Enter a string :)")
string = eval(input())

print("Enter a start position :)")
s1 = int(input())
print("Enter a last position :)")
s2 = int(input())

ans = 0
length = len(string)

if(s1<0 or s1<length or s2<0 or s2<length ):
    ans = slice(s1,s2)
    print(string[ans])