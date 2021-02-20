a,b,c = map(int,input().split())

lcm = 0
while True:
   lcm += 1

   if lcm % a == 0 and lcm % b == 0 and lcm % c == 0 :
       print(lcm)
       break