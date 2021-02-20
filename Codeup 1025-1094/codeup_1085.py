h , b , c ,s = map(int,input().split())

aaa = h * b * c * s

aaa_bit = aaa / 8
aaa_byte = aaa_bit / 1024
aaa_mb = aaa_byte / 1024

print("%.1f MB"%aaa_mb)