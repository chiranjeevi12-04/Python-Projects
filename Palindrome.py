x = "aba"
y = len(x)-1
comp = ""
for i in range(y,-1,-1):
    comp += x[i]
if comp == x:
    print("it is a palindrome")
else:
    print("its not palin")



s = "abcdefgfedcba"
x = len(s)/2
y = s[len(s):int(x-1):-1]
intial = True
for i in range(int(x)):
    if s[i] != y[i]:
       intial = False
       break
if intial:
    print("yes")
else:
    print("no")


