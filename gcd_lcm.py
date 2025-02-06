def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

x, y = map(int, input("Enter two numbers: ").split())
gcd = gcd(x,y)
lcm = (x*y)//gcd
print("GCD is",gcd)
print("LCM is",lcm)
