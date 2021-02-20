aa = int(input() ,16)

for i in range(1,16):

    print(("%X" %aa) + "*" + ("%X"%i)+"="+("%X" %(aa*i)))

