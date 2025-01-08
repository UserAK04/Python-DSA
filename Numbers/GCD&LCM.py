n1 = 36
n2 = 24

dividend = n1
divisor = n2 

while dividend % divisor != 0:
    rem = dividend % divisor
    dividend = divisor
    divisor = rem

gcd = divisor
lcm = n1*n2//gcd

# OR
# import math
# gcd = math.gcd(n1,n2)
# lcm = n1*n2//gcd

print([lcm, gcd])
