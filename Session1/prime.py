import math

n = int(input("Enter a number: "))
count = 0
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        count+=1
if(count == 1):
    print("Prime") 
else:
    print("Not Prime")